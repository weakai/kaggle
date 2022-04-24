# Seaborn

## 颜色

### 常用色系

- darkred
- darkblue
- blue
- green

### 生色

```python
# total number of different collors that we will use
number_of_colors = df_structure.atom.value_counts().count()
# Here I will generate a bunch of hexadecimal colors 
color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]
```