# 指标

## 回归

```python
from sklearn.metrics import mean_squared_error
```

## 分类

### 混淆矩阵

```python
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

def plot_confusion_matrix(y_true, y_pred, ax=1):
    mtx = confusion_matrix(y_true, y_pred)
    # fig, ax = plt.subplots(figsize=(4,4))
    sns.heatmap(mtx, annot=True, fmt='d', linewidths=.5,
                cmap="Blues", cbar=False, ax=ax)
    #  square=True,
    plt.ylabel('true label')
    plt.xlabel('predicted label')
```

### 报告准确率

```python
from sklearn.metrics import classification_report, accuracy_score
def print_validation_report(y_true, y_pred):
    print("Classification Report")
    print(classification_report(y_true, y_pred))
    acc_sc = accuracy_score(y_true, y_pred)
    print("Accuracy : " + str(acc_sc))

    return acc_sc
```
