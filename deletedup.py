#!/usr/bin/env python
# by bogard_t

usage_msg = "usage : ./deletedup.py <outfile> <infile>"

try:
    if len(sys.argv) == 3:
        lines_seen = set()
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
