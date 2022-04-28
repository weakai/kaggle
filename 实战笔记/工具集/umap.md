# umap

```python
import umap

train_sub = train.sample(10000, random_state= 42)  # 下采样
embedding_2d = umap.UMAP(random_state = 42 ,n_components=2).fit_transform(train_sub.drop(columns='target').to_numpy())
embedding_3d = umap.UMAP(random_state = 42 ,n_components=3).fit_transform(train_sub.drop('target', axis=1).values)  # 注意写法

# 2D
plt.figure(figsize=(10,10))
sns.scatterplot(x = embedding_2d[:, 0], y = embedding_2d[:, 1], hue='target', data=train_sub)

plt.figure(figsize=(50,30))
umap_3d = px.scatter_3d(
    embedding_3d,
    x=0, y=1, z=2,
    labels={'color': 'target'},
    color= train_sub.target,
    color_discrete_sequence=['red', 'seagreen', 'gold', 'black'],
)

umap_3d.update_traces(marker_size=2)
umap_3d.show()
```

## 3D
