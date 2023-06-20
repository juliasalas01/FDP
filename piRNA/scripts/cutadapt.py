#define a function to filter the reads by removing the 3' and 5' adaptors
#Also remove the poly-A tails and sequences with error rates
import sys, os


input_file=sys.argv[1]
output_file=sys.argv[2]

cutadapt -a AGATCGGAAGAGCACACGTCT -g GTTCAGAGTTCTACAGTCCGACGATC -o output_file input_file 

def cutadapt(raw_data, quality_filter):
    inputs=[raw_data]
    outputs=[quality_filter]
    cutadapt --max-n 0.10 -a AGATCGGAAGAGCACACGTCT -g GTTCAGAGTTCTACAGTCCGACGATC {} | cutadapt -a A{{100}} --no-indels -e 0.16666666666666666 -o {} -

    return inputs, outputs


for sequences in 1 2 3 4 5;
do{
    echo "# First filtering "
    cutadapt -a AGATCGGAAGAGCACACGTCT -g GTTCAGAGTTCTACAGTCCGACGATC {} | cutadapt -a A{{100}} --no-indels -e 0.16666666666666666 -o {} 
    -o output.fq.gz \
    
}; done;

cutadapt -a AGATCGGAAGAGCACACGTCT -g GTTCAGAGTTCTACAGTCCGACGATC --no-indels -e 0.16666666666666666  --max-n 0.10  -o out_samson.fq.gz Samson.fq.gz 
