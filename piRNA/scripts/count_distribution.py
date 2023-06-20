import sys
import gzip


input_file= sys.argv[1]

counts= {}
with open(input_file,"rt") as i:
    lines = i.read().rstrip("\n").split("\n")
	#we use enumerate to keep the cont of the iterations
    for index,line in enumerate(lines):
        #see if there is a starting read
        if line.startswith("@"):
            read_length = len(lines[index+1])
            if read_length in counts:
                counts[read_length] += 1
            else:
                counts[read_length] = 1
    print(counts.keys())
    print(counts.values())

i.close()
