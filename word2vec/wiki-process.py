import string;
import re;
import math;
import random;

edges = {};
pattern = re.compile("[a-z]+")
file_object = open('wiki-abstract.txt')
output = open('wiki-w2v-nocase.tsv', 'w');
i = 0;
try:
    for line in file_object:
        liststr = line[10:-12];
        liststr = liststr.lower();
        wordlist = pattern.findall(liststr)
        output.write("wiki_"+str(i)+"\t");
        for word in wordlist:
            output.write(word+" ");
        output.write("\n");
        i = i + 1;
finally:
    file_object.close()
    output.close()
