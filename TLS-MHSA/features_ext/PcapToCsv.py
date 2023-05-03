#!/bin/usr/python
#Tag: json to csv
import argparse
import csv
import demjson
import datetime
import operator 
import numpy 
import pandas 
import argparse
import csv
import demjson
import datetime
import operator 
import numpy 
import os
# Need to change the collection date of the traffic
date=datetime.datetime.strptime("2017-08-16","%Y-%m-%d")

months={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}

csvHeader=['low_src_port', 'tls_dst_port', 'bytes_in', 'bytes_out', 'pkts_in', 'pkts_out', 'duration', 'pkt_lengths_00', 'pkt_lengths_01', 'pkt_lengths_02', 'pkt_lengths_03', 'pkt_lengths_04', 'pkt_lengths_05', 'pkt_lengths_06', 'pkt_lengths_07', 'pkt_lengths_08', 'pkt_lengths_09', 'pkt_lengths_10', 'pkt_lengths_11', 'pkt_lengths_12', 'pkt_lengths_13', 'pkt_lengths_14', 'pkt_lengths_15', 'pkt_lengths_16', 'pkt_lengths_17', 'pkt_lengths_18', 'pkt_lengths_19', 'pkt_lengths_20', 'pkt_lengths_21', 'pkt_lengths_22', 'pkt_lengths_23', 'pkt_lengths_24', 'pkt_lengths_25', 'pkt_lengths_26', 'pkt_lengths_27', 'pkt_lengths_28', 'pkt_lengths_29', 'pkt_lengths_30', 'pkt_lengths_31', 'pkt_lengths_32', 'pkt_lengths_33', 'pkt_lengths_34', 'pkt_lengths_35', 'pkt_lengths_36', 'pkt_lengths_37', 'pkt_lengths_38', 'pkt_lengths_39', 'pkt_lengths_40', 'pkt_lengths_41', 'pkt_lengths_42', 'pkt_lengths_43', 'pkt_lengths_44', 'pkt_lengths_45', 'pkt_lengths_46', 'pkt_lengths_47', 'pkt_lengths_48', 'pkt_lengths_49', 'pkt_lengths_50', 'pkt_lengths_51', 'pkt_lengths_52', 'pkt_lengths_53', 'pkt_lengths_54', 'pkt_lengths_55', 'pkt_lengths_56', 'pkt_lengths_57', 'pkt_lengths_58', 'pkt_lengths_59', 'pkt_lengths_60', 'pkt_lengths_61', 'pkt_lengths_62', 'pkt_lengths_63', 'pkt_lengths_64', 'pkt_lengths_65', 'pkt_lengths_66', 'pkt_lengths_67', 'pkt_lengths_68', 'pkt_lengths_69', 'pkt_lengths_70', 'pkt_lengths_71', 'pkt_lengths_72', 'pkt_lengths_73', 'pkt_lengths_74', 'pkt_lengths_75', 'pkt_lengths_76', 'pkt_lengths_77', 'pkt_lengths_78', 'pkt_lengths_79', 'pkt_lengths_80', 'pkt_lengths_81', 'pkt_lengths_82', 'pkt_lengths_83', 'pkt_lengths_84', 'pkt_lengths_85', 'pkt_lengths_86', 'pkt_lengths_87', 'pkt_lengths_88', 'pkt_lengths_89', 'pkt_lengths_90', 'pkt_lengths_91', 'pkt_lengths_92', 'pkt_lengths_93', 'pkt_lengths_94', 'pkt_lengths_95', 'pkt_lengths_96', 'pkt_lengths_97', 'pkt_lengths_98', 'pkt_lengths_99', 'pkt_times_00', 'pkt_times_01', 'pkt_times_02', 'pkt_times_03', 'pkt_times_04', 'pkt_times_05', 'pkt_times_06', 'pkt_times_07', 'pkt_times_08', 'pkt_times_09', 'pkt_times_10', 'pkt_times_11', 'pkt_times_12', 'pkt_times_13', 'pkt_times_14', 'pkt_times_15', 'pkt_times_16', 'pkt_times_17', 'pkt_times_18', 'pkt_times_19', 'pkt_times_20', 'pkt_times_21', 'pkt_times_22', 'pkt_times_23', 'pkt_times_24', 'pkt_times_25', 'pkt_times_26', 'pkt_times_27', 'pkt_times_28', 'pkt_times_29', 'pkt_times_30', 'pkt_times_31', 'pkt_times_32', 'pkt_times_33', 'pkt_times_34', 'pkt_times_35', 'pkt_times_36', 'pkt_times_37', 'pkt_times_38', 'pkt_times_39', 'pkt_times_40', 'pkt_times_41', 'pkt_times_42', 'pkt_times_43', 'pkt_times_44', 'pkt_times_45', 'pkt_times_46', 'pkt_times_47', 'pkt_times_48', 'pkt_times_49', 'pkt_times_50', 'pkt_times_51', 'pkt_times_52', 'pkt_times_53', 'pkt_times_54', 'pkt_times_55', 'pkt_times_56', 'pkt_times_57', 'pkt_times_58', 'pkt_times_59', 'pkt_times_60', 'pkt_times_61', 'pkt_times_62', 'pkt_times_63', 'pkt_times_64', 'pkt_times_65', 'pkt_times_66', 'pkt_times_67', 'pkt_times_68', 'pkt_times_69', 'pkt_times_70', 'pkt_times_71', 'pkt_times_72', 'pkt_times_73', 'pkt_times_74', 'pkt_times_75', 'pkt_times_76', 'pkt_times_77', 'pkt_times_78', 'pkt_times_79', 'pkt_times_80', 'pkt_times_81', 'pkt_times_82', 'pkt_times_83', 'pkt_times_84', 'pkt_times_85', 'pkt_times_86', 'pkt_times_87', 'pkt_times_88', 'pkt_times_89', 'pkt_times_90', 'pkt_times_91', 'pkt_times_92', 'pkt_times_93', 'pkt_times_94', 'pkt_times_95', 'pkt_times_96', 'pkt_times_97', 'pkt_times_98', 'pkt_times_99', 'byte_dist_mean', 'byte_dist_std', 'entropy', 'cs_0003', 'cs_0004', 'cs_0005', 'cs_0006', 'cs_0007', 'cs_0008', 'cs_0009', 'cs_000a', 'cs_000d', 'cs_0010', 'cs_0011', 'cs_0012', 'cs_0013', 'cs_0014', 'cs_0015', 'cs_0016', 'cs_002f', 'cs_0030', 'cs_0031', 'cs_0032', 'cs_0033', 'cs_0035', 'cs_0036', 'cs_0037', 'cs_0038', 'cs_0039', 'cs_003c', 'cs_003d', 'cs_003e', 'cs_003f', 'cs_0040', 'cs_0041', 'cs_0042', 'cs_0043', 'cs_0044', 'cs_0045', 'cs_0067', 'cs_0068', 'cs_0069', 'cs_006a', 'cs_006b', 'cs_0084', 'cs_0085', 'cs_0086', 'cs_0087', 'cs_0088', 'cs_0096', 'cs_0097', 'cs_0098', 'cs_0099', 'cs_009a', 'cs_009c', 'cs_009d', 'cs_009e', 'cs_009f', 'cs_00a0', 'cs_00a1', 'cs_00a2', 'cs_00a3', 'cs_00a4', 'cs_00a5', 'cs_00ba', 'cs_00bd', 'cs_00be', 'cs_00c0', 'cs_00c3', 'cs_00c4', 'cs_00ff', 'cs_1301', 'cs_1302', 'cs_1303', 'cs_1304', 'cs_c002', 'cs_c003', 'cs_c004', 'cs_c005', 'cs_c007', 'cs_c008', 'cs_c009', 'cs_c00a', 'cs_c00c', 'cs_c00d', 'cs_c00e', 'cs_c00f', 'cs_c011', 'cs_c012', 'cs_c013', 'cs_c014', 'cs_c016', 'cs_c017', 'cs_c018', 'cs_c019', 'cs_c023', 'cs_c024', 'cs_c025', 'cs_c026', 'cs_c027', 'cs_c028', 'cs_c029', 'cs_c02a', 'cs_c02b', 'cs_c02c', 'cs_c02d', 'cs_c02e', 'cs_c02f', 'cs_c030', 'cs_c031', 'cs_c032', 'cs_c050', 'cs_c051', 'cs_c052', 'cs_c053', 'cs_c056', 'cs_c057', 'cs_c05c', 'cs_c05d', 'cs_c060', 'cs_c061', 'cs_c072', 'cs_c073', 'cs_c076', 'cs_c077', 'cs_c07a', 'cs_c07b', 'cs_c07c', 'cs_c07d', 'cs_c086', 'cs_c087', 'cs_c08a', 
'cs_c08b', 'cs_c09c', 'cs_c09d', 'cs_c09e', 'cs_c09f', 'cs_c0a0', 'cs_c0a1', 'cs_c0a2', 'cs_c0a3', 'cs_c0ac', 'cs_c0ad', 'cs_c0ae','cs_c0af','cs_cca8','cs_cca9','cs_ccaa','cs_ffff', 'ext_0','ext_5','ext_10','ext_11','ext_13','ext_15','ext_16','ext_17','ext_18', 'ext_21', 'ext_22', 'ext_23', 'ext_24', 'ext_35', 'ext_65281', 'ext_65535', 'nb_ext', 'sg_1', 'sg_2', 'sg_3', 'sg_4', 'sg_5', 'sg_6', 'sg_7', 'sg_8', 'sg_9', 'sg_10', 'sg_11', 'sg_12', 'sg_13', 'sg_14', 'sg_15', 'sg_16', 'sg_17', 'sg_18', 'sg_19', 'sg_20', 'sg_21', 'sg_22', 'sg_23', 'sg_24', 'sg_25', 'sg_26', 'sg_27', 'sg_28', 'sg_29', 'sg_30', 'sg_256', 'sg_257', 'sg_258', 'sg_259', 'sg_260', 'sg_65535', 'pf_0', 'pf_1', 'pf_2', 'pf_255', 'key_length', 'validity', 'nb_san', 'self-signed', 'date', 'source', 'family', 'label']

