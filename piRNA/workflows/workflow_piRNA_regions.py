from gwf import Workflow

gwf=Workflow()
import sys, os, re

##Functions##
#Filter by size the piRNA
def piRNA_filter(reads_flt, piRNA_reads):
	inputs = [reads_flt]
	outputs = [piRNA_reads]
	options = {"account":"piRNA", "memory":"120gb"}
	spec = '''
	python /home/juliasalas/piRNA/Workspaces/julia/scripts/filter_size.py {} {}
	'''.format(reads_flt, piRNA_reads)
	return inputs, outputs, options, spec

#Mapping the piRNA into the genome of each specie
def mapping_piRNA(genome_index,piRNA_reads, out_map_sai_piRNA, out_map_bam_piRNA):
	inputs = [ f'{genome_index}.amb',piRNA_reads] 
	outputs = [out_map_sai_piRNA, out_map_bam_piRNA]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	bwa aln -t 6 {genome_index} {piRNA_reads} > {out_map_sai_piRNA}
	bwa samse -n 5000 {genome_index} {out_map_sai_piRNA} {piRNA_reads} | samtools view -uS - | samtools sort -o {out_map_bam_piRNA}
	'''.format(piRNA_reads=piRNA_reads, genome_index=genome_index, out_map_sai_piRNA=out_map_sai_piRNA, out_map_bam_piRNA=out_map_bam_piRNA)

	return inputs, outputs, options, spec

#Coverage of the map
def coverage_filter_piRNA(out_map_bam_piRNA, out_map_bam_coverage_piRNA):
	inputs = [out_map_bam_piRNA]
	outputs = [out_map_bam_coverage_piRNA] 
	options = {"walltime":"02:00:00","account":"piRNA", "memory":"30gb"}
	spec = '''
	samtools depth {} > {}
	'''.format(out_map_bam_piRNA, out_map_bam_coverage_piRNA)
	return inputs, outputs, options, spec 

#Unique reads
def unique_reads(out_map_bam_piRNA, out_map_unique):
	inputs = [out_map_bam_piRNA]
	outputs = [out_map_unique]
	options = {"walltime":"02:00:00","account":"piRNA", "memory":"30gb"}
	spec = '''
	sambamba view -t 12 -h -f bam -F "mapping_quality >= 1 and not (unmapped or secondary_alignment) and not ([XA] != null or [SA] != null)" {} -o {}
	'''.format(out_map_bam_piRNA, out_map_unique)
	return inputs, outputs, options, spec

#Multi reads
def multi_reads(out_map_bam_piRNA, out_map_multi):
	inputs = [out_map_bam_piRNA]
	outputs = [out_map_multi]
	options = {"walltime":"02:00:00","account":"piRNA", "memory":"30gb"}
	spec = '''
	sambamba view -t 12 -h -f bam -F "mapping_quality == 0" {} -o {}
	'''.format(out_map_bam_piRNA, out_map_multi)
	return inputs, outputs, options, spec 


#Coverage of the map
def coverage_unique(out_map_unique, out_map_bam_coverage_unique):
	inputs = [out_map_unique]
	outputs = [out_map_bam_coverage_unique] 
	options = {"walltime":"02:00:00","account":"piRNA", "memory":"30gb"}
	spec = '''
	samtools depth {} > {}
	'''.format(out_map_unique, out_map_bam_coverage_unique)
	return inputs, outputs, options, spec 
#Coverage of the map
def coverage_multi(out_map_multi, out_map_bam_coverage_multi):
	inputs = [out_map_unique]
	outputs = [out_map_bam_coverage_multi] 
	options = {"walltime":"02:00:00","account":"piRNA", "memory":"30gb"}
	spec = '''
	samtools depth {} > {}
	'''.format(out_map_multi, out_map_bam_coverage_multi)
	return inputs, outputs, options, spec 

#Mapping the piRNA into the human genome
def mapping_piRNA_human(genome_index,piRNA_reads, out_map_sai, out_map_bam_human):
	inputs = [ f'{genome_index}.amb',piRNA_reads] 
	outputs = [out_map_sai, out_map_bam_human]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	bwa aln -t 6 {genome_index} {piRNA_reads} > {out_map_sai}
	bwa samse -n 5000 {genome_index} {out_map_sai} {piRNA_reads} | samtools view -uS - | samtools sort -o {out_map_bam_human}
	'''.format(piRNA_reads=piRNA_reads, genome_index=genome_index, out_map_sai=out_map_sai, out_map_bam_human=out_map_bam_human)

	return inputs, outputs, options, spec
