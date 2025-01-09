from Node import Node
from network import generate_eventrates, create_random_tree
from graph import create_fog_graph

class INES():
    allPais: int
    network: list[Node]
    eventrates: list[list[int]]


    primitiveEvents: list[int]
    def __init__(self, nwSize: int, node_event_ratio: float, num_eventtypes: int, eventskew: float, max_partens: int):
        self.eventrates = generate_eventrates(eventskew,num_eventtypes)
        self.primitiveEvents= self.eventrates[0]
        root, self.network = create_random_tree(nwSize,self.eventrates,node_event_ratio,max_partens) 
        self.graph = create_fog_graph(self.network)

from graph import draw_graph
my_ines = INES(50,0.5,6,0.3,2)
print(my_ines.network)
draw_graph(my_ines.graph)

for i in my_ines.network:
    print(i)