import numpy as np
import os
from datetime import datetime, timedelta, timezone, time
from matplotlib import pyplot as plt
import sys
from scipy.interpolate import interp1d


# TODO: 每次更改数据集时重新设置参数
# night_idxs = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '11', '12', '14', '15', '16', '17', '18', '19']
dataset_choose = 19

if dataset_choose == 0:
    dataset = '00'
    ori_poly_file = './data_original/dataverse_files_00/poly_2017_06_01.txt'
    ori_label_file = './data_original/dataverse_files_00/2017_06_01_patient00_scored.txt'
    ori_cir_file = './data_original/dataverse_files_00/cir_2017_06_01_19_51_09.txt'
    ori_csi_file = './data_original/dataverse_files_00/csi_2017_06_01__19_50_58.txt'
    radar_offset = -8.33
    csi_offset = -8.33
    poly_offset = -0.49
    poly_data_index0 = 184395
    poly_data_index1 = 8401994
    label_index0 = 10
    label_index1 = 1079
    epoch_num = 10 * 107
    ori_epoch1_start_timestamp = datetime(2017, 6, 1, 21, 35, 15, tzinfo=timezone(timedelta(hours=-6))).timestamp()
elif dataset_choose == 1:
    dataset = '01'
    ori_poly_file = './data_original/dataverse_files_01/poly_2017_06_05.txt'
    ori_label_file = './data_original/dataverse_files_01/2017_06_05_patient01_scored.txt'
    ori_cir_file = './data_original/dataverse_files_01/cir_2017_06_05_19_24_55.txt'
    ori_csi_file = './data_original/dataverse_files_01/csi_2017_06_05__19_24_44.txt'
    radar_offset = -8.91
    csi_offset = -8.91
    poly_offset = -0.32
    poly_data_index0 = 768031
    poly_data_index1 = 8832030
    label_index0 = 90
    label_index1 = 1139
    epoch_num = 10 * 105
    ori_epoch1_start_timestamp = datetime(2017, 6, 5, 20, 51, 23, tzinfo=timezone(timedelta(hours=-6))).timestamp()
elif dataset_choose == 2:
    dataset = '02'
    ori_poly_file = './data_original/dataverse_files_02/poly_2017_06_06.txt'
    ori_label_file = './data_original/dataverse_files_02/2017_06_06_patient02_scored.txt'
    ori_cir_file = './data_original/dataverse_files_02/cir_2017_06_06_19_23_12.txt'
    ori_csi_file = './data_original/dataverse_files_02/csi_2017_06_06__19_23_02.txt'
    radar_offset = -9.07
    poly_offset = -0.09
    poly_data_index0 = 399333
    poly_data_index1 = 8156132
    label_index0 = 33
    label_index1 = 1042
    epoch_num = 10 * 101
    ori_epoch1_start_timestamp = datetime(2017, 6, 6, 21, 33, 46, tzinfo=timezone(timedelta(hours=-6))).timestamp()
elif dataset_choose == 3:
    dataset = '03'
    ori_poly_file = './data_original/dataverse_files_03/poly_2017_06_07.txt'
    ori_label_file = './data_original/dataverse_files_03/2017_06_07_patient03_scored.txt'
    ori_cir_file = './data_original/dataverse_files_03/cir_2017_06_07_19_15_13.txt'
    ori_csi_file = './data_original/dataverse_files_03/csi_2017_06_07__19_15_02.txt'
    radar_offset = -8.93
    poly_offset = -1.18
    poly_data_index0 = 714492
    poly_data_index1 = 7472891
    label_index0 = 60
    label_index1 = 939
    epoch_num = 10 * 88
    ori_epoch1_start_timestamp = datetime(2017, 6, 7, 21, 40, 49, tzinfo=timezone(timedelta(hours=-6))).timestamp()
elif dataset_choose == 4:
    dataset = '04'
    ori_poly_file = './data_original/dataverse_files_04/poly_2017_06_13.txt'
    ori_label_file = './data_original/dataverse_files_04/2017_06_13_patient04_scored.txt'
    ori_cir_file = './data_original/dataverse_files_04/cir_2017_06_13_19_24_38.txt'
    ori_csi_file = './data_original/dataverse_files_04/csi_2017_06_13__19_24_27.txt'
    radar_offset = -9.45
    poly_offset = -0.63
    poly_data_index0 = 1067631
    poly_data_index1 = 8363630
    label_index0 = 107
    label_index1 = 1056
    epoch_num = 10 * 95
    ori_epoch1_start_timestamp = datetime(2017, 6, 13, 21, 23, 26, tzinfo=timezone(timedelta(hours=-6))).timestamp()
