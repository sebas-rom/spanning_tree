class Node:
    def __init__(self, name):
        self.name = name
        self.connections = []
        

class Ethernet(Node):
    def __init__(self, name):
        super().__init__(name)
        

class Switch(Node):
    def __init__(self, name):
        super().__init__(name)
        
        
class Network:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.name] = node

    def add_connection(self, node1, node2):
        node1.connections.append(node2)
        node2.connections.append(node1)

    def build_network(self):
        switch_a = Switch('A')
        switch_b = Switch('B')
        switch_c = Switch('C')
        switch_d = Switch('D')
        switch_e = Switch('E')
        ethernet1 = Ethernet('1')
        ethernet2 = Ethernet('2')
        ethernet5 = Ethernet('5')
        ethernet6 = Ethernet('6')
        ethernet8 = Ethernet('8')

        self.add_node(switch_a)
        self.add_node(switch_b)
        self.add_node(switch_c)
        self.add_node(switch_d)
        self.add_node(switch_e)
        self.add_node(ethernet1)
        self.add_node(ethernet2)
        self.add_node(ethernet5)
        self.add_node(ethernet6)
        self.add_node(ethernet8)

        self.add_connection(switch_a, switch_b)
        self.add_connection(switch_a, switch_c)
        self.add_connection(switch_a, switch_d)
        self.add_connection(switch_a, switch_e)
        self.add_connection(switch_a, ethernet2)

        self.add_connection(switch_b, switch_c)
        self.add_connection(switch_b, ethernet5)

        self.add_connection(switch_c, ethernet6)
        self.add_connection(switch_c, switch_e)

        self.add_connection(switch_d, switch_e)
        self.add_connection(switch_d, ethernet8)

        self.add_connection(switch_e, ethernet1)

        return self.nodes

    def spanning_tree(self):
        visited = set()
        tree = []
        stack = [nodes["A"]]
        
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                tree.append(node)
                for neighbor in node.connections:
                    stack.append(neighbor)
                    
        for x in self.nodes:   
            nodes[x].connections=[]
            
        
        for i in range(len(tree)):
            if i == 0:
                #print("joining",tree[0].name," with ",tree[i+1].name)
                self.add_connection(nodes[tree[0].name],nodes[tree[i+1].name])
                
            if i+1<len(tree) and i!=0:
                if isinstance(tree[i+1], Switch):
                    #print("joining",tree[0].name," with ",tree[i+1].name)
                    self.add_connection(nodes[tree[0].name],nodes[tree[i+1].name])
                    if i+2<len(tree):
                        if isinstance(tree[i+2], Ethernet):
                            #print("joining",tree[i+1].name," with ",tree[i+2].name)
                            self.add_connection(nodes[tree[i+1].name],nodes[tree[i+2].name])
                
        return tree
    
if __name__ == '__main__':

    
    import networkx as nx
    import matplotlib.pyplot as plt
    
    network = Network()
    nodes = network.build_network()
  
    G = nx.Graph()
    for node in nodes.values():
        G.add_node(node.name)
        for conn in node.connections:
            G.add_edge(node.name, conn.name)
    
    pos = nx.spring_layout(G)
    
    switch_nodes = [node.name for node in nodes.values() if isinstance(node, Switch)]
    ethernet_nodes = [node.name for node in nodes.values() if isinstance(node, Ethernet)]
    
    nx.draw_networkx_nodes(G, pos, nodelist=switch_nodes, node_size=500, node_color='lightblue')
    nx.draw_networkx_nodes(G, pos, nodelist=ethernet_nodes, node_size=500, node_color='lightgreen')
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)
    
    plt.axis('off')
    plt.show()
    
    
    
    tree = network.spanning_tree()
    
    nodes2 = network.nodes  
    G2 = nx.Graph()
    for node in nodes2.values():
        G2.add_node(node.name)
        for conn in node.connections:
            G2.add_edge(node.name, conn.name)
    
    pos2 = nx.spring_layout(G2)
    
    switch_nodes2 = [node.name for node in nodes2.values() if isinstance(node, Switch)]
    ethernet_nodes2 = [node.name for node in nodes2.values() if isinstance(node, Ethernet)]
    
    nx.draw_networkx_nodes(G2, pos2, nodelist=switch_nodes2, node_size=500, node_color='lightblue')
    nx.draw_networkx_nodes(G2, pos2, nodelist=ethernet_nodes2, node_size=500, node_color='lightgreen')
    nx.draw_networkx_edges(G2, pos2)
    nx.draw_networkx_labels(G2, pos2)
    
    plt.axis('off')
    plt.show()
