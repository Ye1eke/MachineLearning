bow = []
# combining all together
def make_bag(new_item=None):
    global bow
    new_item_list = []
    if new_item is not None:
        if isinstance(new_item, list):
            new_item_list = new_item
        if isinstance(new_item, str):
            new_item_list = [x for x in new_item.split()]
    for item in new_item_list:
        final_item = item.lower().strip()
        if final_item not in bow:
            bow.append(final_item)
    return bow

bag = []
def file_to_bow(filepath='text1.txt'): # filepath here can be actually empty
    global bag
    with open(filepath, 'r') as f:
        lines = f.readlines()
        for line in lines:
            escaped_line = line.replace('\n', '')
            bag = make_bag(escaped_line)


from nltk.corpus import wordnet
# below function imported from web to mark up the words in text format
def pos_tagger(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

def lemmatization(bag):
    words_tags = [(w, pos_tagger.get(pos[0], 'n')) for w, pos in bag.tags]
    lemma_list = [wd.lemmatize(tag) for wd, tag in words_tags]
    lemmatized_sentence = " ".join(lemma_list)
    return lemmatized_sentence



# TF / IDF Vectorization
def findTF(bag):
    TF = []
    for bags in bag:
        words = dict()
        for word in words:
            words[word] = bags.count(word) / len(bags)
        TF.append(words)

    return TF

import math
def findIDF(bag):
    num = 4
    words = dict()
    for word in words:
        curr = 1
        for bags in bag:
            if word in bags:
                curr += 1
        words[word] = math.log(num / curr)

    return words

from random import *
def centroid(cluster, length):
    centroid = []
    for i in range(0, cluster):
        for coordinate in range(0, length):
            centroid.append(uniform(0, 1))
        centroid.append(centroid)
    return centroid

def clusters(matrix, centroid):
    cluster = []
    for i in matrix:
        ind = -1
        for centroid in centroid:
            curr = math.dist(centroid, i)
            min = 999999999
            if curr < min:
                min = curr
                ind += 1
        print()
        if ind == 0:
            cluster.append(i)
    return cluster

def matrixOfVectorization(bag, TF, IDF):
    sum = []
    for tf in TF:
        result = []
        for bags in bag:
            result.append(tf[bags] * IDF[bags])
        sum.append(result)
    return sum

file_to_bow(filepath='text_1.txt')
file_to_bow(filepath='text_2.txt')
file_to_bow(filepath='text_3.txt')
file_to_bow(filepath='text_4.txt')
file_to_bow(filepath='text_5.txt')
file_to_bow(filepath='text_6.txt')
file_to_bow(filepath='text_7.txt')
file_to_bow(filepath='text_8.txt')
file_to_bow(filepath='text_9.txt')
file_to_bow(filepath='text_10.txt')
print(bag)
print()

TF = findTF(bag)
for i in TF:
    print(i)

IDF = findIDF(bag)
print(IDF)

for i in matrixOfVectorization(bag, TF, IDF):
    print(i)
    max = []
    max.append(max(i))
print()

centroid = centroid(len(bag))

for i in range(0, 1):
    cluster = clusters(centroid)
    print("Length of the cluster -> " + str(len(cluster)) + " cluster:" + str(cluster))

    print()
    if cluster:
        centroid = [sum(x) / len(x) for x in zip(*cluster)]

    print(centroid)