elif dataset_choose == 5:
    dataset = '05'
    ori_poly_file = './data_original/dataverse_files_05/poly_2017_06_14.txt'
    ori_label_file = './data_original/dataverse_files_05/2017_06_14_patient05_scored.txt'
    ori_cir_file = './data_original/dataverse_files_05/cir_2017_06_14_19_34_10.txt'
    ori_csi_file = './data_original/dataverse_files_05/csi_2017_06_14__19_34_00.txt'
    radar_offset = -8.77
    poly_offset = -0.41
    poly_data_index0 = 115254
    poly_data_index1 = 7411253
    label_index0 = 4
    label_index1 = 953
    epoch_num = 10 * 95
    ori_epoch1_start_timestamp = datetime(2017, 6, 14, 22, 39, 41, tzinfo=timezone(timedelta(hours=-6))).timestamp()
elif dataset_choose == 6:
    dataset = '06'
    ori_poly_file = './data_original/dataverse_files_06/poly_2017_06_16.txt'
    ori_label_file = './data_original/dataverse_files_06/2017_06_16_patient06_scored.txt'
    ori_cir_file = './data_original/dataverse_files_06/cir_2017_06_16_19_32_15.txt'
    ori_csi_file = './data_original/dataverse_files_06/csi_2017_06_16__19_32_05.txt'
    radar_offset = -9.17
    poly_offset = -0.72
    poly_data_index0 = 176774
    poly_data_index1 = 8087173
    label_index0 = 4
    label_index1 = 1033
    epoch_num = 10 * 103
    ori_epoch1_start_timestamp = datetime(2017, 6, 16, 21, 20, 40, tzinfo=timezone(timedelta(hours=-6))).timestamp()
elif dataset_choose == 7:
    dataset = '07'
    ori_poly_file = './data_original/dataverse_files_07/poly_2017_06_19.txt'
    ori_label_file = './data_original/dataverse_files_07/2017_06_19_patient07_scored.txt'
    ori_cir_file = './data_original/dataverse_files_07/cir_2017_06_19_19_31_45.txt'
    ori_csi_file = './data_original/dataverse_files_07/csi_2017_06_19__19_31_29.txt'
    radar_offset = -9.54
    poly_offset = 0.92
    poly_data_index0 = 690914
    poly_data_index1 = 8063713
    label_index0 = 51
    label_index1 = 1010
    epoch_num = 10 * 96
    ori_epoch1_start_timestamp = datetime(2017, 6, 19, 21, 41, 48, tzinfo=timezone(timedelta(hours=-6))).timestamp()
elif dataset_choose == 8:
    dataset = '08'
    ori_poly_file = './data_original/dataverse_files_08/poly_2017_06_20.txt'
    ori_label_file = './data_original/dataverse_files_08/2017_06_20_patient08_scored.txt'
    ori_cir_file = './data_original/dataverse_files_08/cir_2017_06_20_19_33_23.txt'
    ori_csi_file = './data_original/dataverse_files_08/csi_2017_06_20__19_33_07.txt'
    radar_offset = -8.84
    poly_offset = 0.22
    poly_data_index0 = 806293
    poly_data_index1 = 7103892
    label_index0 = 87
    label_index1 = 906
    epoch_num = 10 * 82
    ori_epoch1_start_timestamp = datetime(2017, 6, 20, 22, 9, 3, tzinfo=timezone(timedelta(hours=-6))).timestamp()
elif dataset_choose == 9:
    dataset = '09'
    ori_poly_file = './data_original/dataverse_files_09/poly_2017_06_21.txt'
    ori_label_file = './data_original/dataverse_files_09/2017_06_21_patient09_scored.txt'
    ori_cir_file = './data_original/dataverse_files_09/cir_2017_06_21_19_36_42.txt'
    ori_csi_file = './data_original/dataverse_files_09/csi_2017_06_21__19_36_26.txt'
    radar_offset = -9.12
    poly_offset = -0.79
    poly_data_index0 = 368792
    poly_data_index1 = 6435991
    label_index0 = 35
    label_index1 = 824
    epoch_num = 10 * 79
    ori_epoch1_start_timestamp = datetime(2017, 6, 21, 22, 14, 33, tzinfo=timezone(timedelta(hours=-6))).timestamp()
# elif dataset_choose == 10:
#     dataset = '10'
#     ori_poly_file = './data_original/dataverse_files_10/poly_2017_06_22.txt'
#     ori_label_file = './data_original/dataverse_files_10/2017_06_22_patient10_scored.txt'
#     ori_cir_file = './data_original/dataverse_files_10/.txt'
#     radar_offset = -8.84
#     poly_offset = -0.4
#     poly_data_index0 = 253492
#     poly_data_index1 = 8087091
#     label_index0 = 21
#     label_index1 = 1040
#     epoch_num = 10 * 102
#     ori_epoch1_start_timestamp = datetime(2017, 6, 22, 21, 18, 49, tzinfo=timezone(timedelta(hours=-6))).timestamp()
elif dataset_choose == 11:
    dataset = '11'
    ori_poly_file = './data_original/dataverse_files_11/poly_2017_06_26.txt'
    ori_label_file = './data_original/dataverse_files_11/2017_06_26_patient11_scored.txt'
    ori_cir_file = './data_original/dataverse_files_11/cir_2017_06_26_19_25_13.txt'
    ori_csi_file = './data_original/dataverse_files_11/csi_2017_06_26__19_24_57.txt'
    radar_offset = -9.56
    poly_offset = 1.49
    poly_data_index0 = 905808
    poly_data_index1 = 7971407
    label_index0 = 25
    label_index1 = 944
    epoch_num = 10 * 92
    ori_epoch1_start_timestamp = datetime(2017, 6, 26, 22, 15, 0, tzinfo=timezone(timedelta(hours=-6))).timestamp()
