
import string;
import re;
import math;
import random;


d2d = {};
re_d2d = {};
test_edge = {};
print("Load acl links and test links")
file_object = open('../aan_testing.tsv');
for line in file_object:
    test_edge[line[:-2]] = 1;
file_object.close();
file_object = open('../2014/acl.txt');
print("Running ... Building CitationNetwork")
output = open('../CitationNetwork/CitationNetwork.tsv','w');
outputBi = open('../CitationNetwork/CitationNetworkBi.tsv','w');
outputCNCCD = open('../CitationNetwork/CitationNetworkPlusCocitedNetwork.tsv','w');
outputCNCCG = open('../CitationNetwork/CitationNetworkPlusCocitingNetwork.tsv','w');
for line in file_object:
    line = line[:-1];
    owner = line.split(' ')[0];
    target = line.split(' ')[2];
    if ((owner+" "+target) in test_edge):
        continue;
    output.write(owner+"\t"+target+"\n");
    outputBi.write(owner+"\t"+target+"\n");
    outputBi.write(target+"\t"+owner+"\n");
    outputCNCCD.write(owner+"\t"+target+"\t1\n");
    outputCNCCD.write(target+"\t"+owner+"\t1\n");
    outputCNCCG.write(owner+"\t"+target+"\t1\n");
    outputCNCCG.write(target+"\t"+owner+"\t1\n");
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

output.close();
outputBi.close();

print("Running ... Building Co-CitedNetwork")
cocited = {};
for owner in d2d:
    for target1 in d2d[owner]:
        for target2 in d2d[owner]:
            mark = (target1+"\t"+target2);
            if (mark) in cocited:
                cocited[mark] = cocited[mark]+1;
            else:
                cocited[mark] = 1;
output = open('../CitationNetwork/CocitedNetwork.tsv','w');
for ccd in cocited:
    output.write(ccd+'\t'+str(cocited[ccd])+"\n");
    outputCNCCD.write(ccd+'\t'+str(cocited[ccd])+"\n");
output.close();
outputCNCCD.close();

print("Running ... Building Co-CitingNetwork")
cociting = {};
for target in re_d2d:
    for owner1 in re_d2d[target]:
        for owner2 in re_d2d[target]:
            mark = (owner1+"\t"+owner2);
            if (mark) in cociting:
                cociting[mark] = cociting[mark]+1;
            else:
                cociting[mark] = 1;
output = open('../CitationNetwork/CocitingNetwork.tsv','w');
for ccg in cociting:
    output.write(ccg+'\t'+str(cociting[ccg])+"\n");
    outputCNCCG.write(ccg+'\t'+str(cociting[ccg])+"\n");
outputCNCCG.close();
output.close();
