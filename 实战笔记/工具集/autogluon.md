# AutoGluon

预测器参数:

- label = 'claim'
- eval_metric = 'roc_auc'

训练器参数:

- train_data: df
- time_limit = 7*3600
- presets:
  - 'best_quality'
- verbosity = 2

预测器参数

- test_data: df | csv_path

```python
import pandas as pd
from autogluon.tabular import TabularDataset, TabularPredictor

train = TabularDataset('../input/titanic/train.csv')
test = TabularDataset('../input/titanic/test.csv')

label = 'Survived'
time_limit = 60
predictor = TabularPredictor(label=label).fit(train, time_limit=time_limit)

submission = pd.read_csv('../input/titanic/gender_submission.csv')
submission[label] = predictor.predict(test)
```