elif dataset_choose == 12:
    dataset = '12'
    ori_poly_file = './data_original/dataverse_files_12/poly_2017_06_27.txt'
    ori_label_file = './data_original/dataverse_files_12/2017_06_27_patient12_scored.txt'
    ori_cir_file = './data_original/dataverse_files_12/cir_2017_06_27_19_30_03.txt'
    ori_csi_file = './data_original/dataverse_files_12/csi_2017_06_27__19_29_47.txt'
    radar_offset = -9.43
    poly_offset = 0.86
    poly_data_index0 = 199409
    poly_data_index1 = 6650608
    label_index0 = 9
    label_index1 = 848
    epoch_num = 10 * 84
    ori_epoch1_start_timestamp = datetime(2017, 6, 27, 21, 23, 30, tzinfo=timezone(timedelta(hours=-6))).timestamp()
elif dataset_choose == 14:
    dataset = '14'
    ori_poly_file = './data_original/dataverse_files_14/poly_2017_06_29.txt'
    ori_label_file = './data_original/dataverse_files_14/2017_06_29_patient14_scored.txt'
    ori_cir_file = './data_original/dataverse_files_14/cir_2017_06_29_19_27_37.txt'
    ori_csi_file = './data_original/dataverse_files_14/csi_2017_06_29__19_27_21.txt'
    radar_offset = -9.01
    poly_offset = -1.02
    poly_data_index0 = 537811
    poly_data_index1 = 5990610
    label_index0 = 56
    label_index1 = 765
    epoch_num = 10 * 71
    ori_epoch1_start_timestamp = datetime(2017, 6, 29, 22, 34, 53, tzinfo=timezone(timedelta(hours=-6))).timestamp()
elif dataset_choose == 15:
    dataset = '15'
    ori_poly_file = './data_original/dataverse_files_15/poly_2017_06_30.txt'
    ori_label_file = './data_original/dataverse_files_15/2017_06_30_patient15_scored.txt'
    ori_cir_file = './data_original/dataverse_files_15/cir_2017_06_30_20_22_44.txt'
    ori_csi_file = './data_original/dataverse_files_15/csi_2017_06_30__20_22_29.txt'
    radar_offset = -9.09
    poly_offset = 0.31
    poly_data_index0 = 314750
    poly_data_index1 = 7764349
    label_index0 = 16
    label_index1 = 985
    epoch_num = 10 * 97
    ori_epoch1_start_timestamp = datetime(2017, 6, 30, 22, 18, 4, tzinfo=timezone(timedelta(hours=-6))).timestamp()
elif dataset_choose == 16:
    dataset = '16'
    ori_poly_file = './data_original/dataverse_files_16/poly_2017_07_06.txt'
    ori_label_file = './data_original/dataverse_files_16/2017_07_06_patient16_scored.txt'
    ori_cir_file = './data_original/dataverse_files_16/cir_2017_07_06_19_35_48.txt'
    ori_csi_file = './data_original/dataverse_files_16/csi_2017_07_06__19_35_32.txt'
    radar_offset = -9.77
    poly_offset = 0.37
    poly_data_index0 = 61295
    poly_data_index1 = 6742894
    label_index0 = 1
    label_index1 = 870
    epoch_num = 10 * 87
    ori_epoch1_start_timestamp = datetime(2017, 7, 6, 23, 9, 48, tzinfo=timezone(timedelta(hours=-6))).timestamp()
elif dataset_choose == 17:
    dataset = '17'
    ori_poly_file = './data_original/dataverse_files_17/poly_2017_07_10.txt'
    ori_label_file = './data_original/dataverse_files_17/2017_07_10_patient17_scored.txt'
    ori_cir_file = './data_original/dataverse_files_17/cir_2017_07_10_19_31_54.txt'
    ori_csi_file = './data_original/dataverse_files_17/csi_2017_07_10__19_31_38.txt'
    radar_offset = -9.84
    poly_offset = 1.61
    poly_data_index0 = 1835057
    poly_data_index1 = 8593456
    label_index0 = 215
    label_index1 = 1094
    epoch_num = 10 * 88
    ori_epoch1_start_timestamp = datetime(2017, 7, 10, 21, 14, 35, tzinfo=timezone(timedelta(hours=-6))).timestamp()
