import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = pd.read_csv('./data2/web-Stanford.txt', sep="\t", header=None, skiprows=4)
    G = nx.DiGraph()
    for i in range(len(data)):
        G.add_node(data.iloc[i][0])
        G.add_node(data.iloc[i][1])
        G.add_edge(data.iloc[i][0], data.iloc[i][1])

    N = len(G)
    d = 0.85
    rank = {}
    for node in G.nodes:
        rank[node] = 1/N
    
    for _ in range(10):
        for node in G.nodes:
            rank_sum = 0
            edge_outlinks = G.out_edges(node)
            for _ , j in edge_outlinks:
                outlinks = len(G.out_edges(j))
                if outlinks > 0:
                    rank_sum += rank[j]/len(G.out_edges(j))

            rank[node] = (1-d)/N + d*rank_sum
            
    print("Tổng số node:", len(rank))
    print(rank)

    # test display graph
    display = 0
    if display:
        pos = nx.spring_layout(G)
        values = [rank.get(node, 0.25) for node in G.nodes()]
        nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),node_color = values, node_size = 500)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edges(G, pos, edge_color='r', arrows=True)
        plt.show()