commonTlsDstPorts=[443,465,563,636,853,989,990,992,993,995]

commonTlsSrcPorts=[49152,65535]

extDict={'server_name': 'ext_0', 'status_request': 'ext_5', 'supported_groups': 'ext_10', 'ec_point_formats': 'ext_11', 'signature_alorithms': 'ext_13', 'heartbeat': 'ext_15', 'application_layer_protocol_negotitation': 'ext_16', 'status_request_v2': 'ext_17', 'signed_certificate_timestamp': 'ext_18', 'padding': 'ext_21', 'encrypt_then_mac': 'ext_22', 'extended_master_secret': 'ext_23', 'token_binding': 'ext_24', 'session_ticket': 'ext_35', 'renegotation_info': 'ext_65281','kind':'ext_65535'}

csList=['cs_0003', 'cs_0004', 'cs_0005', 'cs_0006', 'cs_0007', 'cs_0008', 'cs_0009', 'cs_000a', 'cs_000d', 'cs_0010', 'cs_0011', 'cs_0012', 'cs_0013', 'cs_0014', 'cs_0015', 'cs_0016', 'cs_002f', 'cs_0030', 'cs_0031', 'cs_0032', 'cs_0033', 'cs_0035', 'cs_0036', 'cs_0037', 'cs_0038', 'cs_0039', 'cs_003c', 'cs_003d', 'cs_003e', 'cs_003f', 'cs_0040', 'cs_0041', 'cs_0042', 'cs_0043', 'cs_0044', 'cs_0045', 'cs_0067', 'cs_0068', 'cs_0069', 'cs_006a', 'cs_006b', 'cs_0084', 'cs_0085', 'cs_0086', 'cs_0087', 'cs_0088', 'cs_0096', 'cs_0097', 'cs_0098', 'cs_0099', 'cs_009a', 'cs_009c', 'cs_009d', 'cs_009e', 'cs_009f', 'cs_00a0', 'cs_00a1', 'cs_00a2', 'cs_00a3', 'cs_00a4', 'cs_00a5', 'cs_00ba', 'cs_00bd', 'cs_00be', 'cs_00c0', 'cs_00c3', 'cs_00c4', 'cs_00ff', 'cs_1301', 'cs_1302', 'cs_1303', 'cs_1304', 'cs_c002', 'cs_c003', 'cs_c004', 'cs_c005', 'cs_c007', 'cs_c008', 'cs_c009', 'cs_c00a', 'cs_c00c', 'cs_c00d', 'cs_c00e', 'cs_c00f', 'cs_c011', 'cs_c012', 'cs_c013', 'cs_c014', 'cs_c016', 'cs_c017', 'cs_c018', 'cs_c019', 'cs_c023', 'cs_c024', 'cs_c025', 'cs_c026', 'cs_c027', 'cs_c028', 'cs_c029', 'cs_c02a', 'cs_c02b', 'cs_c02c', 'cs_c02d', 'cs_c02e', 'cs_c02f', 'cs_c030', 'cs_c031', 'cs_c032', 'cs_c050', 'cs_c051', 'cs_c052', 'cs_c053', 'cs_c056', 'cs_c057', 'cs_c05c', 'cs_c05d', 'cs_c060', 'cs_c061', 'cs_c072', 'cs_c073', 'cs_c076', 'cs_c077', 'cs_c07a', 'cs_c07b', 'cs_c07c', 'cs_c07d', 'cs_c086', 'cs_c087', 'cs_c08a', 
'cs_c08b', 'cs_c09c', 'cs_c09d', 'cs_c09e', 'cs_c09f', 'cs_c0a0', 'cs_c0a1', 'cs_c0a2', 'cs_c0a3', 'cs_c0ac', 'cs_c0ad', 'cs_c0ae']

