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


review = "This is the best restaurant in the city"
print(getReviewSentiments(vadeSentiment))
vaderResults = getReviewSentiments(vadeSentiment)
print("keys", vaderResults.keys())
print("positive Reviews", len(vaderResults['results-on-positive']))
print("negative Reviews", len(vaderResults['results-on-negative']))