#!/usr/bin/env python
# by bogard_t

import sys

usage_msg = "usage : ./deletedup.py <infile> <outfile>"

try:
    if len(sys.argv) == 3:
        lines_seen = set()
        infilename = sys.argv[1]
        outfilename = sys.argv[2]
        outfile = open(outfilename, "w")
        for line in open(infilename, "r"):
            if line not in lines_seen:
                outfile.write(line)
                lines_seen.add(line)
        outfile.close()
    else:
        raise(ValueError(usage()))
        
except Exception as e:
    print(str(e))
    exit(42)