supportGroups={'0001':'sect163k1','0002':'sect163r1','0003':'sect163r2','0004':'sect193r1','0005':'sect193r2','0006':'sect233k1','0007':'sect233r1','0008':'sect239k1','0009':'sect283k1','000a':'sect283r1'
            ,'000b':'sect409k1','000c':'sect409r1','000d':'sect571k1','000e':'sect571r1','000f':'secp160k1','0010':'secp160r1','0011':'secp160r2',
            '0012':'secp192k1','0013':'secp192r1','0014':'secp224k1','0015':'secp224r1','0016':'secp256r1','0017':'secp256r1','0018':'secp384r1',
            '0019':'secp521r1','001a':'brainpoolP256r1','001b':'brainpoolP384r1','001c':'brainpoolP512r1','001d':'x25519','001e':'x448','0100':'ffdhe2048','0101':'ffdhe3072','0102':'ffdhe4096','0103':'ffdhe6144','0104':'ffdhe8192','ffff':'unknow'}

ec_point_formats={'00':'pf_0','01':'pf_1','02':'pf_2','ff':'pf_255'}
#{'sg_1': 0, 'sg_2': 0, 'sg_3': 0, 'sg_4': 0, 'sg_5': 0, 'sg_6': 0, 'sg_7': 0, 'sg_8': 0, 'sg_9': 0, 'sg_10': 0, 'sg_11': 0, 'sg_12': 0, 'sg_13': 0, 'sg_14': 0, 'sg_15': 0, 'sg_16': 0, 'sg_17': 0, 'sg_18': 0, 'sg_19': 0, 'sg_20': 0, 'sg_21': 0, 'sg_22': 0, 'sg_23': 0, 
#'sg_24': 0, 'sg_25': 0, 'sg_26': 0, 'sg_27': 0, 'sg_28': 0, 'sg_29': 0, 'sg_30': 0, 'sg_256': 0, 'sg_257': 0, 'sg_258': 0, 'sg_259': 0, 'sg_260': 0}
pktLengths=['pkt_lengths_00', 'pkt_lengths_01', 'pkt_lengths_02', 'pkt_lengths_03', 'pkt_lengths_04', 'pkt_lengths_05', 'pkt_lengths_06', 'pkt_lengths_07', 'pkt_lengths_08', 'pkt_lengths_09', 'pkt_lengths_10', 'pkt_lengths_11', 'pkt_lengths_12', 'pkt_lengths_13', 'pkt_lengths_14', 'pkt_lengths_15', 'pkt_lengths_16', 'pkt_lengths_17', 'pkt_lengths_18', 'pkt_lengths_19', 'pkt_lengths_20', 'pkt_lengths_21', 'pkt_lengths_22', 'pkt_lengths_23', 'pkt_lengths_24', 'pkt_lengths_25', 'pkt_lengths_26', 'pkt_lengths_27', 'pkt_lengths_28', 'pkt_lengths_29', 'pkt_lengths_30', 'pkt_lengths_31', 'pkt_lengths_32', 'pkt_lengths_33', 'pkt_lengths_34', 'pkt_lengths_35', 'pkt_lengths_36', 'pkt_lengths_37', 'pkt_lengths_38', 'pkt_lengths_39', 'pkt_lengths_40', 'pkt_lengths_41', 'pkt_lengths_42', 'pkt_lengths_43', 'pkt_lengths_44', 'pkt_lengths_45', 'pkt_lengths_46', 'pkt_lengths_47', 'pkt_lengths_48', 'pkt_lengths_49', 'pkt_lengths_50', 'pkt_lengths_51', 'pkt_lengths_52', 'pkt_lengths_53', 'pkt_lengths_54', 'pkt_lengths_55', 'pkt_lengths_56', 'pkt_lengths_57', 'pkt_lengths_58', 'pkt_lengths_59', 'pkt_lengths_60', 'pkt_lengths_61', 'pkt_lengths_62', 'pkt_lengths_63', 'pkt_lengths_64', 'pkt_lengths_65', 'pkt_lengths_66', 'pkt_lengths_67', 'pkt_lengths_68', 'pkt_lengths_69', 'pkt_lengths_70', 'pkt_lengths_71', 'pkt_lengths_72', 'pkt_lengths_73', 'pkt_lengths_74', 'pkt_lengths_75', 'pkt_lengths_76', 'pkt_lengths_77', 'pkt_lengths_78', 'pkt_lengths_79', 'pkt_lengths_80', 'pkt_lengths_81', 'pkt_lengths_82', 'pkt_lengths_83', 'pkt_lengths_84', 'pkt_lengths_85', 'pkt_lengths_86', 'pkt_lengths_87', 'pkt_lengths_88', 'pkt_lengths_89', 'pkt_lengths_90', 'pkt_lengths_91', 'pkt_lengths_92', 'pkt_lengths_93', 'pkt_lengths_94', 'pkt_lengths_95', 'pkt_lengths_96', 'pkt_lengths_97', 'pkt_lengths_98', 'pkt_lengths_99']
pktTimes=['pkt_times_00', 'pkt_times_01', 'pkt_times_02', 'pkt_times_03', 'pkt_times_04', 'pkt_times_05', 'pkt_times_06', 'pkt_times_07', 'pkt_times_08', 'pkt_times_09', 'pkt_times_10', 'pkt_times_11', 'pkt_times_12', 'pkt_times_13', 'pkt_times_14', 'pkt_times_15', 'pkt_times_16', 'pkt_times_17', 'pkt_times_18', 'pkt_times_19', 'pkt_times_20', 'pkt_times_21', 'pkt_times_22', 'pkt_times_23', 'pkt_times_24', 'pkt_times_25', 'pkt_times_26', 'pkt_times_27', 'pkt_times_28', 'pkt_times_29', 'pkt_times_30', 'pkt_times_31', 'pkt_times_32', 'pkt_times_33', 'pkt_times_34', 'pkt_times_35', 'pkt_times_36', 'pkt_times_37', 'pkt_times_38', 'pkt_times_39', 'pkt_times_40', 'pkt_times_41', 'pkt_times_42', 'pkt_times_43', 'pkt_times_44', 'pkt_times_45', 'pkt_times_46', 'pkt_times_47', 'pkt_times_48', 'pkt_times_49', 'pkt_times_50', 'pkt_times_51', 'pkt_times_52', 'pkt_times_53', 'pkt_times_54', 'pkt_times_55', 'pkt_times_56', 'pkt_times_57', 'pkt_times_58', 'pkt_times_59', 'pkt_times_60', 'pkt_times_61', 'pkt_times_62', 'pkt_times_63', 'pkt_times_64', 'pkt_times_65', 'pkt_times_66', 'pkt_times_67', 'pkt_times_68', 'pkt_times_69', 'pkt_times_70', 'pkt_times_71', 'pkt_times_72', 'pkt_times_73', 'pkt_times_74', 'pkt_times_75', 'pkt_times_76', 'pkt_times_77', 'pkt_times_78', 'pkt_times_79', 'pkt_times_80', 'pkt_times_81', 'pkt_times_82', 'pkt_times_83', 'pkt_times_84', 'pkt_times_85', 'pkt_times_86', 'pkt_times_87', 'pkt_times_88', 'pkt_times_89', 'pkt_times_90', 'pkt_times_91', 'pkt_times_92', 'pkt_times_93', 'pkt_times_94', 'pkt_times_95', 'pkt_times_96', 'pkt_times_97', 'pkt_times_98', 'pkt_times_99']

