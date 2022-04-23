# LSHForest

文本的类似性能够分为两类：一类是机械类似性；一类是语义类似性。
机械类似性代表着，两个文本内容上的相关程度。比方“你好吗”和“你好”的类似性。纯粹代表着内容上字符是否全然共现，应用场景在：文章去重；
语义类似性代表着，两个文本语义上的类似程度。比方“苹果”和“公司”的类似性。本篇不做这一讨论

## 随机投影森林

### 随机投影森林理论与实现伪代码

当数据个数比較大的时候，线性搜索寻找KNN的时间开销太大，并且须要读取全部的数据在内存中，这是不现实的。因此，实际project上，使用近似近期邻也就是ANN问题。
当中一种方法是利用随机投影树，对全部的数据进行划分，将每次搜索与计算的点的数目减小到一个可接受的范围，然后建立多个随机投影树构成随机投影森林，将森林的综合结果作为终于的结果。

随机投影森林的建立须要两个參数。即单棵树的深度 + 森林数量。这两个參数决定了数据集的分散程度以及随机投影后得到的向量维数。

利用这棵树对新的点进行近期邻计算时，首先通过计算该点与每次划分所用向量的点积。来找到其所属于的叶节点，然后利用这个叶节点内的这些点进行近期邻算法的计算。

这个过程是一棵随机投影树的计算过程。利用相同的方法。建立多个随机投影树构成随机森林，将森林的总和结果作为终于的结果。

## LSHForest/sklearn

LSHforest=LSH+随机投影树
在python的sklearn 中有 LSHForest 能够实现。

```python
class sklearn.neighbors.LSHForest(n_estimators=10, radius=1.0, n_candidates=50, n_neighbors=5, min_hash_match=4, radius_cutoff_ratio=0.9, random_state=None)
```

随机投影森林是近期邻搜索方法的一种替代方法。

LSH森林数据结构使用已排序数组、二进制搜索和32位固定长度的哈希表达。

随机投影计算距离是使用近似余弦距离。

### 案例一则

```python
from sklearn.neighbors import LSHForest

X_train = [[5, 5, 2], [21, 5, 5], [1, 1, 1], [8, 9, 1], [6, 10, 2]]
X_test = [[9, 1, 6], [3, 1, 10], [7, 10, 3]]

lshf = LSHForest(random_state=42)
lshf.fit(X_train)  
LSHForest(min_hash_match=4, n_candidates=50, n_estimators=10,
          n_neighbors=5, radius=1.0, radius_cutoff_ratio=0.9,
          random_state=42)

distances, indices = lshf.kneighbors(X_test, n_neighbors=2)

>>> distances                                        
array([[ 0.069...,  0.149...],
       [ 0.229...,  0.481...],
       [ 0.004...,  0.014...]])

>>> indices
array([[1, 2],
       [2, 0],
       [4, 0]])
```


## See also

- [LSH︱python 实现局部敏感随机投影森林——LSHForest/sklearn（一）](https://www.cnblogs.com/zhchoutai/p/8277181.html)