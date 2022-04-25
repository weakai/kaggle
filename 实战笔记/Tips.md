# Tips

## Python 垃圾回收

- 不用了就删除，尤其是 pd
- 定义的函数内可以使用

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

另一种回收方式

```python
import gc
gc.enable()

...

gd.collect()
```

## Python 的类别

object: 类别属性

## Pandas 的切片

切到的长度等于 1，直接返回元素。大于等于 2，保持原类型返回

## Pandas 的原位操作

能用原为操作的就用原位操作省内存

## Metrics and loss function

Metrics: Evaluating the perfomance of a model