import os
import json
from publicConstants import number_of_classes

# number_of_classes = 2

for i in range(number_of_classes - 1):
    print(i)

    with open('./data/similarities/' + str(i) + '_' + str(i + 1) + '.json') as json_file:
        VxV = [{
            'x':e['x'],
            'y':e['y'],
            'GD':e['GD'],
            'CN':e['CN'],
            'JC':e['JC'],
            'A':e['A'],
            'PA':e['PA'],
            'new': False
        } for e in json.load(json_file)]

    with open('./data/asteria/E_' + str(i) + '_' + str(i + 1) + '_new.json') as json_file:
        new_edges = [{'x':e['s'], 'y':e['t']} for e in json.load(json_file)]

    counter = 0
    counter1 = 0
    for j in new_edges:
        counter1 = counter1 + 1
        print(counter1)
        for ii in range(len(VxV)):
            if VxV[ii]['x'] == j['x'] and VxV[ii]['y'] == j['y']:
                VxV[ii]['new'] = True
                counter = counter + 1
                break
            # if j['x'] < VxV[ii]['x']:
            #     break

    print(counter)

    filename = './data/predict_preparation/' + str(i) + '_' + str(i + 1) + '.json'
    if os.path.exists(filename):
        os.remove(filename)
    with open(filename, 'w') as fout:
        json.dump([{
            'x': ii['x'],
            'y': ii['y'],
            'GD': ii['GD'],
            'CN': ii['CN'],
            'JC': ii['JC'],
            'A': ii['A'],
            'PA': ii['PA'],
            'new': ii['new']
        } for ii in VxV], fout)
