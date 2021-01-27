import os
import json
from publicConstants import number_of_classes

# number_of_classes = 2

for i in range(number_of_classes - 1):
    print(i)

    with open('./data/predict/' + str(i) + '_' + str(i + 1) + '.json') as json_file:
        VxV = [{
            'x':e['x'],
            'y':e['y'],
            'new': e['new'],
            'new_GD': e['new_GD'],
            'new_CN': e['new_CN'],
            'new_JC': e['new_JC'],
            'new_A': e['new_A'],
            'new_PA': e['new_PA']
        } for e in json.load(json_file)]

    total_new_edges = 0
    total_new_edges_GD = 0
    total_new_edges_succ_GD = 0
    total_new_edges_CN = 0
    total_new_edges_succ_CN = 0
    total_new_edges_JC = 0
    total_new_edges_succ_JC = 0
    total_new_edges_A = 0
    total_new_edges_succ_A = 0
    total_new_edges_PA = 0
    total_new_edges_succ_PA = 0

    for ii in VxV:
        if ii['new']:
            total_new_edges = total_new_edges + 1
            if ii['new_GD'] and ii['x'] != ii['y']:
                total_new_edges_succ_GD = total_new_edges_succ_GD + 1
            if ii['new_CN']:
                total_new_edges_succ_CN = total_new_edges_succ_CN + 1
            if ii['new_JC']:
                total_new_edges_succ_JC = total_new_edges_succ_JC + 1
            if ii['new_A']:
                total_new_edges_succ_A = total_new_edges_succ_A + 1
            if ii['new_PA']:
                total_new_edges_succ_PA = total_new_edges_succ_PA + 1
        if ii['new_GD']:
            total_new_edges_GD = total_new_edges_GD + 1
        if ii['new_CN']:
            total_new_edges_CN = total_new_edges_CN + 1
        if ii['new_JC']:
            total_new_edges_JC = total_new_edges_JC + 1
        if ii['new_A']:
            total_new_edges_A = total_new_edges_A + 1
        if ii['new_PA']:
            total_new_edges_PA = total_new_edges_PA + 1

    filename = './data/predict_statistics/' + str(i) + '_' + str(i + 1) + '.json'
    if os.path.exists(filename):
        os.remove(filename)
    f = open(filename, 'x')

    f.write('Total new edges: ' + str(total_new_edges) + '\n\n')

    f.write('---   GD   ---' + '\n')
    f.write('Predicted edges: ' + str(total_new_edges_GD) + '\n')
    f.write('Succefully predicted edges: ' + str(total_new_edges_succ_GD) + ' (' + str(round(total_new_edges_succ_GD / total_new_edges_GD * 100)) + '%)\n')
    f.write('Not succefully predicted edges: ' + str(total_new_edges_GD - total_new_edges_succ_GD) + ' (' + str(round(((total_new_edges_GD - total_new_edges_succ_GD) / total_new_edges_GD) * 100)) + '%)\n')
    f.write('Total percent: ' + str(round(total_new_edges_succ_GD / total_new_edges * 100)) + ' %\n\n')

    f.write('---   CN   ---' + '\n')
    f.write('Predicted edges: ' + str(total_new_edges_CN) + '\n')
    f.write('Succefully predicted edges: ' + str(total_new_edges_succ_CN) + ' (' + str(round(total_new_edges_succ_CN / total_new_edges_CN * 100)) + '%)\n')
    f.write('Not succefully predicted edges: ' + str(total_new_edges_CN - total_new_edges_succ_CN) + ' (' + str(round(((total_new_edges_CN - total_new_edges_succ_CN) / total_new_edges_CN) * 100)) + '%)\n')
    f.write('Total percent: ' + str(round(total_new_edges_succ_CN / total_new_edges * 100)) + ' %\n\n')

    f.write('---   JC   ---' + '\n')
    f.write('Predicted edges: ' + str(total_new_edges_JC) + '\n')
    f.write('Succefully predicted edges: ' + str(total_new_edges_succ_JC) + ' (' + str(round(total_new_edges_succ_JC / total_new_edges_JC * 100)) + '%)\n')
    f.write('Not succefully predicted edges: ' + str(total_new_edges_JC - total_new_edges_succ_JC) + ' (' + str(round(((total_new_edges_JC - total_new_edges_succ_JC) / total_new_edges_JC) * 100)) + '%)\n')
    f.write('Total percent: ' + str(round(total_new_edges_succ_JC / total_new_edges * 100)) + ' %\n\n')

    f.write('---   A   ---' + '\n')
    f.write('Predicted edges: ' + str(total_new_edges_A) + '\n')
    f.write('Succefully predicted edges: ' + str(total_new_edges_succ_A) + ' (' + str(round(total_new_edges_succ_A / total_new_edges_A * 100)) + '%)\n')
    f.write('Not succefully predicted edges: ' + str(total_new_edges_A - total_new_edges_succ_A) + ' (' + str(round(((total_new_edges_A - total_new_edges_succ_A) / total_new_edges_A) * 100)) + '%)\n')
    f.write('Total percent: ' + str(round(total_new_edges_succ_A / total_new_edges * 100)) + ' %\n\n')

    f.write('---   PA   ---' + '\n')
    f.write('Predicted edges: ' + str(total_new_edges_PA) + '\n')
    f.write('Succefully predicted edges: ' + str(total_new_edges_succ_PA) + ' (' + str(round(total_new_edges_succ_PA / total_new_edges_PA * 100)) + '%)\n')
    f.write('Not succefully predicted edges: ' + str(total_new_edges_PA - total_new_edges_succ_PA) + ' (' + str(round(((total_new_edges_PA - total_new_edges_succ_PA) / total_new_edges_PA) * 100)) + '%)\n')
    f.write('Total percent: ' + str(round(total_new_edges_succ_PA / total_new_edges * 100)) + '%')

    f.close()
