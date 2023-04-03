from enum import Enum


class SentimentMethod(Enum):
    TEXTBLOB = "TextBlob"
    VADER = "Vader"
    FLAIR = "Flair"

class NewsSource(Enum):
    BBC = "https://www.bbc.co.uk"
    PINK = "https://www.thepinknews.com"
    VICE = "https://www.vice.com"
    GUARDIAN = "https://www.theguardian.com"

class Topic(Enum):
    TRANSGENDER = "transgender"
    UKRAINE = "ukraine"
    UPLIFTING = "uplifting"
    DISASTER = "disaster"

class TextType(Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"
    
class TextSource(Enum):
    ARTICLES = "articles"
    REVIEWS = "reviews"
