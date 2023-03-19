from enum import Enum
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from article_retriever import *
from preprocessing import *


class SentimentMethod(Enum):
    TEXTBLOB = "TextBlob"
    VADER = "Vader"


_sia = SentimentIntensityAnalyzer()


def get_polarity(text, method=SentimentMethod.VADER):
    if method == SentimentMethod.TEXTBLOB:
        return _get_blob_polarity(text)
    else:
        return _get_vader_polarity(text)


def _get_vader_polarity(processed_text):
    score = _sia.polarity_scores(processed_text)
    return score['compound']


def _get_blob_polarity(processed_text):
    blob = TextBlob(processed_text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    return polarity
