import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

def clean_text(text):
    """Очистка текста от мусора.
    Необходимое удаление символов для работы с текстом."""
    text = text.lower()
    regular = r'[\{+\$+\}+\|+\[+\~+\'+\_+\`+\<+\*+\–+\#+\№\"\-+\+\=+\?+\&\^\.+\;\,+\>+\(\)\/+\:\\+]'
    regular_url = r'(http\S+)|(www\S+)|([\w\d]+www\S+)|([\w\d]+http\S+)'
    text = re.sub(regular, '', text)
    text = re.sub(regular_url, r'', text)
    text = re.sub(r'(\d+\s\d+)|(\d+)','', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub('(\\b[A-Za-z] \\b|\\b [A-Za-z]\\b)', '', text)
    return text

def full_preprocessing(text):
    """Полная предобрабтка текста.
    Включается в себя очистку, токенизацию, лемматизацию и удаление стоп-слов.
    На выходе результат список статей, готовых для работы с ними."""
    stop_words = stopwords.words('english')
    stemmer = SnowballStemmer(language='english')


    # чистка текста (хотя она не нужна в лабе)
    #text = clean_text(text)
    text = text.split()
    stem_words = []
    # удаление стоп-слов
    text = [word for word in text if word not in stop_words]
    # stemmer
    for w in text:
        x = stemmer.stem(w)
        stem_words.append(x)
    return stem_words

def articles_splitter(text):
    """Возвращает список статей.

    Работает по ключевому слову УДК с использованием regex.

    Разбивает комплект статей на список статей."""
    articles = []

    for match in re.findall(r'(?<=<TEXT>)[\s\S]*?(?=</TEXT>)', text):
        match = re.sub("\s+$", "", match)
        articles.append(match)
    return articles