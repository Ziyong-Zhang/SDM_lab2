import pydot
from rdflib.tools.rdf2dot import rdf2dot
from rdflib import Graph
from io import StringIO

# Load your RDF graph
graph = Graph()
graph.parse("data/tbox.ttl", format="ttl")

# Convert RDF graph to DOT format
dot_stream = StringIO()
rdf2dot(graph, dot_stream)

# Save DOT representation to a file
dot_file_path = "data/graph_schema.dot"
with open(dot_file_path, "w") as dot_file:
    dot_file.write(dot_stream.getvalue())

# Generate image from DOT file
output_image_path = "data/graph_schema.png"
(graph_image,) = pydot.graph_from_dot_file(dot_file_path)
graph_image.write_png(output_image_path)

print(f"Graph schema image generated at: {output_image_path}")
