from gwf import Workflow

gwf=Workflow()
import sys, os, re

##Functions##

#Mapping all
def mapping_all(genome_index,all_reads, out_map_sai_all, out_map_bam_all):
	inputs = [ f'{genome_index}.amb',all_reads] 
	outputs = [out_map_sai_all, out_map_bam_all]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	bwa aln -t 6 {genome_index} {all_reads} > {out_map_sai_all}
	bwa samse -n 5000 {genome_index} {out_map_sai_all} {all_reads} | samtools view -uS - | samtools sort -o {out_map_bam_all}
	'''.format(all_reads=all_reads, genome_index=genome_index, out_map_sai_all=out_map_sai_all, out_map_bam_all=out_map_bam_all)

	return inputs, outputs, options, spec
#Unique reads
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
all_output_map="/home/juliasalas/piRNA/Workspaces/julia/all_reads/map"
index="/home/juliasalas/piRNA/Workspaces/julia/PrimaryData/index/"
cutadapt="/home/juliasalas/piRNA/Workspaces/julia/piRNA/cutadapt/"
output_unique="/home/juliasalas/piRNA/Workspaces/julia/all_reads/map/unique"
output_multi="/home/juliasalas/piRNA/Workspaces/julia/all_reads/map/multi"
for sps,samples in species_sample_dict.items():
	for sample in samples:
		#all mapping
		genome_index=f'{index}{sps}/{sps}_index'
		all_reads=f'{cutadapt}{sample}/{sample}.flt.fq.gz'
		all_map_sample= f'{all_output_map}/{sample}/'
		if not os.path.exists(all_map_sample):
			os.makedirs(all_map_sample)
		out_map_sai_all=f'{all_map_sample}{sample}_map.sai'
		out_map_bam_all=f'{all_map_sample}{sample}_map.bam'
		gwf.target_from_template(f'piRNA_map_{sample}',
				 mapping_all(genome_index,all_reads, out_map_sai_all, out_map_bam_all))
		#Unique reads
		unique_sample= f'{output_unique}/{sample}/'
		if not os.path.exists(unique_sample):
			os.makedirs(unique_sample)
		
		out_map_unique=f'{unique_sample}{sample}_unique.bam'
		gwf.target_from_template(f'unique_{sample}',
			unique_reads(out_map_bam_all, out_map_unique))
		
		#piRNA multi
		multi_sample= f'{output_multi}/{sample}/'
		if not os.path.exists(multi_sample):
			os.makedirs(multi_sample)
		
		out_map_multi=f'{multi_sample}{sample}_multi.bam'
		gwf.target_from_template(f'multi_{sample}',
			multi_reads(out_map_bam_all, out_map_multi))
		