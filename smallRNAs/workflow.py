from gwf import Workflow

gwf=Workflow()
import sys, os, re

##Functions##

#M4, Mo3
def adapter1(raw_data_sample,adaptors,trimming_sample):
    inputs = [raw_data_sample,adaptors]
    outputs = [f'{trimming_sample}.fastq']
    options = {"walltime":"02:00:00","account":"piRNA"}
    spec = '''
    flexbar -r {} -a {} -t {} 
    '''.format(raw_data_sample,adaptors,trimming_sample)
    return inputs, outputs, options, spec
#Neb sample1
def adapter2(raw_data_sample_1,adaptors,trimming_sample):
    inputs = [raw_data_sample_1,adaptors]
    outputs = [f'{trimming_sample}.fastq']
    options = {"walltime":"02:00:00","account":"piRNA"}
    spec = '''
    flexbar -r {} -a {} -t {} 
    '''.format(raw_data_sample_1,adaptors,trimming_sample)
    return inputs, outputs, options, spec
#Neb sample2
def adapter3(raw_data_sample_2,adaptors,trimming_sample):
    inputs = [raw_data_sample_2,adaptors]
    outputs = [f'{trimming_sample}.fastq']
    options = {"walltime":"02:00:00","account":"piRNA"}
    spec = '''
    flexbar -r {} -a {} -t {} 
    '''.format(raw_data_sample_2,adaptors,trimming_sample)
    return inputs, outputs, options, spec
#Next 4 nucleotides removal
def removal(trimming_sample,cliped_bases):
    inputs = [trimming_sample]
    outputs = [cliped_bases]
    options = {"walltime":"02:00:00","account":"piRNA"}
    spec = '''
    python /home/juliasalas/smallRNAs/julia/scripts/bases_removal.py {} {} 
    '''.format(trimming_sample,cliped_bases)
    return inputs, outputs, options, spec

    

def mapping_short(genome_index,all_reads,out_map_sai_all, out_map_bam_all):
	inputs = [ f'{genome_index}.amb',all_reads] 
	outputs = [out_map_sai_all, out_map_bam_all]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
    bwa aln -t 6 {genome_index} {all_reads} > {out_map_sai_all}
	bwa samse -n 5000 {genome_index} {out_map_sai_all} {all_reads} | samtools view -uS - | samtools sort -o {out_map_bam_all}
	'''.format(all_reads=all_reads, genome_index=genome_index, out_map_sai_all=out_map_sai_all, out_map_bam_all=out_map_bam_all)

	return inputs, outputs, options, spec
def mapping_long(genome_index,all_reads,out_map_sai_all, out_map_bam_all):
	inputs = [ f'{genome_index}.amb',all_reads] 
	outputs = [out_map_sai_all, out_map_bam_all]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	bwa aln -t 6 {genome_index} {all_reads} > {out_map_sai_all}
	bwa samse -n 5000 {genome_index} {out_map_sai_all} {all_reads} | samtools view -uS - | samtools sort -o {out_map_bam_all}
	'''.format(all_reads=all_reads, genome_index=genome_index, out_map_sai_all=out_map_sai_all, out_map_bam_all=out_map_bam_all)

	return inputs, outputs, options, spec



#Files

raw_data= "/home/juliasalas/smallRNAs/julia/"
trim_data= "/home/juliasalas/smallRNAs/julia/trimmed/"
short_output="/home/juliasalas/smallRNAs/julia/short/"
long_output="/home/juliasalas/smallRNAs/julia/long/"
index="/home/juliasalas/piRNA/Workspaces/julia/PrimaryData/index/human"
cliped_bases="/home/juliasalas/smallRNAs/julia/trimmed"

adaptor_m4_mo3_next = {
	"M4":["1","2"],"Mo3":["1","2"],"C2_Next":["1","2"], "G2_Next":["1","2"]
} 
for type,samples in adaptor_m4_mo3_next.items():
    for sample in samples:
        raw_data_sample=f'{raw_data}{type}/{sample}.fq'
        adaptors=f'{raw_data}{type}/adaptor.fa'
        trimming_sample=f'{trim_data}{type}/{sample}_trimmed'
        if not os.path.exists(trimming_sample):
            os.makedirs(trimming_sample)
        gwf.target_from_template(f'adaptor_{sample}_{type}',
            adapter1(raw_data_sample,adaptors,trimming_sample))

