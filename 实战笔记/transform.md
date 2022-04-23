# Transform

## 标准化

```python
from sklearn.preprocessing import StandardScaler
stdsc = StandardScaler()
# 需要标准化的列
columns = ['Open', 'High', 'Low', 'Close', 'Volume', 'AdjustmentFactor', 'ExpectedDividend', 'SupervisionFlag']
# 过滤上述列
stock_price_df[columns] = stdsc.fit_transform(stock_price_df[columns])
stock_price_df.head()
```

## 编码

```python
from sklearn.preprocessing import LabelEncode
le = LabelEncoder()
# 操作 Series
train["primary_use"] = le.fit_transform(train["primary_use"])
categoricals = ["site_id", "building_id", "primary_use", "hour", "weekday", "meter",  "wind_direction"]

```

## 数据平滑

```python
# 转化偏度比较大的数据，使其更加服从高斯分布
target = np.log1p(train["meter_reading"])
# 其逆运算
revt = np.expm1(target)
```


## 类型转换

### 时间类型转化

```python
train["timestamp"] = pd.to_datetime(train["timestamp"])
train["weekday"] = train["timestamp"].dt.weekday
train["hour"] = train["timestamp"].dt.hour
train["weekday"] = train['weekday'].astype(np.uint8)
train["hour"] = train['hour'].astype(np.uint8)
train['year_built'] = train['year_built']-1900 # 1914.0, 2001, 2014
```

## Other

```python
train['square_feet'] = np.log(train['square_feet'])
```