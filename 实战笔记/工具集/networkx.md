# Networkx

## 分子

```python
import networkx as nx
# 创建图
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