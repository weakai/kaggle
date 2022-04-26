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

### 字符串类型的 Label 编码

```python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
# 操作 Series
train["primary_use"] = le.fit_transform(train["primary_use"])
```

### Object 对象的编码

```python
# Method 1
from sklearn.preprocessing import LabelEncoder

for f in X_train.columns:
    if X_train[f].dtype == 'object' or X_test[f].dtype == 'object':
        lbl = LabelEncoder()
        lbl.fit(list(X_train[f].values) + list(X_test[f].values))
        X_train[f] = lbl.transform(list(X_train[f].values))
        X_test[f] = lbl.transform(list(X_test[f].values))  
```

```python
# Method 1
from sklearn.preprocessing import LabelEncoder

for f in ['atom_index_0', 'atom_index_1', 'atom_1', 'type_0', 'type']:
    if f in good_columns:
        lbl = LabelEncoder()
        lbl.fit(list(df_train[f].values) + list(df_test[f].values))
        df_train[f] = lbl.transform(list(df_train[f].values))
        df_test[f] = lbl.transform(list(df_test[f].values))
```

```python
# Method 3

```

### 使用 pandas 的 get_dummies()

```python
def one_hot_encoder(df, nan_as_category = True):
    """df 原位操作
    """
    original_columns = list(df.columns)  # Index -> List
    categorical_columns = [col for col in df.columns if df[col].dtype == 'object']
    df = pd.get_dummies(df, columns=categorical_columns, dummy_na=nan_as_category)
    new_columns = [c for c in df.columns if c not in original_columns]
    return df, new_columns
```

### 标签数值化，将字符串类别映射到整数

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