elif dataset_choose == 18:
    dataset = '18'
    ori_poly_file = './data_original/dataverse_files_18/poly_2017_07_11.txt'
    ori_label_file = './data_original/dataverse_files_18/2017_07_11_patient18_scored.txt'
    ori_cir_file = './data_original/dataverse_files_18/cir_2017_07_11_20_03_26.txt'
    ori_csi_file = './data_original/dataverse_files_18/csi_2017_07_11__20_03_11.txt'
    radar_offset = -10.16
    poly_offset = 1.07
    poly_data_index0 = 3263676
    poly_data_index1 = 9868475
    label_index0 = 192
    label_index1 = 1051
    epoch_num = 10 * 86
    ori_epoch1_start_timestamp = datetime(2017, 7, 11, 22, 53, 33, tzinfo=timezone(timedelta(hours=-6))).timestamp()
elif dataset_choose == 19:
    dataset = '19'
    ori_poly_file = './data_original/dataverse_files_19/poly_2017_07_12.txt'
    ori_label_file = './data_original/dataverse_files_19/2017_07_12_patient19_scored.txt'
    ori_cir_file = './data_original/dataverse_files_19/cir_2017_07_12_19_03_08.txt'
    ori_csi_file = './data_original/dataverse_files_19/csi_2017_07_12__19_02_53.txt'
    radar_offset = -10.24
    poly_offset = 0.29
    poly_data_index0 = 1528195
    poly_data_index1 = 8286594
    label_index0 = 65
    label_index1 = 944
    epoch_num = 10 * 88
    ori_epoch1_start_timestamp = datetime(2017, 7, 12, 22, 3, 21, tzinfo=timezone(timedelta(hours=-6))).timestamp()
else:
    print('数据集选择有误')
    sys.exit(0)

# TODO: 更改传感器要改的参数
# CR\AR\TC\NC 分别对应胸部，腹部，热电偶，鼻套管传感器

# 一些验证，防止出错
sensor_data_length = epoch_num * 30 * 256
assert poly_data_index1 - poly_data_index0 + 1 == sensor_data_length
assert label_index1 - label_index0 + 1 == epoch_num

sensor = 'nothing'
sensor = 'nothing'


# 获得睡眠障碍相关的label，指定时间范围内的
# 考虑了呼吸暂停(阻塞性、中枢性，混合型归为阻塞型)，不考虑低通气，对于一个epoch，当呼吸暂停超过5s则对该epoch进行标注
def get_sleep_disorders_label_used():
    if not os.path.exists('./gain_data/' + dataset + '/0Ground truth/ori_sleep_disorders_label_used.npy'):
        disorders_to_num = {'Nothing': 0, 'Obstructive Apnea\n': 1, 'Central Apnea\n': 2, 'Mixed Apnea\n': 1}
        # 最后存在这个数组中所有的睡眠障碍label
        disorders_label_arr = [0 for _ in range(epoch_num)]
        filename = ori_label_file

        with open(filename, "r") as file:
            line_count = 0
            for line in file:
                line_count += 1
                if line_count >= 7:
                    line = line.split('\t')
                    line_epoch = line[1]
                    line_duration = line[-2]
                    line_title = line[-1]
                    if line_epoch and line_duration and line_title:
                        # 表示开始有了epoch记录，则对应应该也有duration记录，以及title记录
                        # if ('Hypopnea' in line_title or 'Apnea' in line_title) and '.' not in line_title:
                        if line_title in disorders_to_num:
                            # 该行为需要考虑的睡眠障碍类型，获取其发生的开始epoch，持续时间，以及对应的label数字，以及当前epoch开始的时间
                            line_duration = 60 * int(line_duration.split(':')[0]) + float(line_duration.split(':')[1])
                            # 这个值应该没超过一分钟
                            assert line_duration < 60
                            line_epoch = int(line_epoch)
                            if line_epoch - label_index0 >= epoch_num  or line_epoch - label_index0 < 0:
                                break
                            new_num = disorders_to_num[line_title]
                            # 关于该呼吸障碍事件时间的处理
                            this_epoch_start_timestamp = ori_epoch1_start_timestamp + (line_epoch - 1) * 30
                            this_epoch_start_time = timestamp_to_time(this_epoch_start_timestamp).time()
                            event_start_time = time.fromisoformat(line[0].rstrip())
                            hour_diff = -1
                            # 如果当前事件开始的时间比当前epoch开始的时间还小，说明是跨24点了，处理下
                            if event_start_time < this_epoch_start_time:
                                assert event_start_time.hour == 0
                                assert this_epoch_start_time.hour == 23
                                hour_diff = 1
                            if hour_diff == 1:
                                event_start_past_time = hour_diff * 60 * 60 \
                                                        + (event_start_time.minute - this_epoch_start_time.minute) * 60 \
                                                        + (event_start_time.second - this_epoch_start_time.second)
                            else:
                                event_start_past_time = (event_start_time.hour - this_epoch_start_time.hour) * 60 * 60 \
                                                        + (event_start_time.minute - this_epoch_start_time.minute) * 60 \
                                                        + (event_start_time.second - this_epoch_start_time.second)
                            # =30的情况是这个事件开始时其实已经是下个epoch了
                            assert 0 <= event_start_past_time <= 30
                            this_epoch_leave_time = 30 - event_start_past_time
                            # 定义一个残存的睡眠障碍持续时间，用于跨epoch的
                            leave_disorders_time = line_duration - this_epoch_leave_time
                            if this_epoch_leave_time >= 5 and line_duration >= 5:

                                if disorders_label_arr[line_epoch - label_index0] == 0 or disorders_label_arr[line_epoch - label_index0] == new_num:
                                    # assert disorders_label_arr[line_epoch - label_index0] == 0 or disorders_label_arr[line_epoch - label_index0] == new_num
                                    disorders_label_arr[line_epoch - label_index0] = new_num
                                else:
                                    # 中枢性和阻塞性呼吸暂停在同一个epoch出现，也算阻塞性呼吸暂停
                                    disorders_label_arr[line_epoch - label_index0] = 1
                            while leave_disorders_time >= 5:
                                line_epoch += 1
                                assert disorders_label_arr[line_epoch - label_index0] == 0 or disorders_label_arr[line_epoch - label_index0] == new_num
                                disorders_label_arr[line_epoch - label_index0] = new_num
                                leave_disorders_time -= 30
        np.save('./gain_data/' + dataset + '/0Ground truth/ori_sleep_disorders_label_used', disorders_label_arr)
        print('获取原始sleep disorders label完成')
    else:
        print('原始sleep disorders label文件已存在')


