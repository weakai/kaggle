# umap

Most important parameters of UMAP

- `n_components`
- `n_neighbors`
- `min_dist`
- `metric`

正如你可能已经猜到的，`n_components`控制了投影后的维数。默认的是2，因为它易于可视化。然而，对于拥有超过100个特征的数据集，2D可能不足以完全保留数据的底层拓扑结构。我建议尝试 2-20 之间的值，步长为 5，并评估不同的基线模型，看看准确性的变化。

接下来，我们有`n_neighbors`。它控制了 UMAP 在建立流形时对每个样本的局部邻域的关注。较小的值可以将重点缩小到局部结构，考虑到特殊性和小模式，可能会失去大局。

较高的 `n_neighbors` 值提供了更大的灵活性，允许 UMAP 在相应维度上关注更广泛的数据 "视图"。当然，这也是以失去更精细的结构细节为代价的。这个参数的默认值是 15。

## 一个简单的例子

```python
import umap

train_sub = train.sample(10000, random_state= 42)  # 下采样
embedding_2d = umap.UMAP(random_state = 42 ,n_components=2).fit_transform(train_sub.drop(columns='target').to_numpy())
embedding_3d = umap.UMAP(random_state = 42 ,n_components=3).fit_transform(train_sub.drop('target', axis=1).values)  # 注意写法

# 2D
plt.figure(figsize=(10,10))
sns.scatterplot(x = embedding_2d[:, 0], y = embedding_2d[:, 1], hue='target', data=train_sub)

# plt 画法
# plt.scatter(embedding_2d[:, 0], embedding_2d[:, 1], c=train_sub.target, s=0.5);

# 3D
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

## 一个较完整的例子

注意：QuantileTransformer 对于 umap 是有效分类是必要的

```python
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline

# Sample the data - 100k
tps_sample = tps.sample(10000)
X, y = tps_sample.drop("claim", axis=1), tps_sample["claim"].values.shape

# Preprocess
pipe = make_pipeline(SimpleImputer(strategy="mean"), QuantileTransformer())
X = pipe.fit_transform(X.copy())

# Fit UMAP to processed data
manifold = umap.UMAP().fit(X, y)
X_reduced_2 = manifold.transform(X)

# Plot the results
plt.scatter(X_reduced_2[:, 0], X_reduced_2[:, 1], c=y, s=0.5);
```

更好的例子

```python
import umap
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PowerTransformer
import pandas as pd

# Scale
pipe = make_pipeline(PowerTransformer())
X = pipe.fit_transform(X.copy())

# Encode the target to numeric
y_encoded = pd.factorize(y)[0]

manifold = umap.UMAP().fit(X, y_encoded)
```
