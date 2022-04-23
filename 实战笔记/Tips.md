# Tips

## Python 垃圾回收

不用了就删除，尤其是 pd

```python
# 回收 df 的单列
del train["meter_reading"]
# 回收整个 df
del imputation_df
```