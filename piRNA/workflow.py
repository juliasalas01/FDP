from gwf import Workflow

gwf=Workflow()
import sys, os, re

#Cutadapt filtering
def cutadapt(reads_raw,reads_flt):
	inputs = [reads_raw]
	outputs = [reads_flt]
	options = {"walltime":"02:00:00","account":"piRNA"}
	spec = '''
	cutadapt -a AGATCGGAAGAGCACACGTCT -g GTTCAGAGTTCTACAGTCCGACGATC --no-indels -e 0.16666666666666666  --max-n 0.10  -o {} {}
	'''.format(reads_flt,reads_raw)
	return inputs, outputs, options, spec

#Mapping the reads into the genome
def mapping(genome_index,reads_flt, out_map_sai, out_map_bam):
	inputs = [ f'{genome_index}.amb',reads_flt] 
	outputs = [out_map_sai, out_map_bam]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	bwa aln -t 6 {genome_index} {reads_flt} > {out_map_sai}
	bwa samse -n 5000 {genome_index} {out_map_sai} {reads_flt} | samtools view -uS - | samtools sort -o {out_map_bam}
	'''.format(reads_flt=reads_flt, genome_index=genome_index, out_map_sai=out_map_sai, out_map_bam=out_map_bam)

	return inputs, outputs, options, spec

#Unique reads
def unique_reads(out_map_bam, out_map_unique):
	inputs = [out_map_bam]
	outputs = [out_map_unique]
	options = {"walltime":"02:00:00","account":"piRNA", "memory":"30gb"}
	spec = '''
	sambamba view -t 12 -h -f bam -F "mapping_quality >= 1 and not (unmapped or secondary_alignment) and not ([XA] != null or [SA] != null)" {} -o {}
	'''.format(out_map_bam, out_map_unique)
	return inputs, outputs, options, spec
#Multi reads
def multi_reads(out_map_bam, out_map_multi):
	inputs = [out_map_bam]
	outputs = [out_map_multi]
	options = {"walltime":"02:00:00","account":"piRNA", "memory":"30gb"}
	spec = '''
	sambamba view -t 12 -h -f bam -F "mapping_quality == 0" {} -o {}
	'''.format(out_map_bam, out_map_multi)
	return inputs, outputs, options, spec
#Unique to fasta
def unique_fasta(out_map_unique, unique_fasta_file):
	inputs = [out_map_unique]
	outputs = [unique_fasta_file]
	options = {"walltime":"02:00:00","account":"piRNA", "memory":"30gb"}
	spec = '''
	samtools bam2fq {} > {} 
	'''.format(out_map_unique, unique_fasta_file)
	return inputs, outputs, options, spec
#Multi to fasta
def multi_fasta(out_map_multi, multi_fasta_file):
	inputs = [out_map_multi]
	outputs = [multi_fasta_file]
	options = {"walltime":"02:00:00","account":"piRNA", "memory":"30gb"}
	spec = '''
	samtools bam2fq {} > {}
	'''.format(out_map_multi, multi_fasta_file)
	return inputs, outputs, options, spec
 
species_sample_dict = {
	"human":["Hum1","Hum2"],
	"chimp":["Chimp1","Chimp2","Carl","Martin"],
	"gorilla":["Samson", "MBewe"],
	"baboon":["Baboon1","Baboon2"],
	"bonobo":["Bonobo"],
	"gibbon":["Gibbon"],
	"orangutan":["Orang1", "Pongo"],
	"catta_lemur":["Kat34", "Kat35", "Makak"]
} 

raw_data= "/home/juliasalas/piRNA/Workspaces/julia/PrimaryData/raw_data/"
cutadapt_output= "/home/juliasalas/piRNA/Workspaces/julia/pre_process/cutadapt"
output_map="/home/juliasalas/piRNA/Workspaces/julia/map_all"
index="/home/juliasalas/piRNA/Workspaces/julia/PrimaryData/index/"
unique_output="/home/juliasalas/piRNA/Workspaces/julia/pre_process/unique_reads"
multi_output="/home/juliasalas/piRNA/Workspaces/julia/pre_process/multi_reads"

for sps,samples in species_sample_dict.items():
	for sample in samples:
		reads_raw = f'{raw_data}{sample}/{sample}.fq.gz'	
		## CUTADAPT
        
		cutadapt_sample = f'{cutadapt_output}/{sample}/' 
		if not os.path.exists(cutadapt_sample):
			os.makedirs(cutadapt_sample)
		
		reads_flt = f'{cutadapt_sample}{sample}.flt.fq.gz'
		gwf.target_from_template(f'cutadapt_{sample}',
			cutadapt(reads_raw, reads_flt))
		# mapping
		genome_index=f'{index}{sps}/{sps}_index'
		map_sample= f'{output_map}/{sample}/'
		if not os.path.exists(map_sample):
			os.makedirs(map_sample)
		out_map_sai=f'{map_sample}{sample}_map.sai'
		out_map_bam=f'{map_sample}{sample}_map.bam'
		gwf.target_from_template(f'map_{sample}',
			mapping(genome_index, reads_flt, out_map_sai, out_map_bam))
		
		#unique
		unique_sample= f'{unique_output}/{sample}/'
		if not os.path.exists(unique_sample):
			os.makedirs(unique_sample)
		
		out_map_unique=f'{unique_sample}{sample}_unique.bam'
		gwf.target_from_template(f'unique_{sample}',
			unique_reads(out_map_bam, out_map_unique))
		#multi
		multi_sample= f'{multi_output}/{sample}/'
		if not os.path.exists(multi_sample):
			os.makedirs(multi_sample)
		
		out_map_multi=f'{multi_sample}{sample}_multi.bam'
		gwf.target_from_template(f'multi_{sample}',
			multi_reads(out_map_bam, out_map_multi))
		#Unique to fasta
		unique_fasta_file=f'{unique_sample}{sample}_unique.fq'

		gwf.target_from_template(f'unique_fa_{sample}',
			   unique_fasta(out_map_unique, unique_fasta_file))
		#Multi to fasta
		multi_fasta_file=f'{multi_sample}{sample}_multi.fq'
		
		gwf.target_from_template(f'multi_fa_{sample}',
			   multi_fasta(out_map_multi, multi_fasta_file))
		