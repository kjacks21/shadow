import numpy as np

def generate_stream(stream_length, num_files, noise):
    """
    stream_length: int
    length of entire stream of transfers
    
    num_files: int
    number of file sizes in stream
    
    noise: float
    percentage for noise added to stream
    
    """
    stream = []
    file_size = 1
    for i in range(stream_length):
        if file_size > num_files:
            file_size = 1
        
        if np.random.random_sample() < noise:
            stream.append(np.random.randint(1,num_files+1)) # adding to num_files increases the number of possible noise files
        else:
            stream.append(file_size)
        file_size += 1
        
    index = list(range(1, stream_length+1))
    
    return stream, index



with open("/home/kyle/Documents/GRA/shadow/resource/nrl/custom_generate_client_graphml.py", "w") as text_file:
    text_file.write("import networkx as nx\n\n")
    text_file.write("servers='server1:30080'\n\n")
    text_file.write("G = nx.DiGraph()\n")
    text_file.write("G.add_node('start', serverport='30080', peers=servers)\n")
    
    stream, index = generate_stream(10, 5, 0.2)
    
    for i, file in enumerate(stream):
        text_file.write("G.add_node('transfer%d', type='get', protocol='tcp', size='%d KiB')\n" % (i+1, file))
        
    text_file.write("\nG.add_node('end', count='%d')\n\n" % 10)
        
    text_file.write("G.add_edge('start', 'transfer1')\n")
    for i in index[1:]:
        text_file.write("G.add_edge('tranfer%d', 'transfer%d')\n" % (i-1,i))
    text_file.write("G.add_edge('tranfer%d', 'end')\n" % (index[-1]))
    text_file.write("nx.write_graphml(G, '/home/kyle/Documents/GRA/shadow/resource/nrl/tgen.client.graphml.xml')")
    
    
    
    
    
    
    
