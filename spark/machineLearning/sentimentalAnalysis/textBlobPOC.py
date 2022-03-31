from textblob import TextBlob, Word, Blobber


text = TextBlob("Pluralsight is a great place for learning amazing technology courses")
print (text)
print(text.sentiment.polarity)