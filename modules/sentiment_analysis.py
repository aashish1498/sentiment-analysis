import numpy as np
from .article_retriever import *
from .preprocessing import *
from enum import Enum
from flair.nn import Classifier
from flair.splitter import SegtokSentenceSplitter
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob


class SentimentMethod(Enum):
    TEXTBLOB = "TextBlob"
    VADER = "Vader"
    FLAIR = "Flair"


_sia = SentimentIntensityAnalyzer()
_flair_classifier = Classifier.load('sentiment')
_flair_splitter = SegtokSentenceSplitter()

def get_polarity(text, method=SentimentMethod.VADER):
    if method == SentimentMethod.TEXTBLOB:
        return _get_blob_polarity(text)
    elif method == SentimentMethod.FLAIR:
        return _get_flair_polarity(text)
    elif method == SentimentMethod.VADER:
        return _get_vader_polarity(text)
    else:
        raise ValueError("Invalid method")


def _get_vader_polarity(text):
    score = _sia.polarity_scores(text)
    return score['compound']


def _get_blob_polarity(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    return polarity

def _get_flair_polarity(text):
    sentences = _flair_splitter.split(text)
    _flair_classifier.predict(sentences)
    return np.mean([_get_flair_score(sentence) for sentence in sentences])

def _get_flair_score(sentence):
    label = sentence.get_label()
    if label.value == 'POSITIVE':
        return label.score
    elif label.value == 'NEGATIVE':
        return -label.score
