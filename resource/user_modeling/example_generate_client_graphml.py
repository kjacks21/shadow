import networkx as nx

servers="server1:30080"

G = nx.DiGraph()

G.add_node("start", serverport="30080", peers=servers)
G.add_node("transfer1", type="get", protocol="tcp", size="5 KiB")
G.add_node("transfer2", type="get", protocol="tcp", size="6 KiB")
G.add_node("transfer3", type="get", protocol="tcp", size="7 KiB")
G.add_node("transfer4", type="get", protocol="tcp", size="5 KiB")
G.add_node("transfer5", type="get", protocol="tcp", size="6 KiB")
G.add_node("transfer6", type="get", protocol="tcp", size="7 KiB")
G.add_node("transfer7", type="get", protocol="tcp", size="5 KiB")
G.add_node("transfer8", type="get", protocol="tcp", size="8 KiB") # random noise
G.add_node("transfer9", type="get", protocol="tcp", size="7 KiB")
# etc... for the entire stream, potentially hundreds of these

G.add_edge("start", "transfer1")
G.add_edge("transfer1", "transfer2")
G.add_edge("transfer2", "transfer3")
G.add_edge("transfer3", "transfer4")
G.add_edge("transfer4", "transfer5")
G.add_edge("transfer5", "transfer6")
G.add_edge("transfer6", "transfer7")
G.add_edge("transfer7", "transfer8")
G.add_edge("transfer8", "transfer9")
G.add_edge("transfer9", "start")

nx.write_graphml(G, "tgen.client.graphml.xml")