# calc the 10*10 random matrix,fill in 0 if the number of dimensions is insufficient
def calcRandomMatrix(dataArray):
    metedata=numpy.array(dataArray)
    count={}
    for i in metedata[0:len(metedata) - 1]:
        count[i] = count.get(i, 0) + 1
    count = sorted(count.items(), key=operator.itemgetter(0), reverse=False)
 
    markovMarix = numpy.zeros([len(count), len(count)])
    for j in range(len(metedata) - 1):
        for m in range(len(count)):
            for n in range(len(count)):
                if metedata[j] == count[m][0] and metedata[j + 1] == count[n][0]:
                    markovMarix[m][n] += 1
    for t in range(len(count)):
        markovMarix[t, :] /= count[t][1]
    marixLength=len(markovMarix)
    if (marixLength<10 and marixLength>0):
        markovMarix=numpy.pad(markovMarix,(0,10-marixLength),'constant',constant_values=(0,0))
    return markovMarix


# common features class
# include getPortInfor,getBytesInfor,getPktsInfor,getEntropyInfor
class commonFeature(object):
    def __init__(self,data):
        self.srcPort=data['sp']
        self.dstPort=data['dp']
        self.bytesOut={'bytes_out':data['bytes_out']}
        self.bytesIn={'bytes_in':data['bytes_in']}
        self.pktsIn={'pkts_in':data['num_pkts_in']}
        self.pktsOut={'pkts_out':data['num_pkts_out']}
        self.duration={'duration':int(data['time_end']-data['time_start'])}
        self.byteDist={'byte_dist':data['byte_dist']}
        self.byteDistMean={'byte_dist_mean':data['byte_dist_mean']}
        self.byteDistStd={'byte_dist_std':data['byte_dist_std']}
        self.entropy={'entropy':data['entropy']}
        self.entropyTotal={'entropy_total':data['total_entropy']}
        self.packets=data['packets']
        self.packetsLength=[]
        self.packetsTime=[]


    def getPortInfor(self):
        srcPort=0
        dstPort=0
        if(self.srcPort<commonTlsSrcPorts[0]):
            srcPort=1
        for port in commonTlsDstPorts:
            if(self.dstPort==port):
                dstPort=1
        return {'low_src_port':srcPort},{'tls_dst_port':dstPort}

    def getBytesInfor(self):
        return self.bytesIn,self.bytesOut,self.byteDist,self.byteDistMean,self.byteDistStd

    def getPktsInfor(self):
        packetsLengthNew={key:0 for key in pktLengths}
        packetsTimeNew={key:0 for key in pktTimes}
        packetsLengthArray=[]

        for packets in self.packets:
            self.packetsLength.append(packets['b'])
            self.packetsTime.append(packets['ipt'])

        self.packetsLength=calcRandomMatrix(self.packetsLength)
        self.packetsTime=calcRandomMatrix(self.packetsTime)

        packetsLengthArray=[int(value) for line in self.packetsLength for value in line]
        packetsTimeArray=[int(value) for line in self.packetsTime for value in line]

        flag=0
        for key in packetsLengthNew.keys():
            packetsLengthNew.update({key:packetsLengthArray[flag]})
            flag+=1

        flag=0
        for key in packetsTimeNew.keys():
            packetsTimeNew.update({key:packetsTimeArray[flag]})
            flag+=1

        return self.pktsIn,self.pktsOut,self.duration,packetsLengthNew,packetsTimeNew

    def getEntropyInfor(self):
        return self.entropy,self.entropyTotal


