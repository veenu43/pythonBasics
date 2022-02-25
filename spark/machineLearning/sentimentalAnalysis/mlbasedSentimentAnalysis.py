from nltk.corpus import sentiwordnet as swn
from nltk.sentiment import vader
from string import punctuation
from nltk.corpus import stopwords
import nltk

stopwords = set(stopwords.words('english') + list(punctuation))
testTrainingSplitIndex = 2500

positiveReviewsFileName = "D:\\DataSets\\rt-polaritydata\\rt-polarity.pos"
with open(positiveReviewsFileName, 'r') as f:
    positiveReviews = f.readlines()
    # print(positiveReviews)

negativeReviewsFileName = "D:\\DataSets\\rt-polaritydata\\rt-polarity.neg"
with open(negativeReviewsFileName, 'r') as f:
    negativeReviews = f.readlines()
    # print(negativeReviews)

testNegativeReviews = negativeReviews[testTrainingSplitIndex + 1:]
testPositiveReviews = positiveReviews[testTrainingSplitIndex + 1:]

trainingNegativeReviews = negativeReviews[:testTrainingSplitIndex]
trainingPositiveReviews = positiveReviews[:testTrainingSplitIndex]

positiveWordList = [word for line in trainingPositiveReviews for word in line.split()]
negativeWordList = [word for line in trainingNegativeReviews for word in line.split()]

# Combine all words
allWordList = [item for sublist in [positiveWordList, negativeWordList] for item in sublist]

# Eliminate duplicate
vocabulary = list(set(allWordList))
#print(vocabulary)

negTaggedTrainingReviewList = [{'review': oneReview.split(),'label': 'negative'} for oneReview in trainingNegativeReviews]
posTaggedTrainingReviewList = [{'review': oneReview.split(),'label': 'positive'} for oneReview in trainingPositiveReviews]
fullTaggedTrainingReviewList = [item for sublist in [negTaggedTrainingReviewList,posTaggedTrainingReviewList] for item in sublist]
trainingData = [(review['review'],review['label']) for review in fullTaggedTrainingReviewList]
#print(training)
def extract_features(review):
    review_words = set(review)
    features = {}
    for word in vocabulary:
        features[word] = (word in review_words)
    return features
trainingFeatures = nltk.classify.apply_features(extract_features,trainingData)
print(trainingFeatures)