#Unique reads
def unique_reads_human(out_map_bam_human, out_map_unique_human):
	inputs = [out_map_bam_human]
	outputs = [out_map_unique_human]
	options = {"walltime":"02:00:00","account":"piRNA", "memory":"30gb"}
	spec = '''
	sambamba view -t 12 -h -f bam -F "mapping_quality >= 1 and not (unmapped or secondary_alignment) and not ([XA] != null or [SA] != null)" {} -o {}
	'''.format(out_map_bam_human, out_map_unique_human)
	return inputs, outputs, options, spec
#Multi reads
def multi_reads_human(out_map_bam_human, out_map_multi_human):
	inputs = [out_map_bam_human]
	outputs = [out_map_multi_human]
	options = {"walltime":"02:00:00","account":"piRNA", "memory":"30gb"}
	spec = '''
	sambamba view -t 12 -h -f bam -F "mapping_quality == 0" {} -o {}
	'''.format(out_map_bam_human, out_map_multi_human)
	return inputs, outputs, options, spec 
#Coverage of the map
def coverage_unique_human(out_map_unique_human, out_map_bam_coverage_unique_human):
	inputs = [out_map_unique_human]
	outputs = [out_map_bam_coverage_unique_human] 
	options = {"walltime":"02:00:00","account":"piRNA", "memory":"30gb"}
	spec = '''
	samtools depth {} > {}
	'''.format(out_map_unique_human, out_map_bam_coverage_unique_human)
	return inputs, outputs, options, spec 
#Coverage of the map
def coverage_multi_human(out_map_multi_human, out_map_bam_coverage_multi_human):
	inputs = [out_map_multi_human]
	outputs = [out_map_bam_coverage_multi_human] 
	options = {"walltime":"02:00:00","account":"piRNA", "memory":"30gb"}
	spec = '''
	samtools depth {} > {}
	'''.format(out_map_multi_human, out_map_bam_coverage_multi_human)
	return inputs, outputs, options, spec 

