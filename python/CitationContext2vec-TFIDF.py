import string;
import re;
import math;
import random;
import tool;


dictionary = tool.loadDictionary();


print("Running CitationContext2vec-TF")
print("Running CitationContext2vec-TFIDF")
pattern = re.compile("[a-z]+")
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




file_object = open('../CitationContext.tsv');
output = open('../CitationContextEmbedding/CitationContext2vec-TF.tsv','w');
preid ="";
cite2vec = {};
wordpairs = {};
for line in file_object:
    if (preid==""):
        preid = line.split("\t")[0];
        wordpairs = dealContext(line[:-1].split("\t")[3]);
    else:
        nowid = line.split("\t")[1];
        if ((preid+"=>"+nowid)in cite2vec):
            tmp = cite2vec[(preid+"=>"+nowid)];
            for word in wordpairs:
                if (word in tmp):
                    tmp[word] = tmp[word]+wordpairs[word];
                else:
                    tmp[word] = wordpairs[word];
        else:
            cite2vec[(preid+"=>"+nowid)] = wordpairs;
        preid = "";

outputTFIDF = open('../CitationContextEmbedding/CitationContext2vec-TFIDF.tsv','w');
for cite in cite2vec:
    output.write(cite+"\t");
    outputTFIDF.write(cite+"\t");
    wordpairs = cite2vec[cite];
    wordnum = 0;
    for word in wordpairs:
        output.write(word+":"+str(wordpairs[word])+" ");
        wordnum = wordnum+wordpairs[word];
    for word in wordpairs:
        outputTFIDF.write(word+":"+str(tool.TFIDF(wordpairs[word],wordnum,dictionary[word][1]))+" ");
    output.write("\n");
    outputTFIDF.write("\n");
output.close();
outputTFIDF.close();
file_object.close();
