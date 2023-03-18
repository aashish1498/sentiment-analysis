import string
from nltk.corpus import stopwords
from nltk import tokenize
from nltk.stem import WordNetLemmatizer

from article_retriever import *


def preprocess_text(text):
    sentences = tokenize.sent_tokenize(text.lower())
    sentences = [preprocess_sentence(sentence) for sentence in sentences]
    return ' '.join(sentences)

def generate_sentences(text):
    return tokenize.sent_tokenize(text.lower())


def preprocess_sentence(text):
    word_list = tokenize.word_tokenize(_remove_punctuation(text))
    word_list = _remove_stopwords(word_list)
    word_list = _lemmatize(word_list)
    return ' '.join(word_list)


def _remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))


def _remove_stopwords(word_list):
    stop_words = set(stopwords.words('english'))
    return [word for word in word_list if word not in stop_words]


def _lemmatize(word_list):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in word_list]
