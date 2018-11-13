class node:
    def __init__(self, name, children = []):
        self.name = name
        self.children = children
        self.val = 0
    def show(self, level=0):
        print("%s%s val=%d:" % (level*"  ", self.name, self.val))
        for c in self.children: 
            c.show(level + 1)

def increment(graph):
    graph.val += 1;
    for c in graph.children:
        increment(c)

def encodeGraph(root, nodes={}):
    print("encoding a graph...")
    # nodes
    if id(root) not in nodes:
        newNode = {}
        newNode['name'] = root.name
        newNode['val'] =  root.val
        nodes[id(root)] = newNode
    # graph structure
    encoded = {}
    encoded['id'] = id(root)
    encoded['children'] = []
    # children
    for child in root.children:
        childGraph, nodesCopy = encodeGraph(child, nodes)
        encoded['children'].append(childGraph)
    return encoded, nodes

def decodeGraph(graph, nodes):
    print("decoding a graph...")
    id_ = graph['id']
    if str(id_) in nodes:
        id_ = str(id_)
        print("using string version of 'id': ", id_)
    info = nodes[id_] # get the info for that node
    print("info: ", info)
    root = node(info['name'])
    root.val = info['val']
    root.children = []
    for child in graph['children']:
        root.children.append(decodeGraph(child, nodes))
    return root
    
def show_id(graph):
    print(graph.name, ": ", id(graph))
    for c in graph.children:
        show_id(c)
