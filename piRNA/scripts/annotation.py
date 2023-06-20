import sys
import pandas as pd


#Define in the terminal the input and the output files
input_file= sys.argv[1]

types={}
with open(input_file,"rt") as i:
    content = i.read().rstrip("\n").split("\n")
    for line in content:
        elems = line.split("\t")
        #print(elems)
        #print(elems[3])
        type = elems[3].split('gene_biotype ')[1].split(";")[0]
        if type in types:
            types[type] += 1
        else:
           types[type] = 1
    print(types)
    print(types.keys())
    print(types.values())
i.close()

#df= pd.DataFrame({ types = np.array(list(types.keys()))})
#df.to_csv("Hum1_annotation.tsv",sep="\t")