# tls features
# include getPfAndSg,getExt,getCs
class tlsFeature(object):
    def __init__(self,tls):
        self.cs=tls['cs']
        self.cext=tls['c_extensions']
        self.nbExt=0
        self.pf=[]
        self.sg=[]

    # get ec_point_formats and supported_groups informations
    def getPfAndSg(self):
        for exts in self.cext:
            if exts.get('ec_point_formats'):
                self.pf=exts['ec_point_formats']
            if exts.get('supported_groups'):
                self.sg=exts['supported_groups']    
        sgNew={'sg_'+str(int(key,16)):0 for key,value in supportGroups.items()}
        flag=0
        while(flag<len(self.sg)):
            if ('sg_'+str(int(self.sg[flag:flag+4],16)) in sgNew):
                sgNew.update({'sg_'+str(int(self.sg[flag:flag+4],16)):1})
            flag+=4
        flag=2
        pfNew={value:0 for key,value in ec_point_formats.items()}
        while(flag<len(self.sg)):
            if(self.pf[flag:flag+2] in ec_point_formats ):
                pfNew.update({ec_point_formats[self.pf[flag:flag+2]]:1})       
            flag+=2
        return pfNew,sgNew

    # get c_extension informations
    def getExt(self):
        extNew = {value:0 for key,value in extDict.items()}
        for extKeys in extDict.keys():
            for exts in self.cext:
                if (extKeys in exts):
                    extNew.update({extDict[extKeys]:1})
                    self.nbExt+=1
        return extNew,{'nb_ext':self.nbExt}

    # get cs informations
    def getCs(self):
        csNew={key:0 for key in csList}
        csVersion=[]
        for cs in self.cs:
            csVersion.append('cs_'+cs)
        for cs in csVersion:
            if(cs in csNew):
                csNew.update({cs:1})
        return csNew

        
