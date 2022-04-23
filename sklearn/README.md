
```shell
conda list | grep scikit-learn
# or 
python -c "import sklearn; sklearn.show_versions()"

conda install matplotlib
```

## Tricks

Get sorted random numbers with the shape of (n, 1)

```python
rng = np.random.RandomState(1)
X = np.sort(200 * rng.rand(100, 1) - 100, axis=0)
```

create an seqence with the shape of (n, 1)

```python
X_test = np.arange(0.0, 5.0, 0.01)[..., np.newaxis]
# another way
y = np.array([np.pi * np.sin(X).ravel(), np.pi * np.cos(X).ravel()]).T
```