# 5分类睡眠障碍label，另外这里对应的epoch采用滑窗方法，60秒滑窗大小，使用2s滑窗步长,label打分依据是当前滑窗中间的30s时刻是处于什么事件中。
def get_5_sleep_disorders_label_used_60s_slide_epoch():
    result_filename = 'ori_5_sleep_disorders_label_used_60s_slide_epoch.npy'
    if not os.path.exists('./gain_data/' + dataset + '/0Ground truth/' + result_filename):
        disorders_to_num = {'Nothing': 0, 'Obstructive Apnea': 1, 'Central Apnea': 2, 'Mixed Apnea': 3, 'Obstructive Hypopnea': 4}
        # 最后存在这个数组中所有的睡眠障碍label，由于是60s滑窗大小，2s步长，因此epoch数量
        t = epoch_num * 30
        slide_epoch_num = (t - 60) // 2 + 1
        slide_disorders_label_arr = [0 for _ in range(slide_epoch_num)]

        # 下面根据ori_sleep_disorders_event_used.npy里已经获取的[事件开始时间、持续时间、事件类型]，对滑窗进行label赋值
        disorders_event_arr = np.load('./gain_data/' + dataset + '/0Ground truth/ori_sleep_disorders_event_used.npy')
        for disorders_event in disorders_event_arr:
            # 对于每个事件进行遍历，使其影响其应该影响的 slide epoch
            event_start_time = int(disorders_event[0])
            event_end_time = event_start_time + int(float(disorders_event[1]))
            effect_count = 0
            for t in range(event_start_time, event_end_time + 1):
                if t % 2 == 0 and t >= 30:
                    # 每个t时刻作为中心对应的滑窗编号是 (t-30)//2 ，需要t是偶数
                    window_number = (t - 30) // 2
                    if window_number < slide_epoch_num:
                        slide_disorders_label_arr[window_number] = disorders_to_num[disorders_event[2]]
                        effect_count += 1
            # print(disorders_event[1], effect_count)
        np.save('./gain_data/' + dataset + '/0Ground truth/' + result_filename, slide_disorders_label_arr)
        print('获取'+result_filename+'完成')
    else:
        print(result_filename + '文件已存在')


