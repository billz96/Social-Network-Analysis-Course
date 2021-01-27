import os
import networkx as nx
from publicConstants import number_of_classes
import json

def writeStr2File(filename, string):
    if os.path.exists(filename):
        os.remove(filename)
    f = open(filename, 'x')
    f.write(string)
    f.close()

for i in range(number_of_classes - 1):
    print(i)

    G_old = nx.Graph()
    G_new = nx.Graph()
    G_old.clear()
    G_new.clear()

    with open('./data/' + str(i) + '/data.json') as json_file:
        edges = [(e['s'], e['t']) for e in json.load(json_file)]
    G_old.add_edges_from(edges)
    with open('./data/' + str(i + 1) + '/data.json') as json_file:
        edges = [(e['s'], e['t']) for e in json.load(json_file)]
    G_new.add_edges_from(edges)

    # V j-1 eos j+1
    G_intersection_nodes = list(set(G_new.nodes()).intersection(set(G_old.nodes())))

    G_old_edges = G_old.edges()
    G_new_edges = G_new.edges()

    # E asteri j-1 eos 0
    E_asteri_old_0 = []
    for ii in G_old_edges:
        for j in G_intersection_nodes:
            if ii[0] == j:
                for k in G_intersection_nodes:
                    if ii[1] == k:
                        E_asteri_old_0.append(ii)
                        break

    # print(E_asteri_old_0)
    print(len(E_asteri_old_0))
    # E asteri 0 eos j+1
    E_asteri_0_new = []
    for ii in G_new_edges:
        for j in G_intersection_nodes:
            if ii[0] == j:
                for k in G_intersection_nodes:
                    if ii[1] == k:
                        E_asteri_0_new.append(ii)
                        break

    # print(E_asteri_0_new)
    print(len(E_asteri_0_new))
    # break
    str1 = '['
    for ii in E_asteri_0_new:
        str1 = str1 + '{"s": ' + str(ii[0]) + ', "t": ' + str(ii[1]) + '},'
    str1 = str1[:-1] + ']'
    writeStr2File('./data/asteria/E_' + str(i) + '_' + str(i+1) + '_new.json', str1)

    str1 = '['
    for ii in E_asteri_old_0:
        str1 = str1 + '{"s": ' + str(ii[0]) + ', "t": ' + str(ii[1]) + '},'
    str1 = str1[:-1] + ']'
    writeStr2File('./data/asteria/E_' + str(i) + '_' + str(i + 1) + '_old.json', str1)

    str1 = ''
    for ii in G_intersection_nodes:
        str1 = str1 + str(ii) + '\n'
    writeStr2File('./data/asteria/V_' + str(i) + '_' + str(i + 1) + '.json', str1)