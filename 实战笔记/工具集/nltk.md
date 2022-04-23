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