import networkx as nx
from model import predict_traffic
import datetime

def build_graph():
    G = nx.Graph()

    G.add_edge("A", "B", distance=5)
    G.add_edge("B", "C", distance=7)
    G.add_edge("A", "C", distance=10)
    G.add_edge("C", "D", distance=6)
    G.add_edge("B", "D", distance=8)

    return G

def get_best_route(start, end):
    G = build_graph()

    now = datetime.datetime.now()
    traffic = predict_traffic(now.hour, now.weekday())

    for u, v in G.edges():
        base = G[u][v]['distance']
        G[u][v]['weight'] = base * (1 + traffic/100)

    path = nx.dijkstra_path(G, start, end, weight='weight')

    return path