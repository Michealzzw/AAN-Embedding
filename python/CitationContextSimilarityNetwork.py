import string;
import re;
import math;
import random;
import tool;



ccePath = "../CitationContextEmbedding/"
ccsnPath = "../CitationContextSimilarityNetwork/"

d2d = {};
re_d2d = {};
test_edge = {};
print("Load acl links and test links")
file_object = open('../aan_testing.tsv');
for line in file_object:
    test_edge[line[:-2]] = 1;
file_object.close();
file_object = open('../2014/acl.txt');
for line in file_object:
    line = line[:-1];
    owner = line.split(' ')[0];
    target = line.split(' ')[2];
    if ((owner+" "+target) in test_edge):
        continue;
    tset = {};
    if (owner not in d2d):
        d2d[owner] = tset;
    else:
        tset = d2d[owner];
    tset[target] = 1;
    oset = {};
    if (target not in re_d2d):
        re_d2d[target] = oset;
    else:
        oset = re_d2d[target];
    oset[owner] = 1;

file_object.close();

cocitedArr = [];
print("Load co-cited network")
file_object = open('../CitationNetwork/CocitedNetwork.tsv');
for line in file_object:
    a = line.split("\t")[0];
    b = line.split("\t")[1];
    if (a>b):
        continue;
    cocitedArr.append(a+'\t'+b);
file_object.close();


suffixs = ["Word2vec", "Para2vec"];
for suffix in suffixs:
    Cites = {};
    print("Running ... Building CitationContextSimilarityNetwork-Cocited-"+suffix);
    file_object = open(ccePath+"CitationContext2vec-"+suffix+".tsv");
    output = open(ccsnPath+"CitationContextSimilarityNetwork-Cocited-"+suffix+".tsv",'w');
    for line in file_object:
        cite = line.split("\t")[0];
        arr = [];
        for dim in line.split("\t")[1].split(" ")[:-1]:
            arr.append(float(dim));
        if (len(arr)>0):
            Cites[cite] = arr;

    file_object.close();
    for cocited in cocitedArr:
        a = cocited.split("\t")[0];
        b = cocited.split("\t")[1];
        edge_sum = 0.0;
        for owner in re_d2d[a]:
            if (owner in re_d2d[b] and (owner+"=>"+a) in Cites and (owner+"=>"+b) in Cites):
                edge_sum = edge_sum + tool.cosineSimilarity(Cites[(owner+"=>"+a)],Cites[(owner+"=>"+b)]);
        output.write(cocited+"\t"+str(edge_sum)+"\n");
    output.close();

suffix = "TFIDF";
Cites = {};
print("Running ... Building CitationContextSimilarityNetwork-Cocited-"+suffix);
file_object = open(ccePath+"CitationContext2vec-"+suffix+".tsv");
output = open(ccsnPath+"CitationContextSimilarityNetwork-Cocited-"+suffix+".tsv",'w');
for line in file_object:
    cite = line.split("\t")[0];
    wl = {};
    for dim in line.split("\t")[1].split(" ")[:-1]:
        wl[dim.split(':')[0]] = float(dim.split(':')[1]);
    if (len(wl)>0):
        Cites[cite] = wl;
file_object.close();
for cocited in cocitedArr:
    a = cocited.split("\t")[0];
    b = cocited.split("\t")[1];
    edge_sum = 0.0;
    for owner in re_d2d[a]:
        if (owner in re_d2d[b] and (owner+"=>"+a) in Cites and (owner+"=>"+b) in Cites):
            edge_sum = edge_sum + tool.tfidfSimilarity(Cites[(owner+"=>"+a)],Cites[(owner+"=>"+b)]);
    if (edge_sum<0.0001):
        continue;
    if (edge_sum>tool.MAX_WEIGHT) edge_sum = tool.MAX_WEIGHT;
    output.write(cocited+"\t"+str(edge_sum)+"\n");
output.close();
