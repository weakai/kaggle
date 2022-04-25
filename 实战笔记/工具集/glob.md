# Glob

支持三种通配

1. \*
2. ?
3. []

```python
import glob

glob.glob('./*') -> List
glob.glob('../*.pdf') -> List
glob.iglob('./*.ipynb') -> Iterator
```
