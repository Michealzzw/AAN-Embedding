import string;
import re;
import math;
import random;
import tool;
dictionary = tool.loadDictionary();

document2worddict = {};
pattern = re.compile("[a-z]+")
test_edge = {};
print("Load acl links and test links")
file_object = open('../aan_testing.tsv');
for line in file_object:
    test_edge[line[:-2]] = 1;
file_object.close();
def dealContext(context):
    context = context.lower();
    context, number = re.subn("[ ]+", " ", context);
    context, number = re.subn("- ", "", context);
    wordlist = pattern.findall(context)
    worddict = {};
    for word in wordlist:
        if (word in dictionary):
            if (word in worddict):
                worddict[word] = worddict[word]+1;
            else:
                worddict[word] = 1;
    return worddict;


print("Running ... Building CitationContext2Document-TFIDF");
print("Running ... Building CitationContext2Document-TF");

file_object = open('../CitationContext.tsv');

preid ="";
wordpairs = {};
for line in file_object:
    if (preid==""):
        preid = line.split("\t")[0];
        wordpairs = dealContext(line[:-1].split("\t")[3]);
    else:
        nowid = line.split("\t")[1];
        if (preid+" "+nowid in test_edge):
            preid="";
            continue;
        if (nowid in document2worddict):
            wordpairs_merge = document2worddict[nowid];
            for word in wordpairs:
                if (word in wordpairs_merge):
                    wordpairs_merge[word] = wordpairs_merge[word] + wordpairs[word];
                else:
                    wordpairs_merge[word] = wordpairs[word];
        else:
            document2worddict[nowid] = wordpairs;
        preid = "";

file_object.close();
output = open('../CitationContext2DocumentEmbedding/CitationContext2Document-TFIDF.tsv','w');
outputTF = open('../CitationContext2DocumentEmbedding/CitationContext2Document-TF.tsv','w');

for document in document2worddict:
    output.write(document+"\t");
    outputTF.write(document+"\t");
    wordnum = 0;
    for word in document2worddict[document]:
        wordnum = wordnum + document2worddict[document][word];
        outputTF.write(word+":"+str(document2worddict[document][word])+" ");
    for word in document2worddict[document]:
        output.write(word+":"+str(tool.TFIDF(document2worddict[document][word],wordnum,dictionary[word][1]))+" ");
    output.write("\n");
    outputTF.write("\n");

"""
file_object = open('../DocumentEmbedding/document2vec-TF.tsv');
for line in file_object:
    docid = line.split("\t")[0];
    if (docid not in document2worddict):
        outputTF.write(line);
file_object.close();
file_object = open('../DocumentEmbedding/document2vec-TFIDF.tsv');
for line in file_object:
    docid = line.split("\t")[0];
    if (docid not in document2worddict):
        output.write(line);
file_object.close();
"""

output.close();
outputTF.close();
file_object.close();
