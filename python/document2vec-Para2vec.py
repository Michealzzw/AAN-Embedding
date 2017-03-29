
import string;
import re;
import math;
import random;

#citation2vector = {};
document2vector = {};
document2vectorNum = {};

Citationcontext2Document2vector = {};
Citationcontext2Document2vectorNum = {};

CitaionContext2vector = {};
CitaionContext2vectorNum = {};

print("Running ... Building CitationContext2vec-Para2vec")
file_object = open('paper-vectors.txt');
outputCite = open('CitationContext2vec-Para2vec.tsv','w');
for line in file_object:
    line = line[:-1];
    word = line.split(' ')[0];
    if (("=>") in word):
        #outputCite.write(line+"\n");
        docId = word.split('>')[1];
        citeId = word.split('>')[0]+">"+word.split('>')[1];
        if (citeId in CitaionContext2vector):
            vec = line.split(' ')[1:-1];
            nowvec = CitaionContext2vector[citeId];
            for i in range(len(vec)):
                nowvec[i] = nowvec[i] + float(vec[i]);
            CitaionContext2vectorNum[citeId] = CitaionContext2vectorNum[citeId] + 1;
        else:
            arr = [];
            vec = line.split(' ')[1:-1];
            for i in range(len(vec)):
                arr.append(float(vec[i]));
            CitaionContext2vector[citeId] = arr;
            CitaionContext2vectorNum[citeId] = 1;
        if (docId in Citationcontext2Document2vector):
            vec = line.split(' ')[1:-1];
            nowvec = Citationcontext2Document2vector[docId];
            for i in range(len(vec)):
                nowvec[i] = nowvec[i] + float(vec[i]);
            Citationcontext2Document2vectorNum[docId] = Citationcontext2Document2vectorNum[docId] + 1;
        else:
            arr = [];
            vec = line.split(' ')[1:-1];
            for i in range(len(vec)):
                arr.append(float(vec[i]));
            Citationcontext2Document2vector[docId] = arr;
            Citationcontext2Document2vectorNum[docId] = 1;
    if ('_' in word):
        docId = word.split('_')[0];
        if (docId in document2vector):
            vec = line.split(' ')[1:-1];
            nowvec = document2vector[docId];
            for i in range(len(vec)):
                nowvec[i] = nowvec[i] + float(vec[i]);
            document2vectorNum[docId] = document2vectorNum[docId] + 1;
        else:
            arr = [];
            vec = line.split(' ')[1:-1];
            for i in range(len(vec)):
                arr.append(float(vec[i]));
            document2vector[docId] = arr;
            document2vectorNum[docId] = 1;

for citeId in CitaionContext2vector:
    outputCite.write(citeId+" ");
    paraNum = CitaionContext2vectorNum[citeId];
    vec = CitaionContext2vector[citeId];
    for i in range(len(vec)):
        vec[i] = vec[i]/paraNum;
        outputCite.write(str(vec[i])+' ');
    outputCite.write("\n");
outputCite.close();

print("Running ... Building document2vec-Para2vec")
outputDocument = open('document2vec-Para2vec.tsv','w');
for docid in document2vector:
    outputDocument.write(docid+" ");
    paraNum = document2vectorNum[docid];
    vec = document2vector[docid];
    for i in range(len(vec)):
        vec[i] = vec[i]/paraNum;
        outputDocument.write(str(vec[i])+' ');
    outputDocument.write("\n");
outputDocument.close();


print("Running ... Building CitationContext2Document-Para2vec")
outputDocument = open('CitationContext2Document-Para2vec.tsv','w');
for docid in Citationcontext2Document2vector:
    outputDocument.write(docid+" ");
    paraNum = Citationcontext2Document2vectorNum[docid];
    vec = Citationcontext2Document2vector[docid];
    for i in range(len(vec)):
        vec[i] = vec[i]/paraNum;
        outputDocument.write(str(vec[i])+' ');
    outputDocument.write("\n");
outputDocument.close();





file_object.close();
outputCite.close();
