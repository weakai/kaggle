# 预处理

## Transorm

### PowerTransformer

PowerTransformer is a straightforward log transform.

```python
from sklearn.preprocessing import PowerTransformer
from sklearn.pipeline import make_pipeline

pipe = make_pipeline(PowerTransformer())
X = pipe.fit_transform(X.copy())
```