class certFeature(object):
    def __init__(self,tls):
        self.cKeyLength={'key_length':tls['c_key_length']}
        self.sCert=tls['s_cert'][0]      
        self.cExt=self.sCert['extensions']
        self.startDate=self.sCert['validity_not_before']
        self.endDate=self.sCert['validity_not_after']
        self.nbSan=0
        self.validity=0
        self.selfSigned={}
        self.date={'date':str(date)[:10]}

    def isSelfSigned(self):
        if self.sCert['issuer']==self.sCert['subject']:
            return {'self-signed':1}
        return {'self-signed':0}

    def getcKeyLength(self):
        return self.cKeyLength

    def getValidity(self):
        smonth=str(months[self.startDate[:3]])
        sday=str(int(self.startDate[4:6]))
        syear=self.startDate[16:20]
        sdate=syear+"-"+smonth+"-"+sday
        self.startDate=datetime.datetime.strptime(sdate,"%Y-%m-%d")
        emonth=str(months[self.endDate[:3]])
        eday=str(int(self.endDate[4:6]))
        eyear=self.endDate[16:20]
        edate=eyear+"-"+emonth+"-"+eday        
        self.endDate=datetime.datetime.strptime(edate,"%Y-%m-%d")
        self.validity=(self.endDate-self.startDate).days
        return {'validity':self.validity}
    
    def getSan(self):
        san={}
        for items in self.cExt:
            if items.get('X509v3 Subject Alternative Name'):
                san=items
        self.nbSan=str(san.values()).count(',')+1
        return {'nb_san':self.nbSan}

    def getDate(self):
        return self.date

