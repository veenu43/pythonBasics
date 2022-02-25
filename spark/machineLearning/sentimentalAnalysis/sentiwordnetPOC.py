from nltk.corpus import sentiwordnet as swn

#word = "dog"
word1 = "awesome"
common_meaning = list(swn.senti_synsets(word1))[0]
print(list(swn.senti_synsets(word1)))
print(list(swn.senti_synsets(word1))[0])
print(common_meaning.pos_score())
print(list(swn.senti_synsets(word1))[0].neg_score())

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

print(superNaiveSentiment(word1))