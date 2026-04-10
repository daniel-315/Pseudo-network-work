import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load ranked edges
df = pd.read_csv("output/rankedEdges.csv")

# Keep top N edges for readability
top_n = 20
df_top = df.head(top_n)

# Build directed graph
G = nx.DiGraph()

for _, row in df_top.iterrows():
    G.add_edge(row["Gene1"], row["Gene2"], weight=row["score"])

# Draw
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=2500,
    font_size=10,
    arrows=True
)

edge_labels = {
    (row["Gene1"], row["Gene2"]): f'{row["score"]:.2f}'
    for _, row in df_top.iterrows()
}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

plt.title("Top 20 Ranked Gene Interactions")
plt.savefig("output/network_top20.png", dpi=300, bbox_inches="tight")
