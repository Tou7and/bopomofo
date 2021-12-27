#!/usr/bin/env python3

import os
import subprocess as sp
import json
import sys
words = {}
words[""] = ""

def load(filename):
    tmp_words = json.loads(open(filename).read())
    words.update(tmp_words)
    
directory = os.path.dirname(os.path.realpath(__file__))
for root, dirnames, filenames in os.walk("./data/dict"):
    for filename in filenames:
        load('./data/dict/{}'.format(filename))

try:
    load('./extension.dictxtension.dict')
except:
    pass

with open("data/words.json", "w") as writer:
    json.dump(words, writer)

