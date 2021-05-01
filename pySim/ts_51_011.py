#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Various constants from ETSI TS 151.011
"""

#
# Copyright (C) 2017 Alexander.Chemeris <Alexander.Chemeris@gmail.com>
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

MF_num = '3F00'

DF_num = {
'TELECOM': '7F10',

'GSM': '7F20',
'IS-41': '7F22',
'FP-CTS': '7F23',
'CUSTOM': '7FFF',

'GRAPHICS': '5F50',

'IRIDIUM': '5F30',
'GLOBST': '5F31',
'ICO': '5F32',
'ACeS': '5F33',

'EIA/TIA-553': '5F40',
'CTS': '5F60',
'SOLSA': '5F70',

'MExE': '5F3C',
}

EF_num = {
# MF
'ICCID': '2FE2',
'ELP': '2F05',
'DIR': '2F00',

# DF_TELECOM
'ADN': '6F3A',
'FDN': '6F3B',
'SMS': '6F3C',
'CCP': '6F3D',
'MSISDN': '6F40',
'SMSP': '6F42',
'SMSS': '6F43',
'LND': '6F44',
'SMSR': '6F47',
'SDN': '6F49',
'EXT1': '6F4A',
'EXT2': '6F4B',
'EXT3': '6F4C',
'BDN': '6F4D',
'EXT4': '6F4E',
'CMI': '6F58',
'ECCP': '6F4F',

# DF_GRAPHICS
'IMG': '4F20',

# DF_SoLSA
'SAI': '4F30',
'SLL': '4F31',

# DF_MExE
'MExE-ST': '4F40',
'ORPK': '4F41',
'ARPK': '4F42',
'TPRPK': '4F43',

# DF_GSM
'LP': '6F05',
'IMSI': '6F07',
'Kc': '6F20',
'DCK': '6F2C',
'PLMNsel': '6F30',
'HPPLMN': '6F31',
'CNL': '6F32',
'ACMmax': '6F37',
'SST': '6F38',
'ACM': '6F39',
'GID1': '6F3E',
'GID2': '6F3F',
'PUCT': '6F41',
'CBMI': '6F45',
'SPN': '6F46',
'CBMID': '6F48',
'BCCH': '6F74',
'ACC': '6F78',
'FPLMN': '6F7B',
'LOCI': '6F7E',
'AD': '6FAD',
'PHASE': '6FAE',
'VGCS': '6FB1',
'VGCSS': '6FB2',
'VBS': '6FB3',
'VBSS': '6FB4',
'eMLPP': '6FB5',
'AAeM': '6FB6',
'ECC': '6FB7',
'CBMIR': '6F50',
'NIA': '6F51',
'KcGPRS': '6F52',
'LOCIGPRS': '6F53',
'SUME': '6F54',
'PLMNwAcT': '6F60',
'OPLMNwAcT': '6F61',
# Figure 8 names it HPLMNAcT, but in the text it's names it HPLMNwAcT
'HPLMNAcT': '6F62',
'HPLMNwAcT': '6F62',
'CPBCCH': '6F63',
'INVSCAN': '6F64',
'PNN': '6FC5',
'OPL': '6FC6',
'MBDN': '6FC7',
'EXT6': '6FC8',
'MBI': '6FC9',
'MWIS': '6FCA',
'CFIS': '6FCB',
'EXT7': '6FCC',
'SPDI': '6FCD',
'MMSN': '6FCE',
'EXT8': '6FCF',
'MMSICP': '6FD0',
'MMSUP': '6FD1',
'MMSUCP': '6FD2',
}

DF = {
'TELECOM':  [MF_num, DF_num['TELECOM']],

'GSM':      [MF_num, DF_num['GSM']],
'IS-41':    [MF_num, DF_num['IS-41']],
'FP-CTS':   [MF_num, DF_num['FP-CTS']],
'CUSTOM':   [MF_num, DF_num['CUSTOM']],

'GRAPHICS': [MF_num, DF_num['GRAPHICS']],

'IRIDIUM':  [MF_num, DF_num['IRIDIUM']],
'GLOBST':   [MF_num, DF_num['GLOBST']],
'ICO':      [MF_num, DF_num['ICO']],
'ACeS':     [MF_num, DF_num['ACeS']],

'EIA/TIA-553': [MF_num, DF_num['EIA/TIA-553']],
'CTS':      [MF_num, DF_num['CTS']],
'SoLSA':    [MF_num, DF_num['SOLSA']],

'MExE':     [MF_num, DF_num['MExE']],
}


EF = {
'ICCID':  [MF_num, EF_num['ICCID']],
'ELP':    [MF_num, EF_num['ELP']],
'DIR':    [MF_num, EF_num['DIR']],

'ADN':    DF['TELECOM']+[EF_num['ADN']],
'FDN':    DF['TELECOM']+[EF_num['FDN']],
'SMS':    DF['TELECOM']+[EF_num['SMS']],
'CCP':    DF['TELECOM']+[EF_num['CCP']],
'MSISDN': DF['TELECOM']+[EF_num['MSISDN']],
'SMSP':   DF['TELECOM']+[EF_num['SMSP']],
'SMSS':   DF['TELECOM']+[EF_num['SMSS']],
'LND':    DF['TELECOM']+[EF_num['LND']],
'SMSR':   DF['TELECOM']+[EF_num['SMSR']],
'SDN':    DF['TELECOM']+[EF_num['SDN']],
'EXT1':   DF['TELECOM']+[EF_num['EXT1']],
'EXT2':   DF['TELECOM']+[EF_num['EXT2']],
'EXT3':   DF['TELECOM']+[EF_num['EXT3']],
'BDN':    DF['TELECOM']+[EF_num['BDN']],
'EXT4':   DF['TELECOM']+[EF_num['EXT4']],
'CMI':    DF['TELECOM']+[EF_num['CMI']],
'ECCP':   DF['TELECOM']+[EF_num['ECCP']],

'IMG':    DF['GRAPHICS']+[EF_num['IMG']],

'SAI':    DF['SoLSA']+[EF_num['SAI']],
'SLL':    DF['SoLSA']+[EF_num['SLL']],

'MExE-ST': DF['MExE']+[EF_num['MExE-ST']],
'ORPK':   DF['MExE']+[EF_num['ORPK']],
'ARPK':   DF['MExE']+[EF_num['ARPK']],
'TPRPK':  DF['MExE']+[EF_num['TPRPK']],

'LP':     DF['CUSTOM']+[EF_num['LP']],
'IMSI':   DF['CUSTOM']+[EF_num['IMSI']],
'Kc':     DF['CUSTOM']+[EF_num['Kc']],
'DCK':    DF['CUSTOM']+[EF_num['DCK']],
'PLMNsel': DF['CUSTOM']+[EF_num['PLMNsel']],
'HPPLMN': DF['CUSTOM']+[EF_num['HPPLMN']],
'CNL':    DF['CUSTOM']+[EF_num['CNL']],
'ACMmax': DF['CUSTOM']+[EF_num['ACMmax']],
'SST':    DF['CUSTOM']+[EF_num['SST']],
'ACM':    DF['CUSTOM']+[EF_num['ACM']],
'GID1':   DF['CUSTOM']+[EF_num['GID1']],
'GID2':   DF['CUSTOM']+[EF_num['GID2']],
'PUCT':   DF['CUSTOM']+[EF_num['PUCT']],
'CBMI':   DF['CUSTOM']+[EF_num['CBMI']],
'SPN':    DF['CUSTOM']+[EF_num['SPN']],
'CBMID':  DF['CUSTOM']+[EF_num['CBMID']],
'BCCH':   DF['CUSTOM']+[EF_num['BCCH']],
'ACC':    DF['CUSTOM']+[EF_num['ACC']],
'FPLMN':  DF['CUSTOM']+[EF_num['FPLMN']],
'LOCI':   DF['CUSTOM']+[EF_num['LOCI']],
'AD':     DF['CUSTOM']+[EF_num['AD']],
'PHASE':  DF['CUSTOM']+[EF_num['PHASE']],
'VGCS':   DF['CUSTOM']+[EF_num['VGCS']],
'VGCSS':  DF['CUSTOM']+[EF_num['VGCSS']],
'VBS':    DF['CUSTOM']+[EF_num['VBS']],
'VBSS':   DF['CUSTOM']+[EF_num['VBSS']],
'eMLPP':  DF['CUSTOM']+[EF_num['eMLPP']],
'AAeM':   DF['CUSTOM']+[EF_num['AAeM']],
'ECC':    DF['CUSTOM']+[EF_num['ECC']],
'CBMIR':  DF['CUSTOM']+[EF_num['CBMIR']],
'NIA':    DF['CUSTOM']+[EF_num['NIA']],
'KcGPRS': DF['CUSTOM']+[EF_num['KcGPRS']],
'LOCIGPRS': DF['CUSTOM']+[EF_num['LOCIGPRS']],
'SUME':   DF['CUSTOM']+[EF_num['SUME']],
'PLMNwAcT': DF['CUSTOM']+[EF_num['PLMNwAcT']],
'OPLMNwAcT': DF['CUSTOM']+[EF_num['OPLMNwAcT']],
# Figure 8 names it HPLMNAcT, but in the text it's names it HPLMNwAcT
'HPLMNAcT': DF['CUSTOM']+[EF_num['HPLMNAcT']],
'HPLMNwAcT': DF['CUSTOM']+[EF_num['HPLMNAcT']],
'CPBCCH': DF['CUSTOM']+[EF_num['CPBCCH']],
'INVSCAN': DF['CUSTOM']+[EF_num['INVSCAN']],
'PNN':    DF['CUSTOM']+[EF_num['PNN']],
'OPL':    DF['CUSTOM']+[EF_num['OPL']],
'MBDN':   DF['CUSTOM']+[EF_num['MBDN']],
'EXT6':   DF['CUSTOM']+[EF_num['EXT6']],
'MBI':    DF['CUSTOM']+[EF_num['MBI']],
'MWIS':   DF['CUSTOM']+[EF_num['MWIS']],
'CFIS':   DF['CUSTOM']+[EF_num['CFIS']],
'EXT7':   DF['CUSTOM']+[EF_num['EXT7']],
'SPDI':   DF['CUSTOM']+[EF_num['SPDI']],
'MMSN':   DF['CUSTOM']+[EF_num['MMSN']],
'EXT8':   DF['CUSTOM']+[EF_num['EXT8']],
'MMSICP': DF['CUSTOM']+[EF_num['MMSICP']],
'MMSUP':  DF['CUSTOM']+[EF_num['MMSUP']],
'MMSUCP': DF['CUSTOM']+[EF_num['MMSUCP']],
}

# Mapping between SIM Service Number and its description
EF_SST_map = {
	1: 'CHV1 disable function',
	2: 'Abbreviated Dialling Numbers (ADN)',
	3: 'Fixed Dialling Numbers (FDN)',
	4: 'Short Message Storage (SMS)',
	5: 'Advice of Charge (AoC)',
	6: 'Capability Configuration Parameters (CCP)',
	7: 'PLMN selector',
	8: 'RFU',
	9: 'MSISDN',
	10: 'Extension1',
	11: 'Extension2',
	12: 'SMS Parameters',
	13: 'Last Number Dialled (LND)',
	14: 'Cell Broadcast Message Identifier',
	15: 'Group Identifier Level 1',
	16: 'Group Identifier Level 2',
	17: 'Service Provider Name',
	18: 'Service Dialling Numbers (SDN)',
	19: 'Extension3',
	20: 'RFU',
	21: 'VGCS Group Identifier List (EFVGCS and EFVGCSS)',
	22: 'VBS Group Identifier List (EFVBS and EFVBSS)',
	23: 'enhanced Multi-Level Precedence and Pre-emption Service',
	24: 'Automatic Answer for eMLPP',
	25: 'Data download via SMS-CB',
	26: 'Data download via SMS-PP',
	27: 'Menu selection',
	28: 'Call control',
	29: 'Proactive SIM',
	30: 'Cell Broadcast Message Identifier Ranges',
	31: 'Barred Dialling Numbers (BDN)',
	32: 'Extension4',
	33: 'De-personalization Control Keys',
	34: 'Co-operative Network List',
	35: 'Short Message Status Reports',
	36: 'Network\'s indication of alerting in the MS',
	37: 'Mobile Originated Short Message control by SIM',
	38: 'GPRS',
	39: 'Image (IMG)',
	40: 'SoLSA (Support of Local Service Area)',
	41: 'USSD string data object supported in Call Control',
	42: 'RUN AT COMMAND command',
	43: 'User controlled PLMN Selector with Access Technology',
	44: 'Operator controlled PLMN Selector with Access Technology',
	45: 'HPLMN Selector with Access Technology',
	46: 'CPBCCH Information',
	47: 'Investigation Scan',
	48: 'Extended Capability Configuration Parameters',
	49: 'MExE',
	50: 'Reserved and shall be ignored',
	51: 'PLMN Network Name',
	52: 'Operator PLMN List',
	53: 'Mailbox Dialling Numbers',
	54: 'Message Waiting Indication Status',
	55: 'Call Forwarding Indication Status',
	56: 'Service Provider Display Information',
	57: 'Multimedia Messaging Service (MMS)',
	58: 'Extension 8',
	59: 'MMS User Connectivity Parameters',
}