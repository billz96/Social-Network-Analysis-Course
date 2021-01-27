import os
import json
from publicConstants import number_of_classes

with open('./data/limits.json') as json_file:
    limits = [{
        'classnum': e['classnum'],
        'similarity': e['similarity'],
        'AR_01': e['AR_01']
    } for e in json.load(json_file)]

# number_of_classes = 2

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
            'new': e['new'],
            'new_GD': False,
            'new_CN': False,
            'new_JC': False,
            'new_A': False,
            'new_PA': False
        } for e in json.load(json_file)]

    counter = 0
    GD_Lim = 0
    CN_Lim = 0
    JC_Lim = 0
    A_Lim = 0
    PA_Lim = 0
    for ii in limits:
        if ii['classnum'] == str(i) + '_' + str(i + 1):
            if ii['similarity'] == 'GD': GD_Lim = ii['AR_01']
            if ii['similarity'] == 'CN': CN_Lim = ii['AR_01']
            if ii['similarity'] == 'JC': JC_Lim = ii['AR_01']
            if ii['similarity'] == 'A': A_Lim = ii['AR_01']
            if ii['similarity'] == 'PA': PA_Lim = ii['AR_01']

    for ii in range(len(VxV)):
        # if VxV[ii]['x'] == VxV[ii]['y']:
        #     VxV[ii]['new'] = False
        if VxV[ii]['GD'] >= GD_Lim: # and VxV[ii]['GD'] != 0:
            VxV[ii]['new_GD'] = True
        if VxV[ii]['CN'] >= CN_Lim:
            VxV[ii]['new_CN'] = True
        if VxV[ii]['JC'] >= JC_Lim:
            VxV[ii]['new_JC'] = True
        if VxV[ii]['A'] >= A_Lim:
            VxV[ii]['new_A'] = True
        if VxV[ii]['PA'] >= PA_Lim:
            VxV[ii]['new_PA'] = True

    filename = './data/predict/' + str(i) + '_' + str(i + 1) + '.json'
    if os.path.exists(filename):
        os.remove(filename)
    with open(filename, 'w') as fout:
        json.dump([{
            'x': ii['x'],
            'y': ii['y'],
            # 'GD': ii['GD'],
            # 'CN': ii['CN'],
            # 'JC': ii['JC'],
            # 'A': ii['A'],
            # 'PA': ii['PA'],
            'new': ii['new'],
            'new_GD': ii['new_GD'],
            'new_CN': ii['new_CN'],
            'new_JC': ii['new_JC'],
            'new_A': ii['new_A'],
            'new_PA': ii['new_PA']
        } for ii in VxV], fout)