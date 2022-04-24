# Transform

## 标准化

### StandardScaler

```python
from sklearn.preprocessing import StandardScaler

stdsc = StandardScaler()
# 需要标准化的列
columns = ['Open', 'High', 'Low', 'Close', 'Volume', 'AdjustmentFactor', 'ExpectedDividend', 'SupervisionFlag']
# 过滤上述列
stock_price_df[columns] = stdsc.fit_transform(stock_price_df[columns])
stock_price_df.head()
```

### MinMaxScaler

data_tfidf_train 是 numpy 的数组

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
data_tfidf_train_sc = scaler.fit_transform(data_tfidf_train)
data_tfidf_test_sc  = scaler.transform(data_tfidf_test)
```

## 编码

字符串类型的 Label 编码

```python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
# 操作 Series
train["primary_use"] = le.fit_transform(train["primary_use"])
```

Object 对象的编码

```python
from sklearn.preprocessing import LabelEncoder

for f in X_train.columns:
    if X_train[f].dtype == 'object' or X_test[f].dtype == 'object':
        lbl = LabelEncoder()
        lbl.fit(list(X_train[f].values) + list(X_test[f].values))
        X_train[f] = lbl.transform(list(X_train[f].values))
        X_test[f] = lbl.transform(list(X_test[f].values))  
```

标签数值化

```python
data['spam'] = data['label'].map( {'spam': 1, 'ham': 0} ).astype(int)
```

## 数据平滑

```python
# 转化偏度比较大的数据，使其更加服从高斯分布
target = np.log1p(train["meter_reading"])
# 其逆运算
revt = np.expm1(target)
```

## 类型转换

### 数值类型转化

```python
train["timestamp"] = pd.to_datetime(train["timestamp"])
train["weekday"] = train["timestamp"].dt.weekday
train["hour"] = train["timestamp"].dt.hour
train["weekday"] = train['weekday'].astype(np.uint8)
train["hour"] = train['hour'].astype(np.uint8)
train['year_built'] = train['year_built'] - 1900  # 1914.0, 2001, 2014
```

## Other

```python
train['square_feet'] = np.log(train['square_feet'])
```
