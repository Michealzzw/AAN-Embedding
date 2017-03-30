import string;
import re;
import math;
import random;

MAX_WEIGHT = 10.0;

def loadDictionary():
    print("Load Dictionary");
    file_object = open('../dictionary.tsv');
    dictionary = {};
    for line in file_object:
        line = line[:-1];
        dictionary[line.split(' ')[0]] = [int(line.split(' ')[1]),float(line.split(' ')[2])];
    file_object.close();
    return dictionary;

def TFIDF(tf,wordNum,idf):
    return str(1.0*tf*math.log(1.0/idf)/wordNum);

def cosineSimilarity(vec1, vec2):
    len1 = 0.0;
    len2 = 0.0;
    res = 0.0;
    for i in range(len(vec1)):
        res = res + vec1[i]*vec2[i];
        len1 = len1 + vec1[i]*vec1[i];
        len2 = len2 + vec2[i]*vec2[i];
    return res/math.sqrt(len1*len2);

def tfidfSimilarity(wl1, wl2):
    len1 = 0.0;
    len2 = 0.0;
    res = 0.0;
    for word in wl1:
        a = wl1[word];
        len1 = len1 + a*a;
        if (word in wl2):
            res = res + a * wl2[word];
    for word in wl2:
        b = wl2[word];
        len2 = len2 + b*b;
    return res/math.sqrt(len1*len2);
