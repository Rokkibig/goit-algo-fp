import uuid
import networkx as nx
import matplotlib.pyplot as plt

def draw_heap(heap):
    class Node:
        def __init__(self, val):
            self.val = val
            self.id = str(uuid.uuid4())
            self.left = None
            self.right = None

    def build_tree(i):
        if i >= len(heap):
            return None
        node = Node(heap[i])
        node.left = build_tree(2*i+1)
        node.right = build_tree(2*i+2)
        return node

    def add_edges(graph, node, pos, x=0, y=0, layer=1):
        if node:
            graph.add_node(node.id, label=node.val)
            if node.left:
                graph.add_edge(node.id, node.left.id)
                l = x - 1 / 2**layer
                pos[node.left.id] = (l, y-1)
                add_edges(graph, node.left, pos, l, y-1, layer+1)
            if node.right:
                graph.add_edge(node.id, node.right.id)
                r = x + 1 / 2**layer
                pos[node.right.id] = (r, y-1)
                add_edges(graph, node.right, pos, r, y-1, layer+1)

    root = build_tree(0)
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(tree, root, pos)
    labels = {n: d['label'] for n, d in tree.nodes(data=True)}
    plt.figure(figsize=(8,5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2000, node_color="skyblue")
    plt.show()

if __name__ == "__main__":
    draw_heap([10, 20, 30, 40, 50, 60, 70])
