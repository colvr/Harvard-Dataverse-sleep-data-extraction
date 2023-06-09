import numpy as np
import os
from datetime import datetime, timedelta, timezone

dataset = '00'
ori_poly_file = './data_original/dataverse_files_00/poly_2017_06_01.txt'
ori_label_file = './data_original/dataverse_files_00/2017_06_01_patient00_scored.txt'
offset = -0.49
data_index0 = 184395
data_index1 = 8401994
label_index0 = 10
label_index1 = 1079
use_300s_epoch_num = 107
assert label_index1 - label_index0 + 1 == use_300s_epoch_num * 10
start_timestamp = datetime(2017, 6, 1, 21, 39, 45, tzinfo=timezone(timedelta(hours=-6))).timestamp()


# 给定开始的时间戳，从ploy文件获取接近的开始数据下标
def get_timestamp_arr():
    if not os.path.exists('./gain_data/' + dataset + '/0Ground truth/poly_timestamp_arr.npy'):
        # 获取ploy文件的时间戳数组
        filename = ori_poly_file
        with open(filename, "r") as file:
            timestamp_arr = []
            for line in file:
                timestamp = float(line.split(' ')[4])
                timestamp_arr.append(timestamp)
        np.save('./gain_data/' + dataset + '/0Ground truth/poly_timestamp_arr', np.array(timestamp_arr))
    # 下面读时间戳数组出来找
    timestamp_arr = np.load('./gain_data/' + dataset + '/0Ground truth/poly_timestamp_arr.npy')
    print('self-finding..')
    # timestamp_to_time(timestamp_arr[data_index0] + offset)
    # 找到需要的两个时间节点后，自动找传感器数据的时间戳
    for index in range(len(timestamp_arr)):
        if timestamp_arr[index] + offset >= start_timestamp:
            data_index0 = index
            data_index1 = index + 300*256*use_300s_epoch_num - 1
            print('start time:', timestamp_to_time(timestamp_arr[data_index0] + offset))
            print('end time:', timestamp_to_time(timestamp_arr[data_index1] + offset))
            print('请与选定的时间范围核对')
            print('data_index0 =', data_index0)
            print('data_index1 =', data_index1)
            print('从第'+str(data_index0)+'项数据到第'+str(data_index1)+'项数据')
            print('实际使用的数据长度是300*'+str(use_300s_epoch_num)+'*256= '+str(300*256*use_300s_epoch_num)+'项')
            break


# 一个将时间戳转换为UTC-6时间的辅助函数
def timestamp_to_time(timestamp: float):
    return datetime.fromtimestamp(timestamp, timezone(timedelta(hours=-6)))


if __name__ == '__main__':
    if not os.path.exists('./gain_data/' + dataset + '/0Ground truth/'):
        os.makedirs('./gain_data/' + dataset + '/0Ground truth/')
    print('Dataset now is ' + dataset)
    get_timestamp_arr()

    print('Running finish!')
