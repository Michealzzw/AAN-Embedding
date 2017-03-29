import string;
import re;
import math;


Id2Id = {};
Id2Title = {};
los_count = 0;
count = 0;
Link_Id2Id = {};
IDF = {};
edges = {};
docuNum = 0;
ngram = 3;

def add_edge(a,b,value):
	Link_Id2value = {};
	if (a not in Link_Id2Id):
		Link_Id2Id[a] = Link_Id2value;
	else:
		Link_Id2value = Link_Id2Id[a];
	if (b not in Link_Id2value):
		Link_Id2value[b] = value;
	else:
		Link_Id2value[b] = Link_Id2value[b]+value;



def getDictFromSens(sens):
	dic = {};
	for sen in sens:
		wl = re.split("[^a-z]+",sen.lower());
		for word in wl:
			for i in range(len(word)-ngram+1):
				ng = word[i:i+ngram];
				if (ng in dic):
					dic[ng] = dic[ng]+1.0;
				else:
					dic[ng] = 1.0;
	return dic;

def calculateSimilarity(sens1, sens2):
	dic1 = getDictFromSens(sens1);
	len1 = 0.0;
	for word in dic1:
		len1 = len1+dic1[word];
	for word in dic1:
		if (word in IDF):
			dic1[word] = IDF[word]*dic1[word]/len1;
	len1 = 0.0;
	for word in dic1:
		len1 = len1+dic1[word]*dic1[word];
	len1 = math.sqrt(len1);
	for word in dic1:
		dic1[word] = dic1[word]/len1;
	dic2 = getDictFromSens(sens2);
	len2 = 0.0;
	for word in dic2:
		len2 = len2+dic2[word];
	for word in dic2:
		if (word in IDF):
			dic2[word] = IDF[word]*dic2[word]/len2;
	len2 = 0.0;
	for word in dic2:
		len2 = len2+dic2[word]*dic2[word];
	len2 = math.sqrt(len2);
	for word in dic2:
		dic2[word] = dic2[word]/len2;

	similarity = 0.0;
	for word in dic1:
		if (word in dic2):
			similarity = similarity+dic1[word]*dic2[word];
	similarity = similarity*0.5;
	#print dic1;
	#print dic2;
	#print similarity;
	return similarity;





file_object = open('aan_testing.tsv')

try:
	for line in file_object:
		edges[line[:-1]] = 1;

finally:
	file_object.close()


file_object = open('CitationContext.tsv')

try:
	cur_id = "";
	cur_context = "";
	for line in file_object:
		list = line[:-1].split('\t');
		if (list[0]=="===>Match" and (cur_id+" "+list[1]) not in edges):
			Id2Context = {};
			if (cur_id not in Id2Id):
				Id2Id[cur_id] = Id2Context;
			else: Id2Context = Id2Id[cur_id];
			cur_cita_cont = [];
			if (list[1] not in Id2Context):
				Id2Context[list[1]] = cur_cita_cont;
			else:
				cur_cita_cont = Id2Context[list[1]];
			cur_cita_cont.append(cur_context);
		else:
			cur_id = list[0];
			cur_context = list[3];
finally:
	file_object.close()

file_object = open('2014/acl-metadata.txt')
try:
	cur_id="";
	for line in file_object:
		list = line[:-1].split(' ');
		if (list[0]=="id"):
			cur_id = list[2][1:-1];
		else:
			if (list[0]=="title"):
				Id2Title[cur_id] = line[9:-2];
				#print line;
				#print cur_id;
				#print line[9:-2]
finally:
	file_object.close()
#file_object = open('release/2013/acl.txt')
file_object = open('2014/acl.txt')

try:
	for line in file_object:
		list = line[:-1].split(' ==> ');
		Id2Context = {};
		if (list[0] in Id2Id):
			Id2Context = Id2Id[list[0]];
		else:
			Id2Id[list[0]] = Id2Context;
		cur_cita_cont = [];
		count = count+1;
		if (list[1] not in Id2Context and (list[0]+" "+list[1])not in edges):
			los_count = los_count+1;
			Id2Context[list[1]] = cur_cita_cont;
			#if (list[1] in Id2Title):
			#	cur_cita_cont.append(Id2Title[list[1]]);

finally:
	file_object.close()

print los_count;
print count;


for id1 in Id2Id:
	for id2 in Id2Id[id1]:
		if (len(Id2Id[id1][id2])):
			docuNum = docuNum+1.0;
			dic = getDictFromSens(Id2Id[id1][id2]);
			for key in dic:
				if (key in IDF):
					IDF[key] = IDF[key]+1.0;
				else:
					IDF[key] = 1.0;

for word in IDF:
	#print IDF[word]
	#print word+":"+str(math.log(docuNum/(IDF[word]+1.0)))
	IDF[word] = math.log(docuNum/(IDF[word]+1.0));
output = open('aan_processingCitationWithContext.tsv', 'w');
for id1 in Id2Id:
	for id2 in Id2Id[id1]:
		for id3 in Id2Id[id1]:
			if (id2!=id3):
				if (len(Id2Id[id1][id2]) and len(Id2Id[id1][id3])):
					add_edge(id2,id3,calculateSimilarity(Id2Id[id1][id2],Id2Id[id1][id3]));
					add_edge(id3,id2,calculateSimilarity(Id2Id[id1][id2],Id2Id[id1][id3]));
				else:
					add_edge(id2,id3,0.1);
				add_edge(id3,id2,0.1);
	for id2 in Id2Id[id1]:
		contexts = Id2Id[id1][id2];
		output.write(id1+'\t'+id2);
		for context in contexts:
			output.write("\t"+context);
		output.write("\n");
output.close()

output = open('aan_CitationNetwork.tsv', 'w');
for id1 in Id2Id:
	for id2 in Id2Id[id1]:
		output.write(id1+'\t'+id2+"\t"+str(1)+"\n");
		output.write(id2+'\t'+id1+"\t"+str(1)+"\n");
output.close()



output = open('aan_WeightSimilarityCitationNetworkPlus.tsv', 'w');
#output = open('aan_WeightCitationNetworkPlus.tsv', 'w');
for id1 in Id2Id:
	for id2 in Id2Id[id1]:
		output.write(id1+'\t'+id2+"\t"+str(1)+"\n");
		output.write(id2+'\t'+id1+"\t"+str(1)+"\n");
for id1 in Link_Id2Id:
	for id2 in Link_Id2Id[id1]:
		value = Link_Id2Id[id1][id2];
		output.write(id1+'\t'+id2+"\t"+str(value)+"\n");
		output.write(id2+'\t'+id1+"\t"+str(value)+"\n");
output.close()
