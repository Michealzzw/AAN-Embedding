import string;
import re;
import math;
import random;

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
