from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from article_retriever import *
from preprocessing import *

sia = SentimentIntensityAnalyzer()

def get_vader_polarity(processed_text):
    score = sia.polarity_scores(processed_text)
    return score['compound']

def get_blob_polarity(processed_text):
    blob = TextBlob(processed_text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    return polarity
