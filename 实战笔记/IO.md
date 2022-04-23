# IO

## Walk through DIR

```python
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    # _ 是 dirname 下的目录
    for filename in filenames:
        print(os.path.join(dirname, filename))
```

## Get DataFrame

```python
# set index to ID to avoid droping it later
test  = pd.read_csv('../input/test.csv').set_index('ID')

train_transaction = pd.read_csv('../input/train_transaction.csv', index_col='TransactionID')
```

标签与特征分离


```python
y_train = train['isFraud'].copy()  # 防止干扰源 df
X_train = train.drop('isFraud', axis=1)
X_test = test.copy()
```

