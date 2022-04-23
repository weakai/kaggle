# scipy

## 稀疏矩阵

### 稀疏矩阵创建与转换

```python
from scipy.sparse import coo_matrix, hstack
A = coo_matrix([[1, 2], [3, 4]])
B = coo_matrix([[5], [6]])

A.toarray()
A.A


```

稀疏矩阵的拼接

```python
from scipy.sparse import hstack

X2 = hstack((data_tfidf, np.array(data['length'])[:, None])).A
```
