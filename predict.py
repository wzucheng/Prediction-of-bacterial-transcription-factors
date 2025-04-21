#!/usr/bin/env python
# -*- coding: UTF-8 -*- 
import subprocess
import re
import os
import string
import sys

FASTA= sys.argv[1]
NETvocab= sys.argv[2]
region= sys.argv[3]
label_dic= sys.argv[4]
predictmodel= sys.argv[5]

string="cat ? | grep -v \">\" > seq.test.txt"
print type(string)
string2 = string.replace("?",FASTA)
val = os.system(string2)

d = open('./test.txt.tok','a+')
with open(r'seq.test.txt') as o:
    
    for line2 in o.readlines():
        line3 = re.sub(r"(?<=\w)(?=(?:\w\w)+$)", " ", line2) 
        print >> d, line3,

subprocess.call("cut -b 1 seq.test.txt > temp.test.cat ", shell = True)

with open(r'temp.test.cat') as r:
    line4=r.readlines()
with open(r'test.cat',"w+") as w:
    for l in line4:
        line5 = re.sub(r"\w", "ArgR", l)
        print >> w, line5,
        
pass

d.close()
o.close()


string3="./prep gen_regions input_fn=test vocab_fn=? region_fn_stem=test label_dic_fn=& patch_size=#"

print type(string3)
string4 = string3.replace("?",NETvocab)
string5 = string4.replace("#",region)
string6 = string5.replace("&",label_dic)

print(string6)
val = os.system(string6)


string7="./Net 0:1 predict model_fn=# prediction_fn=result.prediction tstname=test datatype=sparse data_dir=./ WriteText"
print type(string7)
string8 = string7.replace("#",predictmodel)
print(string8)
val = os.system(string8)
