from nltk.corpus import sentiwordnet as swn
from nltk.sentiment import vader
from string import  punctuation
from nltk.corpus import stopwords
import nltk

stopwords = set(stopwords.words('english')+list(punctuation))

positiveReviewsFileName = "D:\\DataSets\\rt-polaritydata\\rt-polarity.pos"
with open(positiveReviewsFileName, 'r') as f:
    positiveReviews = f.readlines()
    # print(positiveReviews)

negativeReviewsFileName = "D:\\DataSets\\rt-polaritydata\\rt-polarity.neg"
with open(negativeReviewsFileName, 'r') as f:
    negativeReviews = f.readlines()
    # print(negativeReviews)

sia = vader.SentimentIntensityAnalyzer()


def vadeSentiment(review):
    return sia.polarity_scores(review)['compound']


def getReviewSentiments(sentimentCalulator):
    negReviewResult = [sentimentCalulator(oneNegativeReview) for oneNegativeReview in negativeReviews]
    posReviewResult = [sentimentCalulator(onePositiveReview) for onePositiveReview in positiveReviews]
    return {'results-on-positive': posReviewResult, 'results-on-negative': negReviewResult}


def runDiagnopstics(reviewResult):
    positiveResult = reviewResult['results-on-positive']
    negativeResult = reviewResult['results-on-negative']
    pctTruePositive = float(sum(x > 0 for x in positiveResult)) / len(positiveResult)
    pctTrueNegative = float(sum(x > 0 for x in negativeResult)) / len(negativeResult)

    totalAccurate = float(sum(x > 0 for x in positiveResult)) + float(sum(x > 0 for x in negativeResult))
    total = len(positiveResult) + len(negativeResult)
    print("Accuracy on positive reviews = " + "%.2f" % (pctTruePositive * 100) + "%")
    print("Accuracy on negative reviews = " + "%.2f" % (pctTrueNegative * 100) + "%")
    print("Overall accuracy  = " + "%.2f" % (totalAccurate*100/total) + "%")


# Build a binary Classifier using Sentiwordnet
# Run this classifier on our corpus of reviews
#Compare accuracy of VADER and Sentiwordnet-based classifiers

def superNaiveSentiment(review):
    reviewPolarity = 0.0
    numExceptions = 0
    for word in review.lower().split():
        numMeanings =0
        if word in stopwords:
            continue
        weight = 0.0
        try:
            for meaning in swn.senti_synsets(word):
                if meaning.pos_score() > meaning.neg_score():
                    weight = weight + (meaning.pos_score() - meaning.neg_score())
                    numMeanings = numMeanings + 1
                elif meaning.pos_score() < meaning.neg_score():
                    weight = weight -(meaning.neg_score() - meaning.pos_score())
                    numMeanings = numMeanings + 1
        except Exception as e:
            numExceptions = numExceptions +1
            #print(e)
        #print(f"Word: {word} weight: {str(weight)}")
        if numMeanings >0 :
                reviewPolarity = reviewPolarity+ (weight/numMeanings)
    return reviewPolarity


#print(superNaiveSentiment("Awesome"))
print(runDiagnopstics(getReviewSentiments(superNaiveSentiment)))
