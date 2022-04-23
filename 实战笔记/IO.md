# IO

```python
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    # _ 是 dirname 下的目录
    for filename in filenames:
        print(os.path.join(dirname, filename))
```