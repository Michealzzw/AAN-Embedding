
import string;
import re;
import math;
import random;
import sys;
dictionary_vector = {};
print("Load dictionary vector");
file_object = open('../dictionary_vector.tsv');
for line in file_object:
    word = line.split(" ")[0];
    arr = [];
    for dim in line[:-1].split(" ")[1:-1]:
        arr.append(float(dim));
    dictionary_vector[word] = arr;



print("Running ... Building CitationContext2vec-Word2vec")
file_object = open('../CitationContextEmbedding/CitationContext2vec-TF.tsv');
outputCite = open('../CitationContextEmbedding/CitationContext2vec-Word2vec.tsv','w');
docuNum = 0;
for line in file_object:
    docuNum = docuNum+1;
    if (docuNum % 100 ==0):
        sys.stdout.write("%d/100335\r"%(docuNum))
        sys.stdout.flush();
    cite = line.split("\t")[0];
    wordlist = line.split("\t")[1].split(" ")[:-1];
    arr = [];
    wordnum = 0;
    for wordpair in wordlist:
        word = wordpair.split(":")[0];
        tf = int(wordpair.split(":")[1]);
        wordnum = wordnum + tf;
        vec = dictionary_vector[word];
        if not arr:
            for i in range(len(vec)):
                arr.append(vec[i]*tf);
        else:
            for i in range(len(vec)):
                arr[i] = arr[i]+ (vec[i]*tf);

    outputCite.write(cite+"\t");
    for i in range(len(arr)):
        arr[i] = arr[i]/wordnum;
        outputCite.write(str(arr[i])+" ");
    outputCite.write("\n");



file_object.close();
outputCite.close();



print("Running ... Building CitationContext2Document-Word2vec")
file_object = open('../CitationContext2Document/CitationContext2Document-TF.tsv');
outputCite = open('../CitationContext2Document/CitationContext2Document-Word2vec.tsv','w');
docuNum = 0;
for line in file_object:
    docuNum = docuNum+1;
    if (docuNum % 100 ==0):
        sys.stdout.write("%d/26000\r"%(docuNum))
        sys.stdout.flush();
    cite = line.split("\t")[0];
    wordlist = line.split("\t")[1].split(" ")[:-1];
    arr = [];
    wordnum = 0;
    for wordpair in wordlist:
        word = wordpair.split(":")[0];
        tf = int(wordpair.split(":")[1]);
        wordnum = wordnum + tf;
        vec = dictionary_vector[word];
        if not arr:
            for i in range(len(vec)):
                arr.append(vec[i]*tf);
        else:
            for i in range(len(vec)):
                arr[i] = arr[i]+ (vec[i]*tf);

    outputCite.write(cite+"\t");
    for i in range(len(arr)):
        arr[i] = arr[i]/wordnum;
        outputCite.write(str(arr[i])+" ");
    outputCite.write("\n");



file_object.close();
outputCite.close();

print("Running ... Building document2vec-Word2vec")
file_object = open('../DocumentEmbedding/document2vec-TF.tsv');
outputCite = open('../DocumentEmbedding/document2vec-Word2vec.tsv','w');
docuNum = 0;
for line in file_object:
    docuNum = docuNum+1;
    if (docuNum % 100 ==0):
        sys.stdout.write("%d/26000\r"%(docuNum))
        sys.stdout.flush();
    cite = line.split("\t")[0];
    wordlist = line.split("\t")[1].split(" ")[:-1];
    arr = [];
    wordnum = 0;
    for wordpair in wordlist:
        word = wordpair.split(":")[0];
        tf = int(wordpair.split(":")[1]);
        wordnum = wordnum + tf;
        vec = dictionary_vector[word];
        if not arr:
            for i in range(len(vec)):
                arr.append(vec[i]*tf);
        else:
            for i in range(len(vec)):
                arr[i] = arr[i]+ (vec[i]*tf);

    outputCite.write(cite+"\t");
    for i in range(len(arr)):
        arr[i] = arr[i]/wordnum;
        outputCite.write(str(arr[i])+" ");
    outputCite.write("\n");



file_object.close();
outputCite.close();
