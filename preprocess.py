import re, string

from nltk.corpus import stopwords
stopwords = stopwords.words('english')

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

def clean_text(text):
  text = text.lower()
  text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
  text = re.sub('(\t)', '', text)
  text = re.sub('\w*\d\w*', '', text)
  text = ' '.join(text.split())
  return text

def remove_stopwords(text):
  text = text.split()
  text = [word for word in text if not word in set(stopwords)]
  text = ' '.join(text)
  return text

def lemmatize(text):
  words = text.split()
  text = []
  for word in words:
    text.append(lemmatizer.lemmatize(word))
  text = ' '.join(text)
  return text

def preprocess_text(text):
  return lemmatize(remove_stopwords(clean_text(text)))