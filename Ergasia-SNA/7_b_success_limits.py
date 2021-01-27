import math
import os
import json
from publicConstants import number_of_classes

success_limits = []

for i in range(number_of_classes - 1):

    print(i)

    with open('./data/predict_preparation/' + str(i) + '_' + str(i + 1) + '.json') as json_file:
        VxV = [{
            'x':e['x'],
            'y':e['y'],
            'GD':e['GD'],
            'CN':e['CN'],
            'JC':e['JC'],
            'A':e['A'],
            'PA':e['PA'],
            'new': e['new']
        } for e in json.load(json_file)]

    total_new = 0
    for ii in VxV:
        if ii['new']:
            total_new = total_new + 1

    percent_new = total_new / len(VxV)

    AR_txt = ['GD', 'CN', 'JC', 'A', 'PA']
    for txt in AR_txt:
        AR = []
        for ii in VxV:
            AR.append(ii[txt])

        AR = sorted(AR, key=lambda k: k)
        index_01 = math.floor(len(AR) * (1 - percent_new * 20))
        AR_01 = AR[index_01]

        success_limits.append({
            'classnum': str(i) + '_' + str(i + 1),
            'similarity': txt,
            'total_new': total_new,
            'percent_new': percent_new,
            'index_01': index_01,
            'AR_01': AR_01
        })

filename = './data/limits.json'
if os.path.exists(filename):
    os.remove(filename)
with open(filename, 'w') as fout:
    json.dump([{
        'classnum': ii['classnum'],
        'similarity': ii['similarity'],
        'total_new': ii['total_new'],
        'percent_new': ii['percent_new'],
        'index_01': ii['index_01'],
        'AR_01': ii['AR_01']
    } for ii in success_limits], fout)
