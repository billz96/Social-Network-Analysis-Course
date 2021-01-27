import os
import networkx as nx
import json
from publicConstants import number_of_classes

# number_of_classes = 2

for i in range(number_of_classes - 1):
    E_old_0 = nx.Graph()
    E_0_new = nx.Graph()

    print(i)

    with open('./data/asteria/E_' + str(i) + '_' + str(i + 1) + '_new.json') as json_file:
        edges = [(e['s'], e['t']) for e in json.load(json_file)]
    E_0_new.add_edges_from(edges)

    with open('./data/asteria/E_' + str(i) + '_' + str(i + 1) + '_old.json') as json_file:
        edges = [(e['s'], e['t']) for e in json.load(json_file)]
    E_old_0.add_edges_from(edges)

    f = open('./data/asteria/V_' + str(i) + '_' + str(i + 1) + '.json')
    V_star = f.readlines()
    for ii in range(len(V_star)):
        V_star[ii] = int(V_star[ii].replace('\n', ''))

    s = {
        'GD': {},
        'CN': {},
        'JC': {},
        'A': {},
        'PA': {}
    }

    VxV = []
    for ii in V_star:
        for iii in V_star:
            VxV.append((ii, iii))

    for pair in VxV:
        try:
            s['GD'][pair] = -nx.shortest_path_length(E_old_0, source=pair[0], target=pair[1])
        except:
            s['GD'][pair] = -5000

        try:
            s['CN'][pair] = len(list(nx.common_neighbors(E_old_0, pair[0], pair[1])))
        except:
            s['CN'][pair] = -5000

        try:
            for u, v, p in nx.jaccard_coefficient(E_old_0, [pair]):
                s['JC'][pair] = p
        except:
            s['JC'][pair] = -5000

        try:
            for u, v, p in nx.adamic_adar_index(E_old_0, [pair]):
                s['A'][pair] = p
        except:
            s['A'][pair] = -5000

        try:
            for u, v, p in nx.preferential_attachment(E_old_0, [pair]):
                s['PA'][pair] = p
        except:
            s['PA'][pair] = -50000

    print([{
            'x': ii[0],
            'y': ii[1],
            'GD': round(s['GD'][ii], 5),
            'CN': round(s['CN'][ii], 5),
            'JC': round(s['JC'][ii], 5),
            'A': round(s['A'][ii], 5),
            'PA': round(s['PA'][ii], 5)
        } for ii in s['GD']])
    filename = './data/similarities/' + str(i) + '_' + str(i + 1) + '.json'
    if os.path.exists(filename):
        os.remove(filename)
    with open(filename, 'w') as fout:
        json.dump([{
            'x': ii[0],
            'y': ii[1],
            'GD': round(s['GD'][ii], 5),
            'CN': round(s['CN'][ii], 5),
            'JC': round(s['JC'][ii], 5),
            'A': round(s['A'][ii], 5),
            'PA': round(s['PA'][ii], 5)
        } for ii in s['GD']], fout)