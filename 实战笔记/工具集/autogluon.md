# AutoGluon

预测器参数 TabularPredictor:

- label = 'claim'
- eval_metric = 'roc_auc'
- path = './ag_sst'  # 模型输出的目录

训练器参数 fit:

- train_data: df
- time_limit = 7*3600
- presets:
  - 'best_quality'
- verbosity = 2
- num_stack_levels = 3  # ?
- num_bag_sets = 1  # ?
- num_bag_folds = 5
- hyperparameters = 'multimodal'  # use multimodal when has GPU
- auto_stack = True
- excluded_model_types = ['KNN']  # 排除模型

验证器参数 evaluate_predictions:

- y_true = valid_data[label]
- y_pred = y_pred_valid  # y_pred_valid = predictor.predict(valid_data)
- auxiliary_metrics = True

评估器参数 predict:

- test_data: df | csv_path

总结器参数 fit_summary:

- show_plot = True

```python
import pandas as pd
from autogluon.tabular import TabularDataset, TabularPredictor

train = TabularDataset('../input/titanic/train.csv')
test = TabularDataset('../input/titanic/test.csv')
submission = pd.read_csv('../input/titanic/gender_submission.csv')

label = 'Survived'
time_limit = 60
predictor = TabularPredictor(label=label).fit(train, time_limit=time_limit)

submission[label] = predictor.predict(test)
```

## 模型保存与加载

```python
predictor = TabularPredictor.load(save_path)
```

## 模型可解释性

```python
predictor.feature_importance(valid_data)
```

## 模型结果

```python
# 查看榜单
predictor.leaderboard()  # fit 后可调用
```

## 置信度预测

```python
predictor.predict_proba(df)[True]
```
