#!/usr/bin/env python
import sys # Load in module that accesses the command line
import fileinput
import re
import json

my_file= sys.argv[1]

for line in fileinput.input(my_file) :    
    if re.match (r'.*\s.*\sgene\s', line) :
      # print line
       columns = re.split('\t', line) 
       gene_name_matches= re.findall('gene_name \"(.*?)\";', line) 
       if columns[2] == "gene":
          if gene_name_matches:
            # print gene_name_matches[0] + "\t" +  columns[0] + "\t" + columns[3] + "\t" + columns[4] 
             print json.dumps({ "genename" : gene_name_matches[0], "chr" : columns[0], "startpos" : columns[3], "endpos" : columns[4]})

