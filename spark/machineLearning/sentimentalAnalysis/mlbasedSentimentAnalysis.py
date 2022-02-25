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

def getVocabulary():
    positiveWordList = [word for line in trainingPositiveReviews for word in line.split()]
    negativeWordList = [word for line in trainingNegativeReviews for word in line.split()]

    # Combine all words
    allWordList = [item for sublist in [positiveWordList, negativeWordList] for item in sublist]

    # Eliminate duplicate
    allwordSet = list(set(allWordList))
    vocabulary = allwordSet
    print("Vocabulary: ", len(vocabulary))
    print("Sample vocabulary: ", vocabulary[0])
    return vocabulary

vocabulary = getVocabulary()


def getTrainingData():
    negTaggedTrainingReviewList = [{'review': oneReview.split(),'label': 'negative'} for oneReview in trainingNegativeReviews]
    posTaggedTrainingReviewList = [{'review': oneReview.split(),'label': 'positive'} for oneReview in trainingPositiveReviews]
    fullTaggedTrainingReviewList = [item for sublist in [negTaggedTrainingReviewList,posTaggedTrainingReviewList] for item in sublist]
    trainingData = [(review['review'],review['label']) for review in fullTaggedTrainingReviewList]
    #print(training)
    print("TrainingData: ", len(trainingData))
    print("Sample TrainingData: ", trainingData[0])
    return  trainingData

trainingData = getTrainingData()

def extract_features(review):
    review_words = set(review)
    features = {}
    for word in vocabulary:
        features[word] = (word in review_words)
    #print("Feature sample", features)
    return features

def getTrainedNaiveBayesClassifier(extract_features,trainingData):
    trainingFeatures = nltk.classify.apply_features(extract_features,trainingData)
    #print(trainingFeatures)
    trainedNBCClassifier = nltk.NaiveBayesClassifier.train(trainingFeatures)
    return trainedNBCClassifier

trainedNBCClassifier = getTrainedNaiveBayesClassifier(extract_features,trainingData);

def naiveBayessSentimentCalculator(review):
    problemInstance = review.split()
    problemFeatures = extract_features(problemInstance)
    return trainedNBCClassifier.classify(problemFeatures)

print("What an Awesome Moview",naiveBayessSentimentCalculator("What an Awesome Moview"))
print("What an terrible Moview",naiveBayessSentimentCalculator("What an terrible Moview"))

def getTestReviewSentiments(naiveBayesSentimentCalculator):
    testNegResults = [naiveBayesSentimentCalculator(review) for review in testNegativeReviews]
    testPosResults = [naiveBayesSentimentCalculator(review) for review in testPositiveReviews]
    lableToNum = {'positive':1,'negative': -1}
    numericNegResults = [lableToNum[x] for x in testNegResults]
    numericPosResults = [lableToNum[x] for x in testPosResults]
    return {'results-on-positive':numericPosResults,'results-on-negative':numericNegResults}


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