defaultFamily={'normal':1,'win_normal':2,'vawtrak':3,'miuref':4,'dridex':5,'locky':6,'zeus':7,'trickbot':8}

# CODE A
def codeA():
    startTime = datetime.datetime.now()
    with open("xxxx.json", 'r', encoding='utf-8') as Sf:
        with open("record.json",'w',encoding='utf-8') as Df:
            line=Sf.readline()
            while (line):
                try:
                    dic=demjson.decode(line)
                    tls=dic['tls']
                    if (tls.get('s_cert') and tls.get('cs') and tls.get('c_key_length') and tls['s_cert'][0].get('extensions')):
                        Df.writelines(line)
                    line=Sf.readline()
                except:
                    line=Sf.readline()
                    continue
    endTime = datetime.datetime.now()
    usedTime=(endTime-startTime).seconds
    print("Used:{}s".format(usedTime))

def codeB():
    startTime = datetime.datetime.now()
    with open("good.csv",'r',encoding='utf-8') as tR:
        with open("recordClear.csv",'w',encoding='utf-8',newline='') as trc:
            trReader=csv.DictReader(tR)
            trcWriter=csv.DictWriter(trc,trReader.fieldnames)
            trcWriter.writerow(dict(zip(trReader.fieldnames,trReader.fieldnames)))
            for items in trReader:
                family=items['family']
                items.update({'family':defaultFamily.get(family)})
                trcWriter.writerow(items)
    endTime = datetime.datetime.now()
    usedTime=(endTime-startTime).seconds
    print("Used:{}s".format(usedTime))

