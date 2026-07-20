from modules.graph_builder import graph
import networkx as nx

def find_path(source, target):

    try:

        path = nx.shortest_path(graph, source, target)

        relations = []

        for i in range(len(path)-1):

            relation = graph[path[i]][path[i+1]]["relation"]

            relations.append({
                "from": path[i],
                "relation": relation,
                "to": path[i+1]
            })

        return relations

    except:
        return []