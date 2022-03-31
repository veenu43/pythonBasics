import flair

sentiment_model = flair.models.TextClassifier.load('en-sentiment')

sentence = flair.data.Sentence('you suck')
print(sentence)
print("sentence: ", sentiment_model.predict(sentence))
