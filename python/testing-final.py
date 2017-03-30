import string;
import re;
import math;
import random;
import tool;
import sys;

metrics = [2,5,10,20,50,100];
output = open("result.tsv",'w');
output.write("result_name\t")
for metric in metrics:
    output.write("recall@"+str(metric)+"\t");
output.write("not_found_num\ttotal\n");
file_path_object = open("result_path.txt");
for file_path in file_path_object:
    file_path = file_path[:-1];
    res = [];
    nf = 0;
    for metric in metrics:res.append(0);
    file_object = open(file_path);
    result_name = file_path.split("/")[-1].split(".")[0];
    output.write(result_name+"\t");
    e_num = 0;
    for line in file_object:
        e_num = e_num+1;
        line = line[:-1];
        if (len(line.split("\t"))<3):continue;
        rank = int(line.split("\t")[2]);
        if (rank==-1):nf = nf +1;
        else:
            for i in range(len(metrics)):
                if (rank<=metrics[i]):
                    res[i] = res[i]+1;
    for i in range(len(metrics)):
        output.write("%lf\t"%(res[i]*1.0/e_num));
    output.write(str(nf)+"\t"+str(e_num)+"\n");

output.close();
file_path_object.close();
