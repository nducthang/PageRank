import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = pd.read_csv('./data/testmini.txt', sep=" ", header=None, skiprows=4)
    G = nx.DiGraph()
    for i in range(len(data)):
        G.add_node(data.iloc[i][0])
        G.add_node(data.iloc[i][1])
        G.add_edge(data.iloc[i][0], data.iloc[i][1])

    N = len(G)
    d = 0.9
    rank = {}
    for node in G.nodes:
        rank[node] = 1/N
    
    for _ in range(10000):
        for node in G.nodes:
            if len(G.out_edges(node)) == 0:
                for j in G.nodes:
                    G.add_edge(node, j)
            rank_sum = 0
            edges = G.in_edges(node)
            for j , _ in edges:
                outlinks = len(G.out_edges(j))
                if outlinks > 0:
                    rank_sum += rank[j]/len(G.out_edges(j))

            rank[node] = (1-d)/N + d*rank_sum
            
    print("Tổng số node:", len(rank))
    print(rank)

    # test display graph
    display = 1
    if display:
        pos = nx.spring_layout(G)
        values = [rank.get(node, 0.25) for node in G.nodes()]
        nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),node_color = values, node_size = 500)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edges(G, pos, edge_color='r', arrows=True)
        plt.show()