# sklearn 特征提取

## 1. CountVectorizer： 统计 token 出现在文本中的次数

```python
from sklearn.feature_extraction.text import CountVectorizer
# remove_punctuation_and_stopwords(str) -> ['word1', 'word2']
bow_transformer = CountVectorizer(analyzer = remove_punctuation_and_stopwords).fit(data['text'])

# 查看字典的大小
print(len(bow_transformer.vocabulary_))

sample_spam = data['text'][8]
bow_sample_spam = bow_transformer.transform([sample_spam]) # bow_sample_spam sparse 矩阵
print(sample_spam)
print(np.shape(bow_sample_spam))  # (1, 9431)

# 列索引反查单词
rows, cols = bow_sample_spam.nonzero()
for col in cols: 
    print(bow_transformer.get_feature_names()[col])  

# 用 bow_transformer 在 series 上直接操作
bow_data = bow_transformer.transform(data['text'])  # bow_data sparse 矩阵
bow_data.shape  # (5572, 9431)
bow_data.nnz  # 49772 nnz 是 sparse 矩阵 零范数=稀疏度
```

## 2. TfidfTransformer

基于 CountVectorizer 求 TfidfTransformer

保持维度不变

```python
from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer().fit(bow_data)
tfidf_sample_ham = tfidf_transformer.transform(bow_sample_ham)
print(tfidf_sample_ham)

data_tfidf = tfidf_transformer.transform(bow_data)  # 也是 numpy 的稀疏矩阵
```

## TfidfVectorizer

直接将文本转化为 TfidfVectorizer

```python
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_transformer = TfidfVectorizer(analyzer = remove_punctuation_and_stopwords).fit(data['text'])
```