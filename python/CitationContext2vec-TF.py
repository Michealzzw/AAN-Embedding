import string;
import re;
import math;
import random;
import tool;


dictionary = tool.loadDictionary();


print("Running CitationContext2vec-TF")
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
output = open('../CitationContextEmbedding/CitationContext-TF.tsv','w');
preid ="";
wordpairs = {};
for line in file_object:
    if (preid==""):
        preid = line.split("\t")[0];
        wordpairs = dealContext(line[:-1].split("\t")[3]);
    else:
        nowid = line.split("\t")[1];
        output.write(preid+"\t"+nowid+"\t");
        for word in wordpairs:
            output.write(word+":"+str(wordpairs[word])+" ");
        output.write("\n");
        preid = "";
output.close();
file_object.close();
