from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analysis(text : str):
    al = TextBlob(text)
    result =  al.sentiment
    
    if result[0] < -0.5:
        return 'Очень негативный текст'
    elif result[0] <= 0 and result[0] >= -0.5:
        return 'Негативный текст'
    elif result[0] >= 0 and result[0] <= 0.5:
        return 'Нейтральный текст'
    elif result[0] > 0.5 and result[0] <= 0.8:
        return 'Позитивный текст'
    elif result[0] > 0.8:
        return 'Очень позитивный текст'