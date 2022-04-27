# Numpy

## np

### np 函数

```python
np.shape(numpy.ndarray) -> tuple
np.stack((test_predsf, test_predsx, test_predsy)) -> numpy.ndarray  # default: axis=0
np.vstack((a, b))  # 垂直拼接
np.hstack((a, b))  # 水平拼接
```

### np 属性

## 线代

### 模运算

[np.linalg.norm() 用法总结](https://blog.csdn.net/silent1cat/article/details/120811844)

x: 表示矩阵
ord: 表示范数类型
ord=None：表示求整体的矩阵元素平方和，再开根号

axis: 对轴操作
axis=None: 求整个矩阵的范数

keepdims：表示是否保持矩阵的二位特性，True表示保持，False表示不保持，默认为False

```python
np.linalg.norm(x, ord=None, axis=None, keepdims=False)
```
