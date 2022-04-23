# KNN

```python
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier

parameters_KNN = {'n_neighbors': (10, 15, 17), }
grid_KNN = GridSearchCV(KNeighborsClassifier(), parameters_KNN, cv=5,
                        n_jobs=-1, verbose=1)
grid_KNN.fit(data_tfidf_train, label_train)
```