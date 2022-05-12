# impute

缺失值处理

```python
'''SimpleImputer(
    *,
    missing_values=nan,
    strategy='mean',
    fill_value=None,
    verbose=0,
    copy=True,
    add_indicator=False,
)
'''

from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline

# Sample the data - 100k
tps_sample = tps.sample(10000)
X, y = tps_sample.drop("claim", axis=1), tps_sample[["claim"]].values.flatten()

# Preprocess
pipe = make_pipeline(SimpleImputer(strategy="mean"))
X = pipe.fit_transform(X.copy())
```

