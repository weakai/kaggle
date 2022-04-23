# XGboost

## 分类器

```python
import xgboost as xgb

clf = xgb.XGBClassifier(n_estimators=500,
                        n_jobs=4,
                        max_depth=9,
                        learning_rate=0.05,
                        subsample=0.9,
                        colsample_bytree=0.9,
                        missing=-999)
clf.fit(X_train, y_train)
sample_submission['isFraud'] = clf.predict_proba(X_test)[:, 1]
sample_submission.to_csv('simple_xgboost.csv')
```