adaptor_neb_1 = ["C2_Neb", "G2_Neb"]
for type in adaptor_neb_1:
    raw_data_sample_1=f'{raw_data}{type}/1.fq'
    adaptors=f'{raw_data}{type}/adaptor1.fa'
    trimming_sample=f'{trim_data}{type}/1_trimmed'
    if not os.path.exists(trimming_sample):
        os.makedirs(trimming_sample)
    gwf.target_from_template(f'adaptor_1_{type}',
        adapter2(raw_data_sample_1,adaptors,trimming_sample))

adaptor_neb_2 = ["C2_Neb", "G2_Neb"]
for type in adaptor_neb_2:
    raw_data_sample_2=f'{raw_data}{type}/2.fq'
    adaptors=f'{raw_data}{type}/adaptor2.fa'
    trimming_sample=f'{trim_data}{type}/2_trimmed'
    if not os.path.exists(trimming_sample):
        os.makedirs(trimming_sample)
    gwf.target_from_template(f'adaptor_2_{type}',
        adapter3(raw_data_sample_2,adaptors,trimming_sample))


#short reads mapping
reads_short="/home/juliasalas/smallRNAs/julia/short/"
reads_long="/home/juliasalas/smallRNAs/julia/long/"
all_output_map_short="/home/juliasalas/smallRNAs/julia/short/map/"
short_sample="/home/juliasalas/smallRNAs/julia/short/"
all_output_map_long="/home/juliasalas/smallRNAs/julia/long/map/"
all= {"M4":["1","2"],"Mo3":["1","2"],"C2_Neb":["1","2"],"G2_Neb":["1","2"]}
for type,samples in all.items():
    for sample in samples:
        #short
        genome_index=f'{index}/human_index'
        all_reads=f'{reads_short}{type}/{type}_{sample}_filter.fastq'
        all_map_sample= f'{all_output_map_short}{type}'
        if not os.path.exists(all_map_sample):
            os.makedirs(all_map_sample)
        out_map_sai_all=f'{all_map_sample}/{sample}_map.sai'
        out_map_bam_all=f'{all_map_sample}/{sample}_map.bam'
        gwf.target_from_template(f'map_{type}_{sample}',
            mapping_short(genome_index,all_reads, out_map_sai_all, out_map_bam_all))
        #long
        all_reads=f'{reads_long}{type}/{type}_{sample}_filter.fastq'
        all_map_sample= f'{all_output_map_long}{type}'
        if not os.path.exists(all_map_sample):
            os.makedirs(all_map_sample)
        out_map_sai_all=f'{all_map_sample}/{sample}_map.sai'
        out_map_bam_all=f'{all_map_sample}/{sample}_map.bam'
        gwf.target_from_template(f'map_long_{type}_{sample}',
            mapping_long(genome_index,all_reads, out_map_sai_all, out_map_bam_all))


#short
genome_index=f'{index}/human_index'
all_reads=f'{reads_short}C2_Next/C2_Next_1_filter.fastq'
all_map_sample= f'{all_output_map_short}C2_Next'
if not os.path.exists(all_map_sample):
    os.makedirs(all_map_sample)
out_map_sai_all=f'{all_map_sample}/1_map.sai'
out_map_bam_all=f'{all_map_sample}/1_map.bam'
gwf.target_from_template(f'map_short_C2_Next_1',
    mapping_short(genome_index,all_reads, out_map_sai_all, out_map_bam_all))
     

#short
genome_index=f'{index}/human_index'
all_reads=f'{reads_short}G2_Next/G2_Next_1_filter.fastq'
all_map_sample= f'{all_output_map_short}G2_Next'
if not os.path.exists(all_map_sample):
    os.makedirs(all_map_sample)
out_map_sai_all=f'{all_map_sample}/1_map.sai'
out_map_bam_all=f'{all_map_sample}/1_map.bam'
gwf.target_from_template(f'map_short_G2_Next_1',
    mapping_short(genome_index,all_reads, out_map_sai_all, out_map_bam_all))

 #long
all_reads=f'{reads_long}C2_Next/C2_Next_2_long.fastq'
all_map_sample= f'{all_output_map_long}C2_Next'
if not os.path.exists(all_map_sample):
    os.makedirs(all_map_sample)
out_map_sai_all=f'{all_map_sample}/2_map.sai'
out_map_bam_all=f'{all_map_sample}/2_map.bam'
gwf.target_from_template(f'map_long_C2_Next_2',
    mapping_long(genome_index,all_reads, out_map_sai_all, out_map_bam_all))