# 这个函数获取指定时间范围内睡眠障碍的事件的[事件开始时间、持续时间、事件类型]，相比前面处理过的epoch标注，这是更加原始的数据，事件类型就用字符串保存了
def get_sleep_disorders_event_used():
    if not os.path.exists('./gain_data/' + dataset + '/0Ground truth/ori_sleep_disorders_event_used.npy'):
        disorders_to_str = {'Obstructive Apnea\n': 'Obstructive Apnea', 'Central Apnea\n': 'Central Apnea',
                            'Mixed Apnea\n': 'Mixed Apnea', 'Obstructive Hypopnea\n': 'Obstructive Hypopnea', }
        # 最后存在这个数组中所有的睡眠障碍事件
        disorders_event_arr = []
        filename = ori_label_file
        label_index0_epoch_start_timestamp = ori_epoch1_start_timestamp + (label_index0 - 1) * 30
        label_index0_epoch_start_time = timestamp_to_time(label_index0_epoch_start_timestamp).time()

        with open(filename, "r") as file:
            line_count = 0
            for line in file:
                line_count += 1
                if line_count >= 7:
                    line = line.split('\t')
                    line_epoch = line[1]
                    line_duration = line[-2]
                    line_title = line[-1]
                    if line_epoch and line_duration and line_title:
                        # 表示开始有了epoch记录，则对应应该也有duration记录，以及title记录
                        # if ('Hypopnea' in line_title or 'Apnea' in line_title) and '.' not in line_title:
                        if line_title in disorders_to_str:
                            # 该行为需要考虑的睡眠障碍类型，获取其发生的开始epoch，持续时间，以及对应的label数字，以及当前epoch开始的时间
                            line_duration = 60 * int(line_duration.split(':')[0]) + float(line_duration.split(':')[1])
                            # 这个值应该没超过一分钟
                            assert line_duration < 80
                            line_epoch = int(line_epoch)
                            if line_epoch - label_index0 >= epoch_num:
                                break
                            if line_epoch - label_index0 < 0:
                                continue
                            new_str = disorders_to_str[line_title]
                            # 关于该呼吸障碍事件时间的处理
                            event_start_time = time.fromisoformat(line[0].rstrip())
                            day_diff = -1
                            # 如果当前事件开始的时间比label index0 epoch开始的时间还小，说明是跨24点了，处理下
                            if event_start_time < label_index0_epoch_start_time:
                                day_diff = 1
                            if day_diff == 1:
                                event_start_past_time = (24 + event_start_time.hour - label_index0_epoch_start_time.hour) * 60 * 60 \
                                                        + (event_start_time.minute - label_index0_epoch_start_time.minute) * 60 \
                                                        + (event_start_time.second - label_index0_epoch_start_time.second)
                            else:
                                event_start_past_time = (event_start_time.hour - label_index0_epoch_start_time.hour) * 60 * 60 \
                                                        + (event_start_time.minute - label_index0_epoch_start_time.minute) * 60 \
                                                        + (event_start_time.second - label_index0_epoch_start_time.second)
                            # 记录事件
                            disorders_event_arr.append([event_start_past_time, line_duration, new_str])
        disorders_event_arr = np.array(disorders_event_arr)
        np.save('./gain_data/' + dataset + '/0Ground truth/ori_sleep_disorders_event_used', disorders_event_arr)
        print('获取原始sleep disorders event完成')
    else:
        print('原始sleep disorders event文件已存在')


# 获取指定数据区间的cir数据
def get_cir_used():
    if not os.path.exists('./gain_data/' + dataset + '/0Ground truth/cir_used.npy'):
        timestamp_arr = []
        cir_used = []
        timestamp_used = []
        start_timestamp = ori_epoch1_start_timestamp + 30 * (label_index0 - 1)
        end_timestamp = ori_epoch1_start_timestamp + 30 * label_index1
        assert end_timestamp - start_timestamp == 30 * epoch_num
        with open(ori_cir_file, "r") as file:
            for line in file:
                content = line.split(' ')
                timestamp = float(content[-1]) + radar_offset
                timestamp_arr.append(timestamp)
                if start_timestamp <= timestamp <= end_timestamp:
                    cir_used.append(list(map(int, content[:40])))
                    timestamp_used.append(timestamp)
        # 至少大约用了一半的数据吧
        assert 1 < len(timestamp_arr) / len(timestamp_used) < 2
        assert timestamp_arr[0] <= start_timestamp < end_timestamp <= timestamp_arr[-1]
        # timestamp_diff = np.diff(np.array(timestamp_used))
        # 对数据做线性插值，插值到确定采样率18.9Hz
        assert len(timestamp_used) == len(cir_used)
        timestamp_used = np.array(timestamp_used)
        cir_used = np.array(cir_used)
        len_after_interp = round((end_timestamp-start_timestamp)*18.9)
        assert len_after_interp % 10 == 0
        print('原数据长度:', len(timestamp_used), '插值后长度:', len_after_interp)

        # 插入点为xvals
        xvals = np.linspace(start_timestamp, end_timestamp, len_after_interp)
        cir_after_interp = []
        for col in range(40):
            cir_interp = np.interp(xvals, timestamp_used, cir_used[:, col])
            cir_after_interp.append(cir_interp)
        cir_after_interp = np.array(cir_after_interp)
        assert cir_after_interp.shape == (40, len_after_interp)

        np.save('./gain_data/' + dataset + '/0Ground truth/cir_used', cir_after_interp)

        print('获取指定区间的cir数据完成')


