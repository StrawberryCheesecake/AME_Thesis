import nltk
import pandas
import numpy as np
import string
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
#def splitdates(dates, news):


def clean_news(news_name):
    file = pandas.read_csv(news_name)
    dates = np.array(file['Date'])
    news = np.array(file['News'])
    stemmer = PorterStemmer()
    lemmer = WordNetLemmatizer()

    #lem and then stem the words as well as remove stop words + punctuation
    newslines = []
    #give the news an index range of 0:1 if we want to test the code
    for line in news[0:3]:
        #remove punctuation
        nline = line.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))
        words = word_tokenize(nline)
        stems = []
        lems = []
        #remove stop words
        words_no_stop = [word for word in words if not word in stopwords.words()]
        #print (words_no_stop)
        #first we lemminize the word string so we can get the base form of each word ie from better to good
        for word in words_no_stop:
            lems.append(lemmer.lemmatize(word))
        #print (lems)
        #next we stem the words so that we can get the base stem of each word ie from died to die we do this because
        #we want to reduce the number of features the model has to accept in hopes to improve performance
        for word in lems:
            #stem and lem words, lem seems to be very computationally heavy may have to remove
            #lem seems much better, should just run once and save results
            #do we want to try lemming and then stemming the words?
            stems.append(stemmer.stem(word))
        #print (np.array(stems))
        newslines.append(np.array(stems))
    #print to test show the result of lem and stem
    #print (dates)
    newslines = np.array(newslines)
    #combine the dates and the now processed news

    #DELETE THIS WHEN DOING WHOLE FILE
    dates = dates[0:3]
    final = []
    for x,y in zip(dates,newslines):
        final.append([x,y])
    df = pandas.DataFrame (final, columns = ['date', 'newslines'])
    df.to_csv('./data/cleanednews.csv')
    exit()
    return
