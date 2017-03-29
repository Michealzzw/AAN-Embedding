import string;
import re;
import math;
import random;

edges = {};

file_object = open('release/2013/acl.txt')

try:	
	for line in file_object:
		list = line[:-1].split(' ==> ');
		if (random.random()<0.01):
			edges[list[0]+" "+list[1]]	= 1;

finally:
	file_object.close()

output = open('aan_testing.tsv', 'w');
for key in edges:
	output.write(key+"\n");
output.close()
