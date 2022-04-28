# discriminant_analysis

## LDA

LDA 降维 + sns 散点图

```python
import seaborn as sns
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

train_sub = train.sample(10000, random_state= 42)

# lda
lda_data = LDA(n_components=2).fit_transform(train_sub.drop(columns='target'), train_sub.target)

plt.figure(figsize=(10, 10))

sns.scatterplot(x=lda_data[:, 0], y=lda_data[:, 1], hue='target', data=train_sub)
```