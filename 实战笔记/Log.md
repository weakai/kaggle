# Log

```python
import sys
sys.version_info
```

```python
import logging

logging.basicConfig(
    format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S", level=logging.INFO
)
logger = logging.getLogger(__name__)

try:
    data = pd.read_csv(csv_url, sep=";")
except Exception as e:
    logger.exception(
        "Unable to download training & test CSV, check your internet connection. Error: %s", e
    )
```

```python
import warnings
warnings.filterwarnings("ignore")
```

TensorFlow

```python
import tensorflow as tf
tf.get_logger().setLevel(logging.ERROR)
```

## Timer

```python
from contextlib import contextmanager
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

## IPython display

```python
from IPython.display import clear_output
clear_output()  # 运行后，后续运行的 cell 将清楚输出
```

## Pandas

```python
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option("float_format", "{:.5f}".format)  # 小数位数显示
```

## Optuna

```python
import optuna
optuna.logging.set_verbosity(optuna.logging.WARNING)
```