# 数据可视化

## 数值描述

```python
# 数值: 打印数值数据的分位
# 类别: count, unique, top, freq
melbourne_data_df.describe()

# 按 label 类分别描述
data.groupby("label").describe()
```

### Series 类别计数

```python
data.label.value_counts()
data.label.value_counts().plot.bar();  # 计数的可视化， 组方图
```

### 字符串长度

```python
data['length'] = data['text'].apply(len)
# 根据 label 分别画 n_labels 张图, 然后按 lenth 画组方图
data.hist(column='length', by='label', bins=60, figsize=(12, 4));  # ; 为抑制输出
plt.xlim(-40, 950);
```

## df 类别数据的计数以及类内数值分布

```python
plt.figure(figsize=(15, 10))

g = plt.subplot(211)
g = sns.countplot(x='type', data=df_train, )
g.set_title("Count of Different Molecule Types", fontsize=22)
g.set_xlabel("Molecular Type Name", fontsize=18)
g.set_ylabel("Count Molecules in each Type", fontsize=18)

g1 = plt.subplot(212)
g1 = sns.boxplot(x='type', y='scalar_coupling_constant', data=df_train)
g1.set_title("Count of Different Molecule Types", fontsize=22)
g1.set_xlabel("Molecular Type Name", fontsize=18)
g1.set_ylabel("Scalar Coupling distribution", fontsize=18)

# 调整子图
plt.subplots_adjust(wspace=0.5, hspace=0.5, top=0.9)

plt.show()
```

### boxenplot 箱线计数图

```python
g = sns.boxenplot(x='atom_index_0', y='scalar_coupling_constant', data=df_train, color='darkred' )
```

## 数值数据

```python
# 随机采样绘制 scalar_coupling_constant 的分布图
n_sample = 200000
df_train['scalar_coupling_constant'].sample(n_sample).iplot(
    kind='hist',
    title='Scalar Coupling Constant Distribuition',
    xTitle='Scalar Coupling value',
    yTitle='Probability',
    histnorm='percent')
```

## 离异值

```python
plt.figure(figsize=(10, 4))
# xlim 限制的是坐标轴的显示范围，根据最大最小值限定
plt.xlim(train.item_price.min(), train.item_price.max() * 1.1)
sns.boxplot(x=train.item_price)

# 手动设置 xlim
plt.figure(figsize=(10, 4))
plt.xlim(-100, 3000)
sns.boxplot(x=train.item_cnt_day)
```

## 双变量的分布

### 索引交叉

```python
cross_index = ['atom_index_0', 'atom_index_1']  # seting the desired 

cm = sns.light_palette("green", as_cmap=True)
pd.crosstab(df_train[cross_index[0]], df_train[cross_index[1]]).style.background_gradient(cmap = cm)
```

均值

```python
pd.crosstab(df_train[scalar_index_cross[0]], df_train[scalar_index_cross[1]], 
            values=df_train['scalar_coupling_constant'], aggfunc=['mean']).style.background_gradient(cmap = cm)
```

## 自然语言

### 词云 WordClouds

```python
import wordcloud


def show_wordcloud(data_spam_or_ham, title):
    # 要求是 tokenized str
    text = ' '.join(data_spam_or_ham['text'].astype(str).tolist())
    stopwords = set(wordcloud.STOPWORDS)

    fig_wordcloud = wordcloud.WordCloud(stopwords=stopwords, background_color='lightgrey',
                                        colormap='viridis', width=800, height=600).generate(text)

    plt.figure(figsize=(10, 7), frameon=True)
    plt.imshow(fig_wordcloud)
    plt.axis('off')
    plt.title(title, fontsize=20)
    plt.show()


show_wordcloud(data_ham, "Ham messages")
```

### Top 30 words in ham and spam messages

使用 collections.Counter 计数

```python
from collections import Counter

# remove_punctuation_and_stopwords(sentence) -> [words1, words2, ...]

data_ham.loc[:, 'text'] = data_ham['text'].apply(remove_punctuation_and_stopwords)
words_data_ham = data_ham['text'].tolist()

list_ham_words = []
for sublist in words_data_ham:
    for item in sublist:
        list_ham_words.append(item)

# 使用 Counter 对 list 的元素直接计数
c_ham = Counter(list_ham_words)

# most_common -> [('a',2), ('b', 4), ...]
# 所以 DataFrame 理论上可以接受任何形式的 二维 数据
df_hamwords_top30 = pd.DataFrame(c_ham.most_common(30), columns=['word', 'count'])

fig, ax = plt.subplots(figsize=(10, 6))
# ax 制定需要绘制的坐标轴
sns.barplot(x='word', y='count',
            data=df_hamwords_top30, ax=ax)
plt.title("Top 30 Ham words")
plt.xticks(rotation='vertical');
```

直接使用 NLTK 的 FreqDist 代替 collections.Counter

```python
# remove_punctuation_and_stopwords(sentence) -> [words1, words2, ...]

data_ham.loc[:, 'text'] = data_ham['text'].apply(remove_punctuation_and_stopwords)
words_data_ham = data_ham['text'].tolist()

list_ham_words = []
for sublist in words_data_ham:
    for item in sublist:
        list_ham_words.append(item)

fdist_ham = nltk.FreqDist(list_ham_words)
df_hamwords_top30_nltk = pd.DataFrame(fdist_ham.most_common(30), columns=['word', 'count'])
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='word', y='count',
            data=df_hamwords_top30_nltk, ax=ax)
plt.title("Top 30 Ham words")
plt.xticks(rotation='vertical');
```
