# Tips

## Python 垃圾回收

不用了就删除，尤其是 pd

```python
# 回收 df 的单列
del train["meter_reading"]
# 回收整个 df
del imputation_df

# 大规模回收
import gc
del train, train_X, val_X, lgb_train, lgb_eval, train_y, val_y, target
gc.collect()
```

## Python 的类别

object: 类别属性