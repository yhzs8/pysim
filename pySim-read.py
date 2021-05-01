#!/usr/bin/env python2

#
# Utility to display some informations about a SIM card
#
#
# Copyright (C) 2009  Sylvain Munaut <tnt@246tNt.com>
# Copyright (C) 2010  Harald Welte <laforge@gnumonks.org>
# Copyright (C) 2013  Alexander Chemeris <alexander.chemeris@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import hashlib
from optparse import OptionParser
import os
import random
import re
import sys
from pySim.ts_51_011 import EF, DF, EF_SST_map
from pySim.ts_31_102 import EF_UST_map, EF_USIM_ADF_map
from pySim.ts_31_103 import EF_IST_map

from pySim.commands import SimCardCommands
from pySim.cards import card_detect, Card
from pySim.utils import h2b, swap_nibbles, rpad, dec_imsi, dec_iccid, dec_msisdn
from pySim.utils import format_xplmn_w_act, dec_spn, dec_st, init_reader, dec_epdgid

def parse_options():

	parser = OptionParser(usage="usage: %prog [options]")

	parser.add_option("-d", "--device", dest="device", metavar="DEV",
			help="Serial Device for SIM access [default: %default]",
			default="/dev/ttyUSB0",
		)
	parser.add_option("-b", "--baud", dest="baudrate", type="int", metavar="BAUD",
			help="Baudrate used for SIM access [default: %default]",
			default=9600,
		)
	parser.add_option("-p", "--pcsc-device", dest="pcsc_dev", type='int', metavar="PCSC",
			help="Which PC/SC reader number for SIM access",
			default=None,
		)
	parser.add_option("--modem-device", dest="modem_dev", metavar="DEV",
			help="Serial port of modem for Generic SIM Access (3GPP TS 27.007)",
			default=None,
		)
	parser.add_option("--modem-baud", dest="modem_baud", type="int", metavar="BAUD",
			help="Baudrate used for modem's port [default: %default]",
			default=115200,
		)
	parser.add_option("--osmocon", dest="osmocon_sock", metavar="PATH",
			help="Socket path for Calypso (e.g. Motorola C1XX) based reader (via OsmocomBB)",
			default=None,
		)

	(options, args) = parser.parse_args()

	if args:
		parser.error("Extraneous arguments")

	return options


