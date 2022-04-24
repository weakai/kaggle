# nltk

```python
from nltk.corpus import stopwords
import string

def remove_punctuation_and_stopwords(sms):
    
    # 逐个字符，过滤掉标点符号
    sms_no_punctuation = [ch for ch in sms if ch not in string.punctuation]  # 不去空格
    sms_no_punctuation = "".join(sms_no_punctuation).split()  # 还是会根据空格来划分
    
    # 过滤掉停用词
    sms_no_punctuation_no_stopwords = \
        [word.lower() for word in sms_no_punctuation if word.lower() not in stopwords.words("english")]
        
    return sms_no_punctuation_no_stopwords

# str2str 直接应用与 series
data['text'].apply(remove_punctuation_and_stopwords)
```

## 

```python
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

sent = 'I love apple and pineapple'

print(sent)
print(sent_tokenize(sent))
print(word_tokenize(sent))

stopWords = set(stopwords.words('english'))
words = word_tokenize(sent)
wordsFiltered = []

for w in words:
    if w not in stopWords:
        # 去掉了停用词
        wordsFiltered.append(w)

print(wordsFiltered)
```