piRNA_output="/home/juliasalas/piRNA/Workspaces/julia/piRNA_reads"
cutadapt_output="/home/juliasalas/piRNA/Workspaces/julia/cutadapt"
piRNA_output_map="/home/juliasalas/piRNA/Workspaces/julia/piRNA_reads/mapping_species"
index="/home/juliasalas/piRNA/Workspaces/julia/PrimaryData/index/"
piRNA_output_coverage="/home/juliasalas/piRNA/Workspaces/julia/piRNA_reads/mapping_species/coverage"
output_unique="/home/juliasalas/piRNA/Workspaces/julia/piRNA_reads/mapping_species/unique_mapping"
output_multi="/home/juliasalas/piRNA/Workspaces/julia/piRNA_reads/mapping_species/multi_mapping"
piRNA_output_coverage_unique="/home/juliasalas/piRNA/Workspaces/julia/piRNA_reads/mapping_species/unique_mapping/coverage"
piRNA_output_coverage_multi="/home/juliasalas/piRNA/Workspaces/julia/piRNA_reads/mapping_species/multi_mapping/coverage"
piRNA_output_map_human="/home/juliasalas/piRNA/Workspaces/julia/piRNA_reads/mapping_human"
output_unique_human="/home/juliasalas/piRNA/Workspaces/julia/piRNA_reads/mapping_human/unique"
output_multi_human="/home/juliasalas/piRNA/Workspaces/julia/piRNA_reads/mapping_human/multi"
piRNA_output_coverage_unique_human="/home/juliasalas/piRNA/Workspaces/julia/piRNA_reads/mapping_human/unique/coverage"
piRNA_output_coverage_multi_human="/home/juliasalas/piRNA/Workspaces/julia/piRNA_reads/mapping_human/multi/coverage"
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
for sps,samples in species_sample_dict.items():
    for sample in samples:
        #piRNA filtering
        reads_flt=f'{cutadapt_output}/{sample}/{sample}.flt.fq.gz'
        piRNA_sample= f'{piRNA_output}/{sample}/'
        if not os.path.exists(piRNA_sample):
            os.makedirs(piRNA_sample)
        piRNA_reads=f'{piRNA_sample}{sample}_size.fq.gz'
        gwf.target_from_template(f'{sample}_piRNA',
            piRNA_filter(reads_flt, piRNA_reads))
        
        #piRNA mapping
        genome_index=f'{index}{sps}/{sps}_index'
        piRNA_map_sample= f'{piRNA_output_map}/{sample}/'
        if not os.path.exists(piRNA_map_sample):
            os.makedirs(piRNA_map_sample)
        out_map_sai_piRNA=f'{piRNA_map_sample}{sample}_map.sai'
        out_map_bam_piRNA=f'{piRNA_map_sample}{sample}_map.bam'
        gwf.target_from_template(f'piRNA_map_{sample}',
            mapping_piRNA(genome_index, piRNA_reads, out_map_sai_piRNA, out_map_bam_piRNA))
        #piRNA coverage
        piRNA_coverage_sample= f'{piRNA_output_coverage}/{sample}/'
        if not os.path.exists(piRNA_coverage_sample):
            os.makedirs(piRNA_coverage_sample)
		
        out_map_bam_coverage_piRNA=f'{piRNA_coverage_sample}{sample}_coverage'
        gwf.target_from_template(f'piRNA_coverage_{sample}',
            coverage_filter_piRNA(out_map_bam_piRNA, out_map_bam_coverage_piRNA))
        
        #Unique reads
        unique_sample= f'{output_unique}/{sample}/'
        if not os.path.exists(unique_sample):
            os.makedirs(unique_sample)
		
        out_map_unique=f'{unique_sample}{sample}_unique.bam'
        gwf.target_from_template(f'unique_{sample}',
            unique_reads(out_map_bam_piRNA, out_map_unique))
		
		#piRNA multi
        multi_sample= f'{output_multi}/{sample}/'
        if not os.path.exists(multi_sample):
            os.makedirs(multi_sample)
		
        out_map_multi=f'{multi_sample}{sample}_multi.bam'
        gwf.target_from_template(f'multi_{sample}',
            multi_reads(out_map_bam_piRNA, out_map_multi))
        
        #piRNA coverage
        piRNA_coverage_sample_unique= f'{piRNA_output_coverage_unique}/{sample}/'
        if not os.path.exists(piRNA_coverage_sample_unique):
            os.makedirs(piRNA_coverage_sample_unique)
		
        out_map_bam_coverage_unique=f'{piRNA_coverage_sample_unique}{sample}_coverage'
        gwf.target_from_template(f'piRNA_coverage_unique_{sample}',
            coverage_unique(out_map_unique, out_map_bam_coverage_unique))
        
         #piRNA coverage
        piRNA_coverage_sample_multi= f'{piRNA_output_coverage_multi}/{sample}/'
        if not os.path.exists(piRNA_coverage_sample_multi):
            os.makedirs(piRNA_coverage_sample_multi)
		
        out_map_bam_coverage_multi=f'{piRNA_coverage_sample_multi}{sample}_coverage'
        gwf.target_from_template(f'piRNA_coverage_multi_{sample}',
            coverage_multi(out_map_multi, out_map_bam_coverage_multi))
	
	    #against human genome
		#piRNA mapping
        genome_index=f'{index}human/human_index'
        piRNA_map_sample_human= f'{piRNA_output_map_human}/{sample}/'
        if not os.path.exists(piRNA_map_sample_human):
            os.makedirs(piRNA_map_sample_human)
        out_map_sai=f'{piRNA_map_sample_human}{sample}_map.sai'
        out_map_bam_human=f'{piRNA_map_sample_human}{sample}_map.bam'
        gwf.target_from_template(f'piRNA_map_human_{sample}',
           mapping_piRNA_human(genome_index,piRNA_reads, out_map_sai, out_map_bam_human))
		
		#Unique reads
        unique_sample_human= f'{output_unique_human}/{sample}/'
        if not os.path.exists(unique_sample_human):
            os.makedirs(unique_sample_human)
		
        out_map_unique_human=f'{unique_sample_human}{sample}_unique.bam'
        gwf.target_from_template(f'unique_human_{sample}',
            unique_reads_human(out_map_bam_human, out_map_unique_human))
		
		#piRNA multi
        multi_sample_human= f'{output_multi_human}/{sample}/'
        if not os.path.exists(multi_sample_human):
            os.makedirs(multi_sample_human)
		
        out_map_multi_human=f'{multi_sample_human}{sample}_multi.bam'
        gwf.target_from_template(f'multi_human_{sample}',
            multi_reads_human(out_map_bam_human, out_map_multi_human))
        
        #piRNA coverage
        piRNA_coverage_sample_unique_human= f'{piRNA_output_coverage_unique_human}/{sample}/'
        if not os.path.exists(piRNA_coverage_sample_unique_human):
            os.makedirs(piRNA_coverage_sample_unique_human)
		
        out_map_bam_coverage_unique_human=f'{piRNA_coverage_sample_unique_human}{sample}_coverage'
        gwf.target_from_template(f'piRNA_coverage_unique_human_{sample}',
            coverage_unique_human(out_map_unique_human, out_map_bam_coverage_unique_human))
        
         #piRNA coverage
        piRNA_coverage_sample_multi_human= f'{piRNA_output_coverage_multi_human}/{sample}/'
        if not os.path.exists(piRNA_coverage_sample_multi_human):
            os.makedirs(piRNA_coverage_sample_multi_human)
		
        out_map_bam_coverage_multi_human=f'{piRNA_coverage_sample_multi_human}{sample}_coverage'
        gwf.target_from_template(f'piRNA_coverage_multi_human_{sample}',
            coverage_multi_human(out_map_multi_human, out_map_bam_coverage_multi_human))
