from enum import Enum


class SentimentMethod(Enum):
    TEXTBLOB = "TextBlob"
    VADER = "Vader"
    FLAIR = "Flair"

class NewsSource(Enum):
    BBC = "https://www.bbc.co.uk"
    PINK = "https://www.thepinknews.com"
    VICE = "https://www.vice.com"
    INDEPENDENT = "https://www.independent.co.uk"
