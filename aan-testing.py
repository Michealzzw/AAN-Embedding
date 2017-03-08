import string;
import re;
import math;
import random;


cn_id2vec = {};
edges = {};

def similarity(vec1,vec2,minvalue=100.0):
	dist = 0.0;
	for i in range(len(vec1)):
		dist = dist + (vec1[i]-vec2[i])*(vec1[i]-vec2[i])
		if (dist>minvalue):
			break;
	return dist;


#file_object = open('vec-2nd-samples10-CitationNetwork.tsv')
#file_object = open('vec-1st-samples10-CitationNetwork.tsv')
#file_object = open('vec-1st-CitationNetwork.tsv')
#file_object = open('vec-2nd-CitationNetwork.tsv')
file_object = open('vec-1st-weightSimilarityCitationNetwork.tsv')
#file_object = open('vec-1st-weightCitationNetwork.tsv')


try:	
	for line in file_object:
		list = line[:-1].split(' ');
		vec = [];
		for key in list[1:-1]:
			#print key
			vec.append(string.atof(key));
		if (len(vec)>1):
			cn_id2vec[list[0]] = vec;

finally:
	file_object.close()

file_object = open('aan_testing.tsv')
output = open('result_CitationNetwork.tsv', 'w');
try:	
	count = 0;
	for line in file_object:
		count = count+1;
		if (count %100==0):
			print count;
		list = line[:-1].split(' ');
		if (list[0] not in cn_id2vec or list[1] not in cn_id2vec):
			output.write(list[0]+"\t"+list[1]+"\t-1\n");
			print (list[0]+"\t"+list[1]+"\t-1\n");
		else:
			dist = similarity(cn_id2vec[list[0]],cn_id2vec[list[1]]);
			rank = 0;
			for vec in cn_id2vec:
				if (similarity(cn_id2vec[vec],cn_id2vec[list[0]],dist)<dist):
					rank = rank+1;
			output.write(list[0]+"\t"+list[1]+"\t"+str(rank)+"\n");
			print (list[0]+"\t"+list[1]+"\t"+str(rank)+"\n");

finally:
	file_object.close()
	output.close();