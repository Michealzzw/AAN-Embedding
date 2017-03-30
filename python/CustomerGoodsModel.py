import string;
import re;
import math;
import random;
import tool;



cceFile = "../CitationContextEmbedding/CitationContext2vec-Para2vec.tsv";
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

cocitingArr = [];
print("Load co-citing network")
file_object = open('../CitationNetwork/CocitingNetwork.tsv');
for line in file_object:
    a = line.split("\t")[0];
    b = line.split("\t")[1];
    if (a>b):
        continue;
    cocitingArr.append(a+'\t'+b);
file_object.close();


file_object = open(cceFile);
print "Load Cites Embedding"
Cites = {};
for line in file_object:
    cite = line.split("\t")[0];
    arr = [];
    for dim in line.split("\t")[1].split(" ")[:-1]:
        arr.append(float(dim));
    if (len(arr)>0):
        Cites[cite] = arr;
file_object.close();

print("Running ... Building CustomerGoodsModel");
print("Running ... Building Goods-Based Quantity Quality Balance");

outputQT = open(ccsnPath+"Goods-Based-Quantity.tsv",'w');
outputQL = open(ccsnPath+"Goods-Based-Quality.tsv",'w');
outputBA = open(ccsnPath+"Goods-Based-Balance.tsv",'w');

for cocited in cocitedArr:
    a = cocited.split("\t")[0];
    b = cocited.split("\t")[1];
    edge_sum = 0.0;
    co_num = 0;
    for owner in re_d2d[a]:
        if (owner in re_d2d[b]):co_num = co_num+1;
        if (owner in re_d2d[b] and (owner+"=>"+a) in Cites and (owner+"=>"+b) in Cites):
            edge_sum = edge_sum + tool.cosineSimilarity(Cites[(owner+"=>"+a)],Cites[(owner+"=>"+b)]);
    qt = co_num / math.log(len(re_d2d[a])+len(re_d2d[b])+2);
    ql = edge_sum / co_num;
    ba = edge_sum / math.log(len(re_d2d[a])+len(re_d2d[b])+2)
    outputQL.write(cocited+"\t"+str(ql)+"\n");
    outputQT.write(cocited+"\t"+str(qt)+"\n");
    outputBA.write(cocited+"\t"+str(ba)+"\n");
outputBA.close();
outputQT.close();
outputQL.close();


print("Running ... Building Customer-Based Quantity Quality Balance");

outputQT = open(ccsnPath+"Customer-Based-Quantity.tsv",'w');
outputQL = open(ccsnPath+"Customer-Based-Quality.tsv",'w');
outputBA = open(ccsnPath+"Customer-Based-Balance.tsv",'w');

for cociting in cocitingArr:
    a = cociting.split("\t")[0];
    b = cociting.split("\t")[1];
    edge_sum = 0.0;
    co_num = 0;
    for target in d2d[a]:
        if (target in d2d[b]):co_num = co_num+1;
        if (target in d2d[b] and (a+"=>"+target) in Cites and (b+"=>"+target) in Cites):
            edge_sum = edge_sum + tool.cosineSimilarity(Cites[(a+"=>"+target)],Cites[(b+"=>"+target)]);
    qt = co_num / math.log(len(d2d[a])+len(d2d[b])+2);
    ql = edge_sum / co_num;
    ba = edge_sum / math.log(len(d2d[a])+len(d2d[b])+2)
    outputQL.write(cociting+"\t"+str(ql)+"\n");
    outputQT.write(cociting+"\t"+str(qt)+"\n");
    outputBA.write(cociting+"\t"+str(ba)+"\n");
outputBA.close();
outputQT.close();
outputQL.close();
