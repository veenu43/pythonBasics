from nltk.sentiment import vader
import nltk

# nltk.download()
sia = vader.SentimentIntensityAnalyzer()
print(sia.polarity_scores("What a terrible restaurant"))
print()

# Emoticons
print("Emoticons")
print(":D : ", sia.polarity_scores(":D"))
print(":) : ", sia.polarity_scores(":)"))
print(":/: ", sia.polarity_scores(":/"))
print()

# Idioms
print("Idioms")
print("the cumin was the kiss of death: ", sia.polarity_scores("the cumin was the kiss of death"))
print()

# Punctuation
print("Punctuation")
print("the food was good", sia.polarity_scores("the cumin was the kiss of death"))
print("Terrible", sia.polarity_scores("Terrible"))
print("Terrible! : ", sia.polarity_scores("Terrible!"))
print("Terrible!! : ", sia.polarity_scores("Terrible!!"))
print()

# Negation
print("Negation")
print("the food was good!! :", sia.polarity_scores("the food was good!!"))
print("the food was not good!! :", sia.polarity_scores("the food was not good!!"))
print("the food was not the worst!! :", sia.polarity_scores("the food was not the worst!!"))
print()

# Emphasis like Captilizationa,booster word
print("Emphasis")
print("the food was good :", sia.polarity_scores("the food was good"))
print("the food was GOOD :", sia.polarity_scores("the food was GOOD"))
print("the food was so good :", sia.polarity_scores("the food was so good"))
print()

# Contrast
print("Contrast")
print("I usually hate seafood but I liked this :", sia.polarity_scores("I usually hate seafood but I liked this"))
print("I usually hate seafood and I liked this :", sia.polarity_scores("I usually hate seafood and I liked this"))
