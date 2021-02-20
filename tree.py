import networkx as nx
from networkx.drawing.nx_agraph import to_agraph

from collatz import collatz

ONLY_ODD_NUMS = True

G = nx.DiGraph()

for n in range(1, 20):

    sequence = collatz(n)
    if ONLY_ODD_NUMS:
        sequence = [i for i in sequence if i % 2 == 1]

    for i, curr in enumerate(sequence):
        known = curr in G
        if i > 0:
            prev = sequence[i - 1]
            G.add_edge(prev, curr)
        if known:
            break

A = to_agraph(G)
A.draw(path='tree.svg', prog='dot')
