from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

train =open("/home/encompass/Desktop/trial/https__enwikipediaorg_wiki_Sathish.txt");

test = [
    "The beer was good.", 'pos',"I do not enjoy my job", 'neg',"I ain't feeling dandy today.", 'neg',"I feel amazing!", 'pos','Gary is a friend of mine.', 'pos',"I can't believe I'm doing this.", 'neg']

cl = NaiveBayesClassifier(train)

# Classify some text
print(cl.classify("Their burgers are amazing."))  # "pos"
print(cl.classify("I don't like their pizza."))   # "neg"

# Classify a TextBlob
blob = TextBlob("The beer was amazing. But the hangover was horrible. "
                "My boss was not pleased.", classifier=cl)
print(blob)
print(blob.classify())

for sentence in blob.sentences:
    print(sentence)
    print(sentence.classify())

# Compute accuracy
print("Accuracy: {0}".format(cl.accuracy(train)))

# Show 5 most informative features
cl.show_informative_features(5)
