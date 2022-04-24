# Log

```python
import sys
sys.version_info
```

## Timer

```python
@contextmanager
def timer(title):
    t0 = time.time()
    yield
    print("{} - done in {:.0f}s".format(title, time.time() - t0))

with timer('Title'):
    do()
```

## warnings

```python
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
```