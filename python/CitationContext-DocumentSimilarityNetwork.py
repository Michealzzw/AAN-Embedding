import string;
import re;
import math;
import random;
import tool;


cceFile = "../CitationContextEmbedding/CitationContext2vec-Para2vec.tsv"
d2vFile = "../DocumentEmbedding/document2vec-Para2vec.tsv";
ccdsnPath = "../CitationContext-DocumentSimilarityNetwork/"
prefix = "CitationContext-DocumentSimilarityNetwork";
docVector = {};
test_edge = {};
print("Load acl links and test links")
file_object = open('../aan_testing.tsv');
for line in file_object:
    test_edge[line[:-2]] = 1;
file_object.close();

print "Load document vector";
file_object = open(d2vFile);
for line in file_object:
    docid = line.split("\t")[0];
    w_arr = line.split("\t")[1].split(' ')[:-1];
    arr = [];
    for w in w_arr:
        arr.append(float(w));
    docVector[docid] = arr;
file_object.close();

print "Running ... Building CitationContext-DocumentSimilarityNetwork Owner+Target";
outputOwner = open(ccdsnPath+prefix+"-owner.tsv",'w');
outputTarget = open(ccdsnPath+prefix+"-target.tsv",'w');
file_object = open(cceFile);
for line in file_object:
    a = line.split("\t")[0].split(">")[0][:-1];
    b = line.split("\t")[0].split(">")[1];
    if (a+" "+b in test_edge):continue;
    w_arr = line.split("\t")[1].split(' ')[:-1];
    arr = [];
    for w in w_arr:
        arr.append(float(w));
    if (a in docVector):
        outputOwner.write(a+"\t"+b+"\t"+str(tool.cosineSimilarity(arr,docVector[a]))+"\n");
    if (b in docVector):
        outputTarget.write(a+"\t"+b+"\t"+str(tool.cosineSimilarity(arr,docVector[b]))+"\n");
outputTarget.close();
outputOwner.close();
