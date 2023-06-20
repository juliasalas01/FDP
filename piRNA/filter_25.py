import sys
import gzip

#Define in the terminal the input and the output files
input_file= sys.argv[1]
output_file= sys.argv[2]

#We are going to write the filtered sequences in the output file
with gzip.open(output_file, "wt") as o:
    #We are going to read the input file sequences
	with gzip.open(input_file,"rt") as i:
        #Read each line. rstrip removes the final space of the end of the string.And split separates the string into a list of characters separated by an space 
		lines = i.read().rstrip("\n").split("\n")
		#we use enumerate to keep the cont of the iterations
		for index,line in enumerate(lines):
            #see if there is a starting read
			if line.startswith("@"):
                #look at the size of the read
				read_length = len(lines[index+1])
                #write it in the output file if the size is between 26 and 30
				if read_length==25:
					o.write(line + "\n")
					o.write(lines[index+1] + "\n")
					o.write(lines[index+2] + "\n")
					o.write(lines[index+3] + "\n")
	i.close()
o.close()