if __name__ == '__main__':

	# Parse options
	opts = parse_options()

	# Init card reader driver
	sl = init_reader(opts)

	# Create command layer
	scc = SimCardCommands(transport=sl)

	# Wait for SIM card
	sl.wait_for_card()

	# Assuming UICC SIM
	scc.cla_byte = "00"
	scc.sel_ctrl = "0004"

	# Testing for Classic SIM or UICC
	(res, sw) = sl.send_apdu(scc.cla_byte + "a4" + scc.sel_ctrl + "02" + "3f00")
	if sw == '6e00':
		# Just a Classic SIM
		scc.cla_byte = "a0"
		scc.sel_ctrl = "0000"

	# Program the card
	print("Reading ...")

	# Initialize Card object by auto detecting the card
	card = card_detect("auto", scc) or Card(scc)

	# Read all AIDs on the UICC
	card.read_aids()

	# EF.ICCID
	(res, sw) = card.read_iccid()
	if sw == '9000':
		print("ICCID: %s" % (res,))
	else:
		print("ICCID: Can't read, response code = %s" % (sw,))

	card.select_aid()

	# EF.IMSI
	(res, sw) = card.read_imsi()
	if sw == '9000':
		print("IMSI: %s" % (res,))
	else:
		print("IMSI: Can't read, response code = %s" % (sw,))

	# EF.GID1
	try:
		(res, sw) = card.read_gid1()
		if sw == '9000':
			print("GID1: %s" % (res,))
		else:
			print("GID1: Can't read, response code = %s" % (sw,))
	except Exception as e:
		print("GID1: Can't read file -- %s" % (str(e),))

	# EF.GID2
	try:
		(res, sw) = card.read_binary('GID2')
		if sw == '9000':
			print("GID2: %s" % (res,))
		else:
			print("GID2: Can't read, response code = %s" % (sw,))
	except Exception as e:
		print("GID2: Can't read file -- %s" % (str(e),))

	# EF.SMSP
	(res, sw) = card.read_record('SMSP', 1)
	if sw == '9000':
		print("SMSP: %s" % (res,))
	else:
		print("SMSP: Can't read, response code = %s" % (sw,))

	# EF.SPN
	try:
		(res, sw) = card.read_spn()
		if sw == '9000':
			print("SPN: %s" % (res[0] or "Not available"))
			print("Display HPLMN: %s" % (res[1],))
			print("Display OPLMN: %s" % (res[2],))
		else:
			print("SPN: Can't read, response code = %s" % (sw,))
	except Exception as e:
		print("SPN: Can't read file -- %s" % (str(e),))

	# EF.PLMNsel
	try:
		(res, sw) = card.read_binary('PLMNsel')
		if sw == '9000':
			print("PLMNsel: %s" % (res))
		else:
			print("PLMNsel: Can't read, response code = %s" % (sw,))
	except Exception as e:
		print("PLMNsel: Can't read file -- " + str(e))

	# EF.PLMNwAcT
	try:
		(res, sw) = card.read_plmn_act()
		if sw == '9000':
			print("PLMNwAcT:\n%s" % (res))
		else:
			print("PLMNwAcT: Can't read, response code = %s" % (sw,))
	except Exception as e:
		print("PLMNwAcT: Can't read file -- " + str(e))

	# EF.OPLMNwAcT
	try:
		(res, sw) = card.read_oplmn_act()
		if sw == '9000':
			print("OPLMNwAcT:\n%s" % (res))
		else:
			print("OPLMNwAcT: Can't read, response code = %s" % (sw,))
	except Exception as e:
		print("OPLMNwAcT: Can't read file -- " + str(e))

	# EF.HPLMNAcT
	try:
		(res, sw) = card.read_hplmn_act()
		if sw == '9000':
			print("HPLMNAcT:\n%s" % (res))
		else:
			print("HPLMNAcT: Can't read, response code = %s" % (sw,))
	except Exception as e:
		print("HPLMNAcT: Can't read file -- " + str(e))

	# EF.ACC
	(res, sw) = card.read_binary('ACC')
	if sw == '9000':
		print("ACC: %s" % (res,))
	else:
		print("ACC: Can't read, response code = %s" % (sw,))

	# EF.MSISDN
	try:
		(res, sw) = card.read_msisdn()
		if sw == '9000':
			# (npi, ton, msisdn) = res
			if res is not None:
				print("MSISDN (NPI=%d ToN=%d): %s" % res)
			else:
				print("MSISDN: Not available")
		else:
			print("MSISDN: Can't read, response code = %s" % (sw,))
	except Exception as e:
		print("MSISDN: Can't read file -- " + str(e))

	# EF.AD
	(res, sw) = card.read_binary('AD')
	if sw == '9000':
		print("AD: %s" % (res,))
	else:
		print("AD: Can't read, response code = %s" % (sw,))

	# EF.SST
	(res, sw) = card.read_binary('SST')
	if sw == '9000':
		print("SIM Service Table: %s" % res)
		# Print those which are available
		print("%s" % dec_st(res))
	else:
		print("SIM Service Table: Can't read, response code = %s" % (sw,))

	# Check whether we have th AID of USIM, if so select it by its AID
	# EF.UST - File Id in ADF USIM : 6f38
	if '9000' == card.select_adf_by_aid():
		# EF.UST
		(res, sw) = card.read_binary(EF_USIM_ADF_map['UST'])
		if sw == '9000':
			print("USIM Service Table: %s" % res)
			# Print those which are available
			print("%s" % dec_st(res, table="usim"))
		else:
			print("USIM Service Table: Can't read, response code = %s" % (sw,))

		#EF.ePDGId - Home ePDG Identifier
		try:
			(res, sw) = card.read_binary(EF_USIM_ADF_map['ePDGId'])
			if sw == '9000':
				content = dec_epdgid(res)
				print("ePDGId:\n%s" % (len(content) and content or '\tNot available\n',))
			else:
				print("ePDGId: Can't read, response code = %s" % (sw,))
		except Exception as e:
			print("ePDGId: Can't read file -- " + str(e))

	# Check whether we have th AID of ISIM, if so select it by its AID
	# EF.IST - File Id in ADF ISIM : 6f07
	if '9000' == card.select_adf_by_aid(adf="isim"):
		# EF.IST
		(res, sw) = card.read_binary('6f07')
		if sw == '9000':
			print("ISIM Service Table: %s" % res)
			# Print those which are available
			print("%s" % dec_st(res, table="isim"))
		else:
			print("ISIM Service Table: Can't read, response code = %s" % (sw,))

	# Done for this card and maybe for everything ?
	print("Done !\n")
