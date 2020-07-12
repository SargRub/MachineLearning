from bs4 import BeautifulSoup
import requests
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re

url = input()
website = requests.get(url)
text = website.text

soup = BeautifulSoup(text, 'html.parser')
pattern = re.compile(r'\w+')
words = pattern.findall(soup.get_text())

stop_words = stopwords.words('english')

porter = PorterStemmer()
root_words_non_stop_words = [porter.stem(word) for word in words if porter.stem(word) not in stop_words]
cleared_words = []
for word in root_words_non_stop_words:
    if word not in cleared_words:
        cleared_words.append(word)

print(cleared_words)