# 获取指定数据区间的CSI数据
def get_csi_used():
    if not os.path.exists('./gain_data/' + dataset + '/0Ground truth/csi_used.npy'):
        timestamp_arr = []
        csi_used = []
        timestamp_used = []
        start_timestamp = ori_epoch1_start_timestamp + 30 * (label_index0 - 1)
        end_timestamp = ori_epoch1_start_timestamp + 30 * label_index1
        assert end_timestamp - start_timestamp == 30 * epoch_num
        with open(ori_csi_file, "r") as file:
            for line in file:
                content = line.split(' ')
                assert len(content) == 114 * 8 + 1 + 14
                timestamp = float(content[-1]) + radar_offset
                timestamp_arr.append(timestamp)
                if start_timestamp <= timestamp <= end_timestamp:
                    csi_used.append(list(map(int, content[14: -1])))
                    timestamp_used.append(timestamp)
        # 至少大约用了一半的数据吧
        assert 1 < len(timestamp_arr) / len(timestamp_used) < 2
        assert timestamp_arr[0] <= start_timestamp < end_timestamp <= timestamp_arr[-1]
        # timestamp_diff = np.diff(np.array(timestamp_used))
        # 对数据做三次条样插值，插值到确定采样率9.9Hz
        assert len(timestamp_used) == len(csi_used)
        timestamp_used = np.array(timestamp_used)
        csi_used = np.array(csi_used)
        len_after_interp = round((end_timestamp-start_timestamp)*9.9)
        assert len_after_interp % 10 == 0
        print('原数据长度:', len(timestamp_used), '插值后长度:', len_after_interp)

        # # 随便可视化下中间段
        # fig, ax = plt.subplots(figsize=(6.5, 4))
        # ax.plot(timestamp_used[20000:20300], csi_used[20000:20300, 0], label='data')
        # plt.show()

        # 插入点为xvals
        xvals = np.linspace(start_timestamp, end_timestamp, len_after_interp)
        csi_after_interp = []
        for col in range(114 * 8):
            csi_interp = np.interp(xvals, timestamp_used, csi_used[:, col])
            csi_after_interp.append(csi_interp)
        csi_after_interp = np.array(csi_after_interp)
        assert csi_after_interp.shape == (8*114, len_after_interp)

        np.save('./gain_data/' + dataset + '/0Ground truth/csi_used', csi_after_interp)

        print('获取指定区间的csi数据完成')


# 获取原始scored标注文件中的睡眠阶段
def get_ori_sleep_stage_label():
    if not os.path.exists('./gain_data/' + dataset + '/0Ground truth/ori_sleep_stage_label.npy'):
        stage_to_num = {'U': -1, 'W': 0, 'N1': 1, 'N2': 2, 'N3': 3, 'R': 4}
        arr = [0]  # 默认第0epoch为清醒W
        last_epoch = 0
        last_stage_num = 0
        filename = ori_label_file
        with open(filename, "r") as file:
            line_count = 0
            for line in file:
                line_count += 1
                if line_count >= 7:
                    line = line.split('\t')
                    line_epoch = line[1]
                    line_stage = line[2]
                    if line_epoch:
                        # 表示开始有了epoch记录，则对应应该也有stage记录
                        assert line_stage
                        new_epoch = int(line_epoch)
                        new_num = stage_to_num[line_stage]
                        if new_epoch == last_epoch:
                            continue
                        ex_arr = [last_stage_num] * (new_epoch - last_epoch)
                        ex_arr[-1] = new_num
                        arr = arr + ex_arr
                        last_epoch = new_epoch
                        last_stage_num = new_num

        np.save('./gain_data/' + dataset + '/0Ground truth/ori_sleep_stage_label', arr)
        print('获取原始sleep stage label完成')
    else:
        print('原始sleep stage label文件已存在')


# 截取一段指定区间的睡眠阶段label
def get_sleep_stage_label_used():
    ori_arr = np.load('./gain_data/' + dataset + '/0Ground truth/ori_sleep_stage_label.npy')
    label_arr = ori_arr[label_index0:label_index1 + 1]
    np.save('./gain_data/' + dataset + '/0Ground truth/sleep_stage_label_used', label_arr)
    print('获得指定区间的睡眠阶段label完成')


# 获得原始完整的呼吸传感器数据array
def get_sensor_data_arr():
    filename = ori_poly_file
    sensors_to_col = {'CR': 0, 'AR': 1, 'TC': 2, 'NC': 3}
    with open(filename, "r") as file:
        sensors_data_arr = []
        for line in file:
            # 这里的呼吸传感器记录采样率是256hz
            sensors_data_now = float(line.split(' ')[sensors_to_col[sensor]])
            sensors_data_arr.append(sensors_data_now)

        # print('数组长度： ', len(sensors_data_arr))
        fin_arr = np.array(sensors_data_arr)
        np.save('./gain_data/' + dataset + '/0Ground truth/' + sensor + '/' + sensor + '_arr', fin_arr)


