# Pandas

## pd

### pd 函数

```python
concat([df1, df2], axis=0).reset_index()
read_csv(file, index_col=0)
DataFrame({'c1': [1, 2], 'c2': [1, 2]}, index=['a', 'b'])
reset_index(drop=True)  # 丢掉原来的 index
```

### pd 属性

```python
```

## Series

### Series 函数

```python
value_counts() -> Series
count() -> int  # 计算 Series 长度
tolist() -> list
replace(src_value, tgt_value, ) -> DataFrame | None  # with inplace
```

### Series 属性

```python
index -> Index
values -> np.array
dtype -> numpy.dtype
dtypes -> numpy.dtype
```

## Index

### Index 函数

### Index 属性

```python

```

## DataFrame

### DataFrame 函数

```python
# FutureWarning -> pd.concat([df1, df2], axis=0).reset_index()
append(df) -> DataFrame
reset_index() -> DataFrame
rename(columns={"v1": "label", "v2": "text"}) -> DataFrame
```

### DataFrame 属性

```python
columns -> Index  # 包含列名的 Index 序列
values -> numpy.ndarray  # The same shape as df
T -> DataFrame
```

## Groupby

### Groupby 函数

transform: min, max, count, mean, std

```python
Seriesgroupby.transform() -> Series  # 聚合函数
```

### Groupby 属性

## 索引

```python
(df.col1 > 100) & (df.col2 < 500)
(df.col1 > 100) | (df.col2 < 500)
~(df.col2 < 500)
```

