# lightgbm

```python
import lightgbm as lgb

params = {
            'boosting_type': 'gbdt',
            'objective': 'regression',
            'metric': {'rmse'},
            'subsample': 0.25,
            'subsample_freq': 1,
            'learning_rate': 0.4,
            'num_leaves': 20,
            'feature_fraction': 0.9,
            'lambda_l1': 1,  
            'lambda_l2': 1
            }

# categoricals = ['catgry_feaut1', 'catgry_feaut2']
# train_X = train[feat_cols].iloc[train_index]

lgb_train = lgb.Dataset(train_X, train_y, categorical_feature=categoricals)
lgb_eval = lgb.Dataset(val_X, val_y, categorical_feature=categoricals)
gbm = lgb.train(params,
                lgb_train,
                num_boost_round=500,
                valid_sets=(lgb_train, lgb_eval),
                early_stopping_rounds=100,
                verbose_eval = 100)
```