import string;
import re;
import math;
import random;
import tool;
import sys;
dictionary = tool.loadDictionary();
print("Running ... Divide paper into sentences")
print("Running ... Building para2vec training set")

edges = {};
pattern = re.compile("[a-z]+")


def dealText(context,output,wordlist_d):
    context = context.lower();
    context, number = re.subn("[ ]+", " ", context);
    context, number = re.subn("- ", "", context);
    wordlist = pattern.findall(context)
    for word in wordlist:
        if (word in dictionary):
            output.write(word+" ");
            if (word in wordlist_d):
                wordlist_d[word] = wordlist_d[word]+1;
            else:
                wordlist_d[word] = 1;

output = open("../word2vec/papers_w2v.tsv", 'w');
#output = open("word2vec/alldata_w2v.tsv", 'w');


file_object = open('../CitationContext.tsv');
preid ="";
wordpairs = {};
Context = "";
i = 0;
for line in file_object:
    if (preid==""):
        preid = line.split("\t")[0];
        Context = line[:-1].split("\t")[3];
    else:
        nowid = line.split("\t")[1];
        output.write(preid+"=>"+nowid+">"+str(i)+"\t");
        i = i+1;
        dealText(Context,output,{});
        output.write("\n");
        preid = "";
file_object.close();

file_object = open('../2014/paper_path.txt');


print("Running ... Building documentEmbedding-TF")
print("Running ... Building documentEmbedding-TFIDF")

outputDocu = open("../DocumentEmbedding/documentEmbedding-TF.tsv", 'w');
outputDocuTFIDF = open("../DocumentEmbedding/documentEmbedding-TFIDF.tsv", 'w');
try:
    docuNum = 0;
    for file_name in file_object:
        docuNum = docuNum+1;
        if (docuNum % 100 ==0):
            sys.stdout.write("%d/26000\r"%(docuNum))
            sys.stdout.flush();
        wordlist_d  ={};
        paper_object = open(file_name[:-1]);
        docId = file_name.split("/")[-1].split('.')[0];
        para_no = 0;
        text = "";
        for line in paper_object:
            line = line.strip();
            if (len(line)<3):
                continue;
            now_text = line[:-1];
            if (now_text[-1]=='-'):
                now_text = now_text[:-1];
            if (now_text[-1]=='.'):
                text = text + now_text;
                output.write(docId+"_"+str(para_no)+"\t")
                dealText(text,output,wordlist_d);
                output.write("\n");
                text = "";
                para_no = para_no+1;
                continue;
            sepByDot = now_text.split(".");
            for i in range(len(sepByDot)):
                if (i==len(sepByDot)-1):
                    text = text + sepByDot[i];
                    continue;
                text = text + sepByDot[i] +".";
                if (len(text)>=300):
                    output.write(docId+"_"+str(para_no)+"\t")
                    dealText(text,output,wordlist_d);
                    output.write("\n");
                    text = "";
                    para_no = para_no+1;
        output.write(docId+"_"+str(para_no)+"\t")
        dealText(text,output,wordlist_d);
        output.write("\n");
        text = "";
        para_no = para_no+1;
        paper_object.close();
        outputDocu.write(docId+"\t");
        wordNum = 0;
        for word in wordlist_d:
            outputDocu.write(word+":"+str(wordlist_d[word])+" ");
            wordNum = wordNum + wordlist_d[word];
        outputDocu.write("\n");
        outputDocuTFIDF.write(docId+"\t");
        for word in wordlist_d:
            outputDocuTFIDF.write(word+":"+tool.TFIDF(wordlist_d[word],wordNum,dictionary[word][1])+" ");
        outputDocuTFIDF.write("\n");

finally:
    file_object.close()
    #output.close()

outputDocuTFIDF.close();
outputDocu.close();
output.close();
