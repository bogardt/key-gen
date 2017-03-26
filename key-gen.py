#!/usr/bin/env python

import sys
import random
import string
from random import choice

usage_msg="""usage : ./key-gen.py
-l for lower alpha
-l1 for lower alpha/num
-U for upper alpha
-U1 for upper alpha/num
-lU1 for lower/upper alpha/num"""

def     usage():
    print(usage_msg)
    exit(42)

def     keyGen():
    while True :
        try:
            res = ''.join(random.sample(char_set, int(key_len)))
            print (res)
        except (KeyboardInterrupt):
            exit(42)

args = sys.argv[1:]
if len(sys.argv) == 3:
    key_len = sys.argv[2]

try:
    if args:
        for arg in args:
            if int(key_len) <= 0:
                raise(ValueError("Key len must be > 0"))
            if arg == '-l':
                char_set = string.ascii_lowercase
                keyGen()
            elif arg == '-l1':
                char_set = string.ascii_lowercase + string.digits
                keyGen()
            elif arg == 'U':
                char_set = string.ascii_uppercase
                keyGen()
            elif arg == '-U1':
                char_set = string.ascii_uppercase + string.digits
                keyGen()
            elif arg == '-lU1':
                char_set = string.ascii_letters + string.digits
                keyGen()
            else:
                raise(ValueError(usage()))
    else:
        raise(ValueError(usage()))

except Exception as e:
    print(str(e))
    exit(42)
