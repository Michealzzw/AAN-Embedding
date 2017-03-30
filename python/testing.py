import string;
import re;
import math;
import random;
import tool;
import sys;


print("Start Testing")
print("Load Test Edges")
test_edge = [];
file_object = open('../aan_testing.tsv')
for line in file_object:
    line = line[:-2];
    test_edge.append([line.split(" ")[0],line.split(" ")[1]]);
file_object.close();


file_path_object = open("embedding_path.txt");
for file_path in file_path_object:
    file_path = file_path[:-1];
    embedding_name = file_path.split("/")[-1].split(".")[0];
    print("Running ... Test "+embedding_name);
    file_object = open(file_path);
    vectors = {};
    type_e = 0;
    if ("-vec" in embedding_name):
        type_e = 2;
    for line in file_object:
        if (len(line)<12):continue;
        if ("\t" not in line):
            docid = line.split(" ")[0];
            w_arr = line.split(" ")[1:-1];
        else:
            docid = line.split("\t")[0];
            w_arr = line.split("\t")[1].split(' ')[:-1];
        if (len(w_arr)<1):
            continue;
        if (':' in w_arr[0]):
            type_e = 1;
            wl = {};
            w_sum = 0.0;
            for w_p in w_arr:
                wl[w_p.split(":")[0]] = float(w_p.split(":")[1]);
                w_sum = w_sum + float(w_p.split(":")[1])*float(w_p.split(":")[1]);
            w_sum = math.sqrt(w_sum);
            for w in wl:
                wl[w] = wl[w] / w_sum;
            vectors[docid] = wl;
        else:
            arr = [];
            w_sum = 0.0;
            for dim in w_arr:
                w_sum = w_sum + float(dim)*float(dim);
                arr.append(float(dim));
            w_sum = math.sqrt(w_sum);
            if (type_e==0):
                for i in range(len(arr)):
                    arr[i] = arr[i]/w_sum;
            vectors[docid] = arr;
    if (type_e==0):print "type : p2v,w2v";
    if (type_e==1):print "type : tfidf";
    if (type_e==2):print "type : line";


    #   type_e:
    #   0 : p2v, w2v
    #   1 : TFIDF
    #   2 : LINE
    #

    file_object.close();
    output = open('../Result/result-'+embedding_name+'.tsv','w');
    edgeNum = 0;

    for edge in test_edge:
        edgeNum = edgeNum+1;
        if (edgeNum % 10 == 0):
            sys.stdout.write("%d/%d\r"%(edgeNum,len(test_edge)))
            sys.stdout.flush();
        a = edge[0];
        b = edge[1];
        if (a not in vectors or b not in vectors):
            output.write(a+"\t"+b+"\t-1\n");
        else:
            vec_owner = vectors[a];
            if (type_e == 1):
                dist = tool.norm_tfidfSimilarity(vec_owner,vectors[b]);
                rank = 0;
                for vec in vectors:
                    if (tool.norm_tfidfSimilarity(vec_owner,vectors[vec])>dist):
                        rank = rank+1;
                output.write(a+"\t"+b+"\t"+str(rank)+"\n");
            else:
                if (type_e == 0):
                    dist = tool.norm_cosineSimilarity(vec_owner,vectors[b]);
                    rank = 0;
                    for vec in vectors:
                        if (tool.norm_cosineSimilarity(vec_owner,vectors[vec])>dist):
                            rank = rank+1;
                    output.write(a+"\t"+b+"\t"+str(rank)+"\n");
                else:
                    dist = tool.lineSimilarity(vec_owner,vectors[b]);
                    rank = 0;
                    for vec in vectors:
                        if (tool.lineSimilarity(vec_owner,vectors[vec])<dist):
                            rank = rank+1;
                    output.write(a+"\t"+b+"\t"+str(rank)+"\n");
    output.close();



file_path_object.close();