# 一个将时间戳转换为UTC-6时间的辅助函数
def timestamp_to_time(timestamp: float):
    return datetime.fromtimestamp(timestamp, timezone(timedelta(hours=-6)))


# 将呼吸传感器数据从中间截取epoch需要的那一段array
def get_the_middle_section_data():
    arr = np.load('./gain_data/' + dataset + '/0Ground truth/' + sensor + '/' + sensor + '_arr.npy')
    new_arr = arr[poly_data_index0:poly_data_index1 + 1]
    assert len(new_arr) == sensor_data_length
    np.save('./gain_data/' + dataset + '/0Ground truth/' + sensor + '/' + sensor + '_arr_middle_section', new_arr)


# 可视化选取的中间段数据看看数据长什么样
def visualize_data():
    arr = np.load('./gain_data/' + dataset + '/0Ground truth/' + sensor + '/' + sensor + '_arr_middle_section.npy')
    save_path = './gain_data/' + dataset + '/0Ground truth/' + sensor + '/' + sensor + '_arr_middle_section_pic'
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    len_of_one_epoch = 30 * 256
    num_of_epoch = epoch_num
    assert num_of_epoch * len_of_one_epoch == len(arr)
    for epoch in range(num_of_epoch):
        now = arr[epoch * len_of_one_epoch:epoch * len_of_one_epoch + len_of_one_epoch]
        plt.plot([1 / 256 * i for i in range(len_of_one_epoch)], now, '-')
        plt.title(sensor + ' data pic' + ', epoch ' + str(epoch))
        plt.xlabel('Time(second)')
        plt.xlim((0, 30))
        plt.savefig(save_path + '/epoch ' + str(epoch) + '.jpg')
        # plt.show()
        plt.cla()
    # 另外使用np.percentile()做数据范围分析
    per_list = [0, 2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 98, 100]
    print('数据范围分析（精确到整数）：')
    for per in per_list:
        print(str(per) + '%: ' + str(int(np.percentile(arr, per))))


# 将中间那一段array的一些异常值截断处理
def clip_the_middle_section_data():
    arr = np.load('./gain_data/' + dataset + '/0Ground truth/' + sensor + '/' + sensor + '_arr_middle_section.npy')
    # print(np.percentile(arr, 1))
    res_arr = np.clip(arr, np.percentile(arr, 2), np.percentile(arr, 98))
    np.save('./gain_data/' + dataset + '/0Ground truth/' + sensor + '/' + sensor + '_arr_middle_section_clip',
            res_arr)
    print('获得截断处理的去除异常值的传感器数据完成')


# 可视化选取的中间段数据截断后的图像
def visualize_clip_data():
    arr = np.load(
        './gain_data/' + dataset + '/0Ground truth/' + sensor + '/' + sensor + '_arr_middle_section_clip.npy')
    save_path = './gain_data/' + dataset + '/0Ground truth/' + sensor + '/' + sensor + '_arr_middle_section_clip_pic'
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    len_of_one_epoch = 30 * 256
    num_of_epoch = epoch_num
    assert num_of_epoch * len_of_one_epoch == len(arr)
    for epoch in range(num_of_epoch):
        now = arr[epoch * len_of_one_epoch:epoch * len_of_one_epoch + len_of_one_epoch]
        plt.plot([1 / 256 * i for i in range(len_of_one_epoch)], now, '-')
        plt.title(sensor + ' data pic' + ', epoch ' + str(epoch))
        plt.xlabel('Time(second)')
        plt.xlim((0, 30))
        plt.savefig(save_path + '/epoch ' + str(epoch) + '.jpg')
        # plt.show()
        plt.cla()


if __name__ == '__main__':
    print('Dataset now is ' + dataset)
    if not os.path.exists('./gain_data/' + dataset + '/0Ground truth'):
        os.makedirs('./gain_data/' + dataset + '/0Ground truth')
    # # 1. 对每个数据集要跑的函数
    # get_ori_sleep_stage_label()
    # get_sleep_stage_label_used()
    # # 以及获取到指定epoch范围内的cir数据
    # get_cir_used()
    # 获取到指定epoch范围内的CSI数据
    get_csi_used()
    # # 获取睡眠障碍相关的label
    # get_sleep_disorders_label_used()
    # get_sleep_disorders_event_used()
    # get_5_sleep_disorders_label_used_60s_slide_epoch()
    #
    # # 2. 对每个传感器要跑的函数
    # sensor_list = ['CR', 'AR', 'TC', 'NC']
    # for sensor in sensor_list:
    #     if not os.path.exists('./gain_data/' + dataset + '/0Ground truth/' + sensor):
    #         os.makedirs('./gain_data/' + dataset + '/0Ground truth/' + sensor)
    #     print('Sensor now is ' + sensor)
    #     get_sensor_data_arr()
    #     get_the_middle_section_data()
    #     clip_the_middle_section_data()
    # #     # visualize_clip_data()

    print('Running finish!')
