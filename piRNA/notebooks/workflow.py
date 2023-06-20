from gwf import Workflow

gwf=Workflow()
import sys, os, re

##Functions##
#adaptor removal
def cutadapt(all_reads, filter_reads):
	inputs = [ all_reads] 
	outputs = [filter_reads]
	options = {"walltime":"8:00:00","cores":2,"memory":"30g","account":"piRNA"}
	spec = '''
	cutadapt -a TGGAATTCTCGGGTGCCAAGG -o {} {}
	'''.format(filter_reads, all_reads)
	return inputs, outputs, options, spec
#Mapping all
def mapping_all(genome_index,filter_reads,out_map_sai_all, out_map_bam_all):
	inputs = [ f'{genome_index}.amb',filter_reads] 
	outputs = [out_map_sai_all, out_map_bam_all]
	options = {"walltime":"8:00:00","cores":2,"memory":"60g","account":"piRNA"}
	spec = '''
	bwa aln -t 6 {genome_index} {filter_reads} > {out_map_sai_all}
	bwa samse -n 5000 {genome_index} {out_map_sai_all} {filter_reads} | samtools view -uS - | samtools sort -o {out_map_bam_all}
	'''.format(filter_reads=filter_reads, genome_index=genome_index, out_map_sai_all=out_map_sai_all, out_map_bam_all=out_map_bam_all)

	return inputs, outputs, options, spec
#Unique reads
def unique_reads(out_map_bam_all, out_map_unique):
	inputs = [out_map_bam_all]
	outputs = [out_map_unique]
	options = {"walltime":"02:00:00","account":"piRNA", "memory":"30gb"}
	spec = '''
	sambamba view -t 12 -h -f bam -F "mapping_quality >= 1 and not (unmapped or secondary_alignment) and not ([XA] != null or [SA] != null)" {} -o {}
	'''.format(out_map_bam_all, out_map_unique)
	return inputs, outputs, options, spec
#Multi reads
def multi_reads(out_map_bam_all, out_map_multi):
	inputs = [out_map_bam_all]
	outputs = [out_map_multi]
	options = {"walltime":"02:00:00","account":"piRNA", "memory":"30gb"}
	spec = '''
	sambamba view -t 12 -h -f bam -F "mapping_quality == 0" {} -o {}
	'''.format(out_map_bam_all, out_map_multi)
	return inputs, outputs, options, spec 

#Coverage
def coverage_multi(out_map_multi, coverage_multi):
	inputs = [out_map_multi]
	outputs = [coverage_multi] 
	options = {"walltime":"02:00:00","account":"piRNA", "memory":"30gb"}
	spec = '''
	samtools depth {} > {}
	'''.format(out_map_multi, coverage_multi)
	return inputs, outputs, options, spec 

#Coverage
def coverage_unique(out_map_unique, coverage_unique):
	inputs = [out_map_unique]
	outputs = [coverage_unique] 
	options = {"walltime":"02:00:00","account":"piRNA", "memory":"30gb"}
	spec = '''
	samtools depth {} > {}
	'''.format(out_map_unique, coverage_unique)
	return inputs, outputs, options, spec 

all_output_map="/home/juliasalas/piRNA/Workspaces/julia/zamore_lab/map"
output_coverage="/home/juliasalas/piRNA/Workspaces/julia/zamore_lab/coverage"
index="/home/juliasalas/piRNA/Workspaces/julia/PrimaryData/index/human"
reads="/home/juliasalas/piRNA/Workspaces/julia/zamore_lab/data"
output_unique="/home/juliasalas/piRNA/Workspaces/julia/zamore_lab/unique"
output_multi="/home/juliasalas/piRNA/Workspaces/julia/zamore_lab/multi"
output_coverage_unique="/home/juliasalas/piRNA/Workspaces/julia/zamore_lab/coverage_unique"
output_coverage_multi="/home/juliasalas/piRNA/Workspaces/julia/zamore_lab/coverage_multi"
cutadapt_output="/home/juliasalas/piRNA/Workspaces/julia/zamore_lab/cutadapt"
samples=["A1","A2","A3","A4","A5","A6","A7","A8","A9",
 "A10","A11","A12","A13", "A14",
 "J1_1", "J1_2","J2", "J3"]





#mapping
genome_index=f'{index}/human_index'
for sample in samples:
	#cutadapt
	all_reads=f'{reads}/{sample}.fastq'
	cutadapt_sample=f'{cutadapt_output}/{sample}'
	if not os.path.exists(cutadapt_sample):
		os.makedirs(cutadapt_sample)
	filter_reads=f'{cutadapt_sample}/{sample}_filter.fastq'
	gwf.target_from_template(f'cutadapt_{sample}',
			  cutadapt(all_reads,filter_reads))
	all_map_sample= f'{all_output_map}/{sample}'
	if not os.path.exists(all_map_sample):
		os.makedirs(all_map_sample)
	out_map_sai_all=f'{all_map_sample}/{sample}_map.sai'
	out_map_bam_all=f'{all_map_sample}/{sample}_map.bam'
	gwf.target_from_template(f'map_{sample}',
		mapping_all(genome_index,filter_reads, out_map_sai_all, out_map_bam_all))
	#unique
	unique_sample= f'{output_unique}/{sample}/'
	if not os.path.exists(unique_sample):
		os.makedirs(unique_sample)
	
	out_map_unique=f'{unique_sample}{sample}_unique.bam'
	gwf.target_from_template(f'unique_{sample}',
		unique_reads(out_map_bam_all, out_map_unique))
	
	#multi
	multi_sample= f'{output_multi}/{sample}/'
	if not os.path.exists(multi_sample):
		os.makedirs(multi_sample)
	
	out_map_multi=f'{multi_sample}{sample}_multi.bam'
	gwf.target_from_template(f'multi_{sample}',
		multi_reads(out_map_bam_all, out_map_multi))
	
	#coverage unique
	coverage_sample= f'{output_coverage_unique}/{sample}/'
	if not os.path.exists(coverage_sample):
		os.makedirs(coverage_sample)

	out_coverage_unique=f'{coverage_sample}{sample}_coverage'
	gwf.target_from_template(f'unique_coverage_{sample}',
		coverage_unique(out_map_unique, out_coverage_unique))
		
	#coverage multi
	coverage_sample_multi= f'{output_coverage_multi}/{sample}/'
	if not os.path.exists(coverage_sample_multi):
		os.makedirs(coverage_sample_multi)
	
	out_coverage_multi=f'{coverage_sample_multi}{sample}_coverage'
	gwf.target_from_template(f'multi_coverage_{sample}',
		coverage_multi(out_map_multi, out_coverage_multi))