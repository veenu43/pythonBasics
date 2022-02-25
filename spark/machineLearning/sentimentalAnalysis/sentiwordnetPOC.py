from nltk.corpus import sentiwordnet as swn
from string import  punctuation
from nltk.corpus import stopwords
stopwords = set(stopwords.words('english')+list(punctuation))
#word = "dog"
word1 = "awesome"
'''
common_meaning = list(swn.senti_synsets(word1))[0]
print(list(swn.senti_synsets(word1)))
print(list(swn.senti_synsets(word1))[0])
print(common_meaning.pos_score())
print(list(swn.senti_synsets(word1))[0].neg_score())
'''
def superNaiveSentiment(review):
    reviewPolarity = 0.0
    numExceptions = 0
    for word in review.lower().split():
        weight = 0.0
        try:
            print(f"word: {word} ")
            common_meaning = list(swn.senti_synsets(word))[0]
            print(f"common_meaning: {common_meaning} ")
            if(common_meaning.pos_score() > common_meaning.neg_score()):
                weight = weight + common_meaning.pos_score()
            elif common_meaning.pos_score() < common_meaning.neg_score():
                weight = weight - common_meaning.neg_score()
        except  Exception as e:
            numExceptions = numExceptions +1
            print(e)
        print(f"Word: {word} weight: {str(weight)}")
        reviewPolarity = reviewPolarity+weight
    return reviewPolarity


def superNaiveSentiment1(review):
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

#print(superNaiveSentiment(word1))
#print(superNaiveSentiment1(word1))

word2 = "this is the best restaurant in the city"
word3 = "this is not the best restaurant in the city"
print(superNaiveSentiment1(word2))
print(superNaiveSentiment1(word3))

