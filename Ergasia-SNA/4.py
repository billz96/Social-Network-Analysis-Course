import networkx as nx
import json
import os
import matplotlib.pyplot as plt
from publicConstants import number_of_classes

def printgraph(G, type, classname, filename):
    plt.clf()
    plt.plot([type[n] for n in G.nodes()])
    plt.xlabel(str(classname) + '-' + filename)
    plt.ylabel('')
    plt.savefig('./data/' + str(classname) + '/' + filename)
    # plt.show()

for i in range(number_of_classes):
    G = nx.DiGraph()
    G.clear()
    with open('./data/' + str(i) + '/data.json') as json_file:
        edges = [(e['s'], e['t']) for e in json.load(json_file)]

    G.add_edges_from(edges)
    print('')
    print('number of class: ' + str(i))
    print('count edges: ' + str(G.number_of_edges()))

    print('dc')
    dc = nx.degree_centrality(G)
    printgraph(G, dc, i, 'dc.png')
    print('kc')
    kc = nx.katz_centrality_numpy(G)
    printgraph(G, kc, i, 'kc.png')
    print('ec')
    ec = nx.eigenvector_centrality(G)
    printgraph(G, ec, i, 'ec.png')
    print('cc')
    cc = nx.closeness_centrality(G)
    printgraph(G, cc, i, 'cc.png')
    print('bc')
    bc = nx.betweenness_centrality(G)
    printgraph(G, bc, i, 'bc.png')
    print('idc')
    idc = nx.in_degree_centrality(G)
    printgraph(G, idc, i, 'idc.png')
    print('odc')
    odc = nx.out_degree_centrality(G)
    printgraph(G, odc, i, 'odc.png')

    filename = './data/' + str(i) + '/diktes.json'
    if os.path.exists(filename):
        os.remove(filename)
    f = open(filename, 'x')
    f.write(json.dumps({
        'dc': dc,
        'cc': cc,
        'bc': bc,
        'ec': ec,
        'kc': kc,
        'idc': idc,
        'odc': odc
    }))
    f.close()