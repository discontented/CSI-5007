from DiGraph import DiGraph

G = DiGraph(8, 0, 4)
print(G.G.edges())

u, v = [int(e) for e in input("Edge: ").split(",")]
print("Weight: %d" % G.w(u,v))
