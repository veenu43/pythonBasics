from nltk.corpus import sentiwordnet as swn
from nltk.sentiment import vader
import nltk

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
        weight = 0.0
        try:
            common_meaning = list(swn.senti_synsets(word))[0]
            #print(f"common_meaning: {common_meaning} ")
            if(common_meaning.pos_score() > common_meaning.neg_score()):
                weight = weight + common_meaning.pos_score()
            elif common_meaning.pos_score() < common_meaning.neg_score():
                weight = weight - common_meaning.neg_score()
        except Exception as e:
            numExceptions = numExceptions +1
            #print(e)
        #print(f"Word: {word} weight: {str(weight)}")
        reviewPolarity = reviewPolarity+weight
    return reviewPolarity


#print(superNaiveSentiment("Awesome"))
print(runDiagnopstics(getReviewSentiments(superNaiveSentiment)))