import subprocess
def pcap_to_csv(pcap_id):
    subprocess.call(['./joy_static','-x','SelectCommond', pcap_id])
    subprocess.call('./clear.sh')
    codeA()
    startTime = datetime.datetime.now()
    csvDict={header:0 for header in csvHeader}
    source={'source':'stratosphere'}
    family={'family':'normal'}
    label={'label':0}
    flag=0
    tmpcsv="tmpcsv.csv"
    with open("record.json", 'r', encoding='utf-8') as Sf:
        with open('good.csv','w',newline='',encoding='utf-8') as gc:
            writer=csv.writer(gc)
            writer.writerow(csvHeader)
            line=Sf.readline()
            while (line):
            
                dic=demjson.decode(line)
                commonFeas=commonFeature(dic)
                try:
                    tlsFeas=tlsFeature(dic['tls'])
                    certFeas=certFeature(dic['tls'])
                except:
                    line=Sf.readline()
                    continue
                pktsIn,pktsOut,duration,packetsLenths,packetsTimes=commonFeas.getPktsInfor()
                srcPort,dstPort=commonFeas.getPortInfor()
                bytesIn,bytesOut,byteDist,byteDistMean,byteDistStd=commonFeas.getBytesInfor()
                entropy,entropyTotal=commonFeas.getEntropyInfor()

                ext,nbExt=tlsFeas.getExt()
                cs=tlsFeas.getCs()
                pf,sg=tlsFeas.getPfAndSg()
                try:
                    nbSan=certFeas.getSan()
                    selfSigned=certFeas.isSelfSigned()
                    keyLength=certFeas.getcKeyLength()
                    validity=certFeas.getValidity()
                    mydate=certFeas.getDate()
                except:
                    line=Sf.readline()
                    continue
                csvValue=[pktsIn,pktsOut,duration,packetsLenths,packetsTimes,
                                srcPort,dstPort,bytesIn,bytesOut,byteDistMean,
                                byteDistStd,entropy,ext,nbExt,cs,pf,sg,nbSan,
                                selfSigned,keyLength,validity,mydate,source,family,label]
                
                for value in csvValue:
                    csvDict.update(value)
                    #print(csvDict)
             
                #csvframe = pandas.DataFrame(csvDict,index=[0])
                #csvframe.to_csv(tmpcsv,index=False,sep=',')
                writer.writerow(csvDict.values())

                line=Sf.readline()
    endTime = datetime.datetime.now()
    usedTime=(endTime-startTime).seconds
    print("Used:{}s".format(usedTime))
    codeB()
if __name__=="__main__":
    pcap2csv('test.pcap')