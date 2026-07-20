import networkx as nx

graph=nx.Graph()

def add_to_graph(result):

    for e in result["entities"]:

        graph.add_node(e)

    for s,r,t in result["relationships"]:

        graph.add_edge(
            s,
            t,
            relation=r
        )