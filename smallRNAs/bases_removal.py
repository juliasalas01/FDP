#!/usr/bin/env python

import sys

input_file= sys.argv[1]
output_file= sys.argv[2]

# Open the input and output files
with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
    # Read the input file line by line
    lines = f_in.read().rstrip("\n").split("\n")
    for idx,line in enumerate(lines):
        # Check if this is the header line of a read
        if line.startswith('@'):
            header = line
            seq = lines[idx+1]
            plus = lines[idx+2]
            qual = lines[idx+3]
        
           # new_seq = ""
            #for index,l in enumerate(seq):
             #   if index >= 3 and index <= len(seq)-4:
              #      new_seq += l
            #print(len(seq)-len(new_seq))


            
            new_seq = seq[4:-4]
            new_qual= qual[4:-4]
            #for i in range(4, len(seq)-4):
             #   new_seq += seq[i]


            f_out.write(header + '\n')
            f_out.write(new_seq + '\n')
            f_out.write(plus + '\n')
            f_out.write(new_qual + '\n')
   ## print(new_seq)
            
f_out.close()
f_in.close()

