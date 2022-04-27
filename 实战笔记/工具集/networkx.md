# Networkx


## 函数

### nx

```python
info()  # 任意 nx 对象
spring_layout(fb) -> pos  # 点生成布局
draw_networkx(fb, pos, with_labels = False, node_size = 35)
```

## 建图

### 边法建图

```python
edgelist = [['Mannheim', 'Frankfurt', 85], ['Mannheim', 'Karlsruhe', 80], ...]

g = nx.Graph()
for edge in edgelist:
    g.add_edge(edge[0], edge[1], weight = edge[2])

plt.rcParams['figure.figsize'] = (11, 11)

pos = nx.spring_layout(g)
# drawing nodes
nx.draw_networkx(g, pos)
plt.title('Undirected Graphs', fontsize = 20)
plt.axis('off')
plt.show()
```

各种点位布局

```python
['bipartite_layout',
 'circular_layout',
 'kamada_kawai_layout',
 'random_layout',
 'rescale_layout',
 'shell_layout',
 'spring_layout',
 'spectral_layout',
 'fruchterman_reingold_layout']
 '''
```

## 常用算法

连通组分 Connected Component

```python
for i, x in enumerate(nx.connected_components(g)):
    print("cc"+str(i)+":",x)
```

Shortest paths

```python
nx.shortest_path(g, 'Stuttgart', 'Frankfurt', weight='weight')
print(nx.shortest_path_length(g, 'Stuttgart','Frankfurt',weight='weight'))
for x in nx.all_pairs_dijkstra_path(g,weight='weight'):
    print(x)
```

最小生成树 Minimum Spanning Tree

```python
nx.draw_networkx(nx.minimum_spanning_tree(g))
```

Pagerank

```python
fb = nx.read_edgelist('../input/facebook-combined.txt', create_using = nx.Graph(), nodetype = int)
```

中心性 Centrality

```python

```

## 应用实例

## 分子

```python
import networkx as nx
# 边法建图 起始点的列 终止点的列 边属性列
fig, ax = plt.subplots(figsize = (20, 12))
for i, t in enumerate(df_train['type'].unique()):
    train_type = df_train.loc[df_train['type'] == t]
    # G = nx.from_pandas_edgelist(train_type, 'atom_index_0', 'atom_index_1', ['scalar_coupling_constant'])
    G = nx.from_pandas_edgelist(train_type, 'atom_index_0', 'atom_index_1', ['dist'])
    # subplot(nrows, ncols, index, **kwargs)
    plt.subplot(2, 4, i + 1);
    nx.draw(G, with_labels=True);
    plt.title(f'Graph for type {t}')
```

