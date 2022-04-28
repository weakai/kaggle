# manifold

```python
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler  # Scaled before TSNE 
import seaborn as sns

train_sub = train.sample(10000, random_state= 42)
model = TSNE(n_components=2, random_state=0, perplexity=50, n_iter=3000)
tsne_data = model.fit_transform(StandardScaler().fit_transform(train_sub.drop('target', axis = 1).astype(float)))  # tsne_data.shape = (10000, 2)

tsne_data = np.hstack((tsne_data, train_sub[['target']]))  # train_sub[['target']].shape = (10000, 1)

# 降维后 重命名列
tsne_df = pd.DataFrame(data=tsne_data, columns=("D1", "D2", "target"))

# FacetGrid 的绘制对象是 df 格式的数据
sns.FacetGrid(tsne_df, hue="target", height=6).map(plt.scatter, 'D1', 'D2').add_legend()
plt.title('Perplexity=50, n_iter=3000')
plt.show()
```

```python
# 另一种绘图法
plt.figure(figsize=(10,10))
sns.scatterplot(x = tsne_data[:, 0], y = tsne_data[:, 1], hue = 'target', data=train_sub)
```

