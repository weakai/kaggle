# 数据

## 初识数

Looking some informations of all datasets

```python
print(df_train.shape)
print("")
print(df_train.head())
print("")
print(df_train.nunique())
print("")
print(df_train.columns)
```

```python
print('(rows, columns) =', stock_price_df.shape)
stock_price_df.tail()
```

numpy 数组的维度

```python
np.shape(arr)
```

## 数据类型

```python
# Nan to int 0
stock_price_df['ExpectedDividend'] = stock_price_df['ExpectedDividend'].fillna(0)
# bool to int
stock_price_df['SupervisionFlag'] = stock_price_df['SupervisionFlag'].map({True: 1, False: 0})
# date string to dtype datetime
stock_price_df['Date'] = pd.to_datetime(stock_price_df['Date'])
# check memory and dtype
stock_price_df.info()
```

## 缺失值

### 1. 丢弃

```python
stock_price_df = stock_price_df.dropna(how='any')
```

### 2. 填充

median 填充

```python
# 求所有价格为正数值的 median
median = train[(train.shop_id == 32) & (train.item_id == 2973) & (train.date_block_num == 4) & (
        train.item_price > 0)].item_price.median()
# loc 法赋值
# loc 混合索引给价格为负数的值重新赋值
train.loc[train.item_price < 0, 'item_price'] = median
```

-999 填充

```python
X_train = X_train.fillna(-999)
X_test = X_test.fillna(-999)
```

## 数据表操作

```python
# 按列融合
train = train.merge(weather_train, left_on=["site_id", "timestamp"], right_on=["site_id", "timestamp"])
```

### 分组

### 列的保留与删除

```python
categoricals = ["site_id", "building_id", "primary_use", "hour", "weekday", "meter", "wind_direction"]
drop_cols = ["sea_level_pressure", "wind_speed"]
train = train.drop(drop_cols, axis=1)
numericals = ["square_feet", "year_built", "air_temperature", "cloud_coverage",
              "dew_temperature", 'precip_depth_1_hr', 'floor_count', 'beaufort_scale']
feat_cols = categoricals + numericals
```

重命名列

```python
data = data.rename(columns={"v1": "label", "v2": "text"})
```