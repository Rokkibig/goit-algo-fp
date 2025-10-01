import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.id = str(uuid.uuid4())
        self.left = None
        self.right = None

def draw_tree_with_colors(root, order):
    tree = nx.DiGraph()
    pos = {}
    colors = {}
    def add_edges(node, x=0, y=0, layer=1):
        if node:
            tree.add_node(node.id, label=node.val)
            pos[node.id] = (x, y)
            if node.left:
                tree.add_edge(node.id, node.left.id)
                add_edges(node.left, x-1/2**layer, y-1, layer+1)
            if node.right:
                tree.add_edge(node.id, node.right.id)
                add_edges(node.right, x+1/2**layer, y-1, layer+1)
    add_edges(root)

    palette = plt.cm.Blues
    for i, node in enumerate(order):
        colors[node.id] = palette(0.3 + 0.7*i/len(order))

    node_colors = [colors[n] for n in tree.nodes()]
    labels = {n: d['label'] for n, d in tree.nodes(data=True)}
    plt.figure(figsize=(8,5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2000, node_color=node_colors)
    plt.show()

def bfs(root):
    order = []
    q = deque([root])
    while q:
        node = q.popleft()
        order.append(node)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
    return order

def dfs(root):
    order = []
    stack = [root]
    while stack:
        node = stack.pop()
        order.append(node)
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
    return order

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    bfs_order = bfs(root)
    draw_tree_with_colors(root, bfs_order)
    dfs_order = dfs(root)
    draw_tree_with_colors(root, dfs_order)
