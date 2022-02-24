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


review = "This is the best restaurant in the city"
print(getReviewSentiments(vadeSentiment))
vaderResults = getReviewSentiments(vadeSentiment)
print("keys", vaderResults.keys())
print("positive Reviews", len(vaderResults['results-on-positive']))
print("negative Reviews", len(vaderResults['results-on-negative']))
print(runDiagnopstics(getReviewSentiments(vadeSentiment)))
