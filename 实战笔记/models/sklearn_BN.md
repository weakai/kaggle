# 贝叶斯

```python
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

spam_detect_model = MultinomialNB().fit(data_tfidf_train, label_train)
pred_test_MNB = spam_detect_model.predict(data_tfidf_test)
acc_MNB = accuracy_score(label_test, pred_test_MNB)
print(acc_MNB)
```

