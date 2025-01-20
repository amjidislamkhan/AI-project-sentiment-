#pip install nltk        type this and enter in terminal first
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
#nltk.download('vader_lexicon')  #run this once and comment it after that
def analyze_sentiment(text):
    sia=SentimentIntensityAnalyzer()
    scores=sia.polarity_scores(text)
    if scores['compound']>=0.05:
        return 'positive'
    elif scores['compound']<= -0.05:
        return 'negative'
    else:
        return 'neutral'
#def main():
text='ai is cool'  #change it for any sentences and check results
print(analyze_sentiment(text))
#if __name__ == "__main__":
   # main()
