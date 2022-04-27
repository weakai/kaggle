# IO

## 目录遍历

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

# 或者
# 该操作在时序数据中比较常见
train_transaction = pd.read_csv('../input/train_transaction.csv', index_col='TransactionID')
```

### 标签与特征分离

```python
y_train = train['isFraud'].copy()  # 防止干扰源 df
X_train = train.drop('isFraud', axis=1)
X_test = test.copy()
```

另一种写法

```python
target = [column for column in df.columns if "target" in column] 
features = df.columns.drop(target)
```

## ...

```python
# Preprocess application_train.csv and application_test.csv
def application_train_test(num_rows = None, nan_as_category = False):
    # Read data and merge
    df = pd.read_csv('../input/application_train.csv', nrows=num_rows)
    test_df = pd.read_csv('../input/application_test.csv', nrows=num_rows)
    print("Train samples: {}, test samples: {}".format(len(df), len(test_df)))
    df = df.append(test_df).reset_index()
    # Optional: Remove 4 applications with XNA CODE_GENDER (train set)
    df = df[df['CODE_GENDER'] != 'XNA']
    
    # Categorical features with Binary encode (0 or 1; two categories)
    for bin_feature in ['CODE_GENDER', 'FLAG_OWN_CAR', 'FLAG_OWN_REALTY']:
        df[bin_feature], uniques = pd.factorize(df[bin_feature])
    # Categorical features with One-Hot encode
    df, cat_cols = one_hot_encoder(df, nan_as_category)
    
    # NaN values for DAYS_EMPLOYED: 365.243 -> nan
    df['DAYS_EMPLOYED'].replace(365243, np.nan, inplace= True)
    # Some simple new features (percentages)
    df['DAYS_EMPLOYED_PERC'] = df['DAYS_EMPLOYED'] / df['DAYS_BIRTH']
    df['INCOME_CREDIT_PERC'] = df['AMT_INCOME_TOTAL'] / df['AMT_CREDIT']
    df['INCOME_PER_PERSON'] = df['AMT_INCOME_TOTAL'] / df['CNT_FAM_MEMBERS']
    df['ANNUITY_INCOME_PERC'] = df['AMT_ANNUITY'] / df['AMT_INCOME_TOTAL']
    df['PAYMENT_RATE'] = df['AMT_ANNUITY'] / df['AMT_CREDIT']
    del test_df
    gc.collect()
    return df
```

