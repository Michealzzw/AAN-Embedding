import string;
import re;
import math;
import random;
import tool;


print("Running ... Get dictionary-vector")
dictionary = tool.loadDictionary();
vectors = {};


file_object = open('../paper-vectors.txt');
for line in file_object:
    line = line[:-1];
    word = line.split(' ')[0];
    if (word in dictionary):
        vectors[word] = line.split(' ')[1:];

file_object.close();

output = open("../dictionary_vector.tsv", 'w');
for word in vectors:
    output.write(word+" ");
    for vec in vectors[word]:
        output.write(vec+" ");
    output.write("\n");
output.close();
