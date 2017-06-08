import networkx as nx

servers='server1:30080'

G = nx.DiGraph()
G.add_node('start', serverport='30080', peers=servers)
G.add_node('transfer1', type='get', protocol='tcp', size='1 KiB')
G.add_node('transfer2', type='get', protocol='tcp', size='2 KiB')
G.add_node('transfer3', type='get', protocol='tcp', size='3 KiB')
G.add_node('transfer4', type='get', protocol='tcp', size='4 KiB')
G.add_node('transfer5', type='get', protocol='tcp', size='3 KiB')
G.add_node('transfer6', type='get', protocol='tcp', size='1 KiB')
G.add_node('transfer7', type='get', protocol='tcp', size='2 KiB')
G.add_node('transfer8', type='get', protocol='tcp', size='3 KiB')
G.add_node('transfer9', type='get', protocol='tcp', size='4 KiB')
G.add_node('transfer10', type='get', protocol='tcp', size='5 KiB')

G.add_node('end', count='10')

G.add_edge('start', 'transfer1')
G.add_edge('tranfer1', 'transfer2')
G.add_edge('tranfer2', 'transfer3')
G.add_edge('tranfer3', 'transfer4')
G.add_edge('tranfer4', 'transfer5')
G.add_edge('tranfer5', 'transfer6')
G.add_edge('tranfer6', 'transfer7')
G.add_edge('tranfer7', 'transfer8')
G.add_edge('tranfer8', 'transfer9')
G.add_edge('tranfer9', 'transfer10')
G.add_edge('tranfer10', 'end')
nx.write_graphml(G, '/home/kyle/Documents/GRA/shadow/resource/nrl/tgen.client.graphml.xml')