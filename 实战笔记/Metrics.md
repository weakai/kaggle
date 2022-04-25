# 指标

## 回归

```python
from sklearn.metrics import mean_squared_error
```

### Simple Example of Multiple Variables Regression

```python
# the metric used in this competition
def comp_metric(xhat, yhat, fhat, x, y, f):
    intermediate = np.sqrt(np.power(xhat - x,2) + np.power(yhat-y,2)) + 15 * np.abs(fhat-f)
    return intermediate.sum()/xhat.shape[0]
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

### 指标

from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import roc_auc_score

```python
from sklearn.metrics import (
    classification_report,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

# 对两个标签分别求精度
precision_score(label_test, dict_pred[clf], average=None, labels=[0,1])
precision_score(y_true, y_pred)

def print_validation_report(y_true, y_pred):
    print("Classification Report")
    # precision    recall  f1-score   support + acc
    print(classification_report(y_true, y_pred))
    acc_sc = accuracy_score(y_true, y_pred)
    print("Accuracy : " + str(acc_sc))

    return acc_sc
```

## 多模型对比

```python
import matplotlib.pyplot as plt

# 模型名，用作 title
list_clf = ["MNB", "KNN", "SVC", "SGD", "GBC", "XGB"]

# 这是预测好的 label
list_pred = [pred_test_MNB, pred_test_grid_KNN,
             pred_test_grid_SVC, pred_test_grid_SGD,
             pred_test_grid_GBC, pred_test_grid_XGB]

dict_pred = dict(zip(list_clf, list_pred))


def plot_all_confusion_matrices(y_true, dict_all_pred, str_title):
    list_classifiers = list(dict_all_pred.keys())
    plt.figure(figsize=(10, 7.5))
    plt.suptitle(str_title, fontsize=20, fontweight='bold')
    n = 231

    for clf in list_classifiers:
        plt.subplot(n)
        # 此处定义看上边
        plot_confusion_matrix(y_true, dict_all_pred[clf])
        plt.title(clf, fontweight='bold')
        n += 1

    plt.tight_layout()
    plt.subplots_adjust(top=0.9)
```

## 操作曲线

```python
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

fpr, tpr, thr = roc_curve(true, pred)
plt.figure(figsize=(5, 5))
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic Plot')
auc_knn4 = auc(fpr, tpr) * 100
plt.legend(["AUC {0:.3f}".format(auc_knn4)]);
```
