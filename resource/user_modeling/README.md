Network, node, and application configuration is specified in shadow.config.xml.
Client behavior models (traffic generator configs) specified in the tgen.*.graphml.xml files.
- Graph vertices represent actions and graph edges represent dependencies
- Packet loss, latency, jitter, etc. can be configured in shadow.config.xml

The pipeline from stream generation are as follows:
1. Run generate_generation_file.py, where you specify stream size, number of files
in each pattern, and the percentage of noise to add to the stream. Running this will
create custom_generate_client_graphml.py
2. Run custom_generate_client_graphml.py, which generates tgen.client.graphml.xml,
which is used in running shadow
3. Run in terminal: shadow shadow.config.xml > shadow.log
