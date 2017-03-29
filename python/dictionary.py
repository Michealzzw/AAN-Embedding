import string;
import re;
import math;
import random;
import sys;
dictTF = {};
dictIDF = {};
dictIDFID = {};
pattern = re.compile("[a-zA-Z]+")


print("Running ... Building dictionary");

def addDict(text):
    text = text.lower();
    wordlist = pattern.findall(text)
    for word in wordlist:
        if (word in dictTF):
            dictTF[word] = dictTF[word]+ 1;
            if (dictIDFID[word]!=docId):
                dictIDF[word] = dictIDF[word]+1;
                dictIDFID[word] = docId;
        else:
            dictTF[word] = 1;
            dictIDFID[word] = docId;
            dictIDF[word] = 1;

file_object = open('../2014/paper_path.txt');
output = open("../dictionary.tsv", 'w');
#output = open("word2vec/papers_w2v.tsv", 'w');
try:
    docuNum = 0;
    for file_name in file_object:
        docuNum = docuNum+1;
        if (docuNum % 100 ==0):
            sys.stdout.write("%d wordNum: %d\r"%(docuNum,len(dictTF)))
            sys.stdout.flush();
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
                addDict(text);
                text = "";
                continue;
            sepByDot = now_text.split(".");
            for i in range(len(sepByDot)):
                if (i==len(sepByDot)-1):
                    text = text + sepByDot[i];
                    continue;
                text = text + sepByDot[i] +".";
                if (len(text)>=300):
                    addDict(text)
                    text = "";

        addDict(text);
        text = "";
        para_no = para_no+1;
        paper_object.close();
finally:
    file_object.close()
    #output.close()


for word in dictTF:
    if (dictTF[word]>=50 and dictIDF[word]>=2):
        output.write(word+" "+str(dictTF[word])+" "+str((1.0*dictIDF[word])/docuNum)+"\n");

output.close();
