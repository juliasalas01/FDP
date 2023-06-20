from gwf import Workflow

gwf=Workflow()
import sys, os, re


##Functions##

#20
#Map the size to the ref genome
def map_20(genome_index,read_20, out_map_sai_20, out_map_bam_20):
	inputs = [ f'{genome_index}.amb',read_20] 
	outputs = [out_map_sai_20, out_map_bam_20]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	bwa aln -t 6 {genome_index} {read_20} > {out_map_sai_20}
	bwa samse -n 5000 {genome_index} {out_map_sai_20} {read_20} | samtools view -uS - | samtools sort -o {out_map_bam_20}
	'''.format(genome_index=genome_index,read_20=read_20, out_map_sai_20=out_map_sai_20, out_map_bam_20=out_map_bam_20)

	return inputs, outputs, options, spec
#from bam to bed
def map_bed_20(out_map_bam_20, out_map_bed_20):
	inputs = [ out_map_bam_20] 
	outputs = [out_map_bed_20]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	bedtools bamtobed -i {} > {}
	'''.format(out_map_bam_20,out_map_bed_20)

	return inputs, outputs, options, spec
#Intersect bed files

#21
def map_21(genome_index,read_21, out_map_sai_21, out_map_bam_21):
	inputs = [ f'{genome_index}.amb',read_21] 
	outputs = [out_map_sai_21, out_map_bam_21]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	bwa aln -t 6 {genome_index} {read_21} > {out_map_sai_21}
	bwa samse -n 5000 {genome_index} {out_map_sai_21} {read_21} | samtools view -uS - | samtools sort -o {out_map_bam_21}
	'''.format(genome_index=genome_index,read_21=read_21, out_map_sai_21=out_map_sai_21, out_map_bam_21=out_map_bam_21)

	return inputs, outputs, options, spec
#from bam to bed
def map_bed_21(out_map_bam_21, out_map_bed_21):
	inputs = [ out_map_bam_21] 
	outputs = [out_map_bed_21]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	samtools bamtobed -i {} > {}
	'''.format(out_map_bam_21,out_map_bed_21)

	return inputs, outputs, options, spec

#22
def map_22(genome_index,read_22, out_map_sai_22, out_map_bam_22):
	inputs = [ f'{genome_index}.amb',read_22] 
	outputs = [out_map_sai_22, out_map_bam_22]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	bwa aln -t 6 {genome_index} {read_22} > {out_map_sai_22}
	bwa samse -n 5000 {genome_index} {out_map_sai_22} {read_22} | samtools view -uS - | samtools sort -o {out_map_bam_22}
	'''.format(genome_index=genome_index,read_22=read_22, out_map_sai_22=out_map_sai_22, out_map_bam_22=out_map_bam_22)

	return inputs, outputs, options, spec
#from bam to bed
def map_bed_22(out_map_bam_22, out_map_bed_22):
	inputs = [ out_map_bam_22] 
	outputs = [out_map_bed_22]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	samtools bamtobed -i {} > {}
	'''.format(out_map_bam_22,out_map_bed_22)

	return inputs, outputs, options, spec

#23
def map_23(genome_index,read_23, out_map_sai_23, out_map_bam_23):
	inputs = [ f'{genome_index}.amb',read_23] 
	outputs = [out_map_sai_23, out_map_bam_23]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	bwa aln -t 6 {genome_index} {read_23} > {out_map_sai_23}
	bwa samse -n 5000 {genome_index} {out_map_sai_23} {read_23} | samtools view -uS - | samtools sort -o {out_map_bam_23}
	'''.format(genome_index=genome_index,read_23=read_23, out_map_sai_23=out_map_sai_23, out_map_bam_23=out_map_bam_23)

	return inputs, outputs, options, spec
#from bam to bed
def map_bed_23(out_map_bam_23, out_map_bed_23):
	inputs = [ out_map_bam_23] 
	outputs = [out_map_bed_23]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	samtools bamtobed -i {} > {}
	'''.format(out_map_bam_23,out_map_bed_23)

	return inputs, outputs, options, spec

#21
def map_21(genome_index,read_21, out_map_sai_21, out_map_bam_21):
	inputs = [ f'{genome_index}.amb',read_21] 
	outputs = [out_map_sai_21, out_map_bam_21]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	bwa aln -t 6 {genome_index} {read_21} > {out_map_sai_21}
	bwa samse -n 5000 {genome_index} {out_map_sai_21} {read_21} | samtools view -uS - | samtools sort -o {out_map_bam_21}
	'''.format(genome_index=genome_index,read_21=read_21, out_map_sai_21=out_map_sai_21, out_map_bam_21=out_map_bam_21)

	return inputs, outputs, options, spec
#from bam to bed
def map_bed_23(out_map_bam_23, out_map_bed_23):
	inputs = [ out_map_bam_23] 
	outputs = [out_map_bed_23]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	samtools bamtobed -i {} > {}
	'''.format(out_map_bam_23,out_map_bed_23)

	return inputs, outputs, options, spec
#24
def map_24(genome_index,read_24, out_map_sai_24, out_map_bam_24):
	inputs = [ f'{genome_index}.amb',read_24] 
	outputs = [out_map_sai_24, out_map_bam_24]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	bwa aln -t 6 {genome_index} {read_24} > {out_map_sai_24}
	bwa samse -n 5000 {genome_index} {out_map_sai_24} {read_24} | samtools view -uS - | samtools sort -o {out_map_bam_24}
	'''.format(genome_index=genome_index,read_24=read_24, out_map_sai_24=out_map_sai_24, out_map_bam_24=out_map_bam_24)

	return inputs, outputs, options, spec
#from bam to bed
def map_bed_24(out_map_bam_24, out_map_bed_24):
	inputs = [ out_map_bam_24] 
	outputs = [out_map_bed_24]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	samtools bamtobed -i {} > {}
	'''.format(out_map_bam_24,out_map_bed_24)

	return inputs, outputs, options, spec
#25
def map_25(genome_index,read_25, out_map_sai_25, out_map_bam_25):
	inputs = [ f'{genome_index}.amb',read_25] 
	outputs = [out_map_sai_25, out_map_bam_25]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	bwa aln -t 6 {genome_index} {read_25} > {out_map_sai_25}
	bwa samse -n 5000 {genome_index} {out_map_sai_25} {read_25} | samtools view -uS - | samtools sort -o {out_map_bam_25}
	'''.format(genome_index=genome_index,read_25=read_25, out_map_sai_25=out_map_sai_25, out_map_bam_25=out_map_bam_25)

	return inputs, outputs, options, spec
#from bam to bed
def map_bed_25(out_map_bam_25, out_map_bed_25):
	inputs = [ out_map_bam_25] 
	outputs = [out_map_bed_25]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	samtools bamtobed -i {} > {}
	'''.format(out_map_bam_25,out_map_bed_25)

	return inputs, outputs, options, spec

#26
def map_26(genome_index,read_26, out_map_sai_26, out_map_bam_26):
	inputs = [ f'{genome_index}.amb',read_26] 
	outputs = [out_map_sai_26, out_map_bam_26]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	bwa aln -t 6 {genome_index} {read_26} > {out_map_sai_26}
	bwa samse -n 5000 {genome_index} {out_map_sai_26} {read_26} | samtools view -uS - | samtools sort -o {out_map_bam_26}
	'''.format(genome_index=genome_index,read_26=read_26, out_map_sai_26=out_map_sai_26, out_map_bam_26=out_map_bam_26)

	return inputs, outputs, options, spec
#from bam to bed
def map_bed_26(out_map_bam_26, out_map_bed_26):
	inputs = [ out_map_bam_26] 
	outputs = [out_map_bed_26]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	samtools bamtobed -i {} > {}
	'''.format(out_map_bam_26,out_map_bed_26)

	return inputs, outputs, options, spec
#27
def map_27(genome_index,read_27, out_map_sai_27, out_map_bam_27):
	inputs = [ f'{genome_index}.amb',read_27] 
	outputs = [out_map_sai_27, out_map_bam_27]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	bwa aln -t 6 {genome_index} {read_27} > {out_map_sai_27}
	bwa samse -n 5000 {genome_index} {out_map_sai_27} {read_27} | samtools view -uS - | samtools sort -o {out_map_bam_27}
	'''.format(genome_index=genome_index,read_27=read_27, out_map_sai_27=out_map_sai_27, out_map_bam_27=out_map_bam_27)

	return inputs, outputs, options, spec
#from bam to bed
def map_bed_27(out_map_bam_27, out_map_bed_27):
	inputs = [ out_map_bam_27] 
	outputs = [out_map_bed_27]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	samtools bamtobed -i {} > {}
	'''.format(out_map_bam_27,out_map_bed_27)

	return inputs, outputs, options, spec

#28
def map_28(genome_index,read_28, out_map_sai_28, out_map_bam_28):
	inputs = [ f'{genome_index}.amb',read_28] 
	outputs = [out_map_sai_28, out_map_bam_28]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	bwa aln -t 6 {genome_index} {read_28} > {out_map_sai_28}
	bwa samse -n 5000 {genome_index} {out_map_sai_28} {read_28} | samtools view -uS - | samtools sort -o {out_map_bam_28}
	'''.format(genome_index=genome_index,read_28=read_28, out_map_sai_28=out_map_sai_28, out_map_bam_28=out_map_bam_28)

	return inputs, outputs, options, spec
#from bam to bed
def map_bed_28(out_map_bam_28, out_map_bed_28):
	inputs = [ out_map_bam_28] 
	outputs = [out_map_bed_28]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	samtools bamtobed -i {} > {}
	'''.format(out_map_bam_28,out_map_bed_28)

	return inputs, outputs, options, spec
#29
def map_29(genome_index,read_29, out_map_sai_29, out_map_bam_29):
	inputs = [ f'{genome_index}.amb',read_29] 
	outputs = [out_map_sai_29, out_map_bam_29]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	bwa aln -t 6 {genome_index} {read_29} > {out_map_sai_29}
	bwa samse -n 5000 {genome_index} {out_map_sai_29} {read_29} | samtools view -uS - | samtools sort -o {out_map_bam_29}
	'''.format(genome_index=genome_index,read_29=read_29, out_map_sai_29=out_map_sai_29, out_map_bam_29=out_map_bam_29)

	return inputs, outputs, options, spec
#from bam to bed
def map_bed_29(out_map_bam_29, out_map_bed_29):
	inputs = [ out_map_bam_29] 
	outputs = [out_map_bed_29]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	samtools bamtobed -i {} > {}
	'''.format(out_map_bam_29,out_map_bed_29)

	return inputs, outputs, options, spec
#30
def map_30(genome_index,read_30, out_map_sai_30, out_map_bam_30):
	inputs = [ f'{genome_index}.amb',read_30] 
	outputs = [out_map_sai_30, out_map_bam_30]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	bwa aln -t 6 {genome_index} {read_30} > {out_map_sai_30}
	bwa samse -n 5000 {genome_index} {out_map_sai_30} {read_30} | samtools view -uS - | samtools sort -o {out_map_bam_30}
	'''.format(genome_index=genome_index,read_30=read_30, out_map_sai_30=out_map_sai_30, out_map_bam_30=out_map_bam_30)

	return inputs, outputs, options, spec
#from bam to bed
def map_bed_30(out_map_bam_30, out_map_bed_30):
	inputs = [ out_map_bam_30] 
	outputs = [out_map_bed_30]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	bedtools bamtobed -i {} > {}
	'''.format(out_map_bam_30,out_map_bed_30)

	return inputs, outputs, options, spec

#31
def map_31(genome_index,read_31, out_map_sai_31, out_map_bam_31):
	inputs = [ f'{genome_index}.amb',read_31] 
	outputs = [out_map_sai_31, out_map_bam_31]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	bwa aln -t 6 {genome_index} {read_31} > {out_map_sai_31}
	bwa samse -n 5000 {genome_index} {out_map_sai_31} {read_31} | samtools view -uS - | samtools sort -o {out_map_bam_31}
	'''.format(genome_index=genome_index,read_31=read_31, out_map_sai_31=out_map_sai_31, out_map_bam_31=out_map_bam_31)

	return inputs, outputs, options, spec
#from bam to bed
def map_bed_31(out_map_bam_31, out_map_bed_31):
	inputs = [ out_map_bam_31] 
	outputs = [out_map_bed_31]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	bedtools bamtobed -i {} > {}
	'''.format(out_map_bam_31,out_map_bed_31)

#32
def map_32(genome_index,read_32, out_map_sai_32, out_map_bam_32):
	inputs = [ f'{genome_index}.amb',read_32] 
	outputs = [out_map_sai_32, out_map_bam_32]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	bwa aln -t 6 {genome_index} {read_32} > {out_map_sai_32}
	bwa samse -n 5000 {genome_index} {out_map_sai_32} {read_32} | samtools view -uS - | samtools sort -o {out_map_bam_32}
	'''.format(genome_index=genome_index,read_32=read_32, out_map_sai_32=out_map_sai_32, out_map_bam_32=out_map_bam_32)

	return inputs, outputs, options, spec
#from bam to bed
def map_bed_32(out_map_bam_32, out_map_bed_32):
	inputs = [ out_map_bam_32] 
	outputs = [out_map_bed_32]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	bedtools bamtobed -i {} > {}
	'''.format(out_map_bam_32,out_map_bed_32)

	#33
def map_33(genome_index,read_33, out_map_sai_33, out_map_bam_33):
	inputs = [ f'{genome_index}.amb',read_33] 
	outputs = [out_map_sai_33, out_map_bam_33]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	bwa aln -t 6 {genome_index} {read_33} > {out_map_sai_33}
	bwa samse -n 5000 {genome_index} {out_map_sai_33} {read_33} | samtools view -uS - | samtools sort -o {out_map_bam_33}
	'''.format(genome_index=genome_index,read_33=read_33, out_map_sai_33=out_map_sai_33, out_map_bam_33=out_map_bam_33)

	return inputs, outputs, options, spec
#from bam to bed
def map_bed_33(out_map_bam_33, out_map_bed_33):
	inputs = [ out_map_bam_33] 
	outputs = [out_map_bed_33]
	options = {"walltime":"48:00:00","cores":6,"memory":"100g","account":"piRNA"}
	spec = '''
	bedtools bamtobed -i {} > {}
	'''.format(out_map_bam_33,out_map_bed_33)

index="/home/juliasalas/piRNA/Workspaces/julia/PrimaryData/index/"
reads="/home/juliasalas/piRNA/Workspaces/julia/per_size/"
piRNA_20_output="/home/juliasalas/piRNA/Workspaces/julia/per_size/map/20"
bed_output_20="/home/juliasalas/piRNA/Workspaces/julia/per_size/map/20"
piRNA_21_output="/home/juliasalas/piRNA/Workspaces/julia/per_size/map/21"
bed_output_21="/home/juliasalas/piRNA/Workspaces/julia/per_size/map/21"
piRNA_22_output="/home/juliasalas/piRNA/Workspaces/julia/per_size/map/22"
bed_output_22="/home/juliasalas/piRNA/Workspaces/julia/per_size/map/22"
piRNA_23_output="/home/juliasalas/piRNA/Workspaces/julia/per_size/map/23"
bed_output_23="/home/juliasalas/piRNA/Workspaces/julia/per_size/map/23"
piRNA_24_output="/home/juliasalas/piRNA/Workspaces/julia/per_size/map/24"
bed_output_24="/home/juliasalas/piRNA/Workspaces/julia/per_size/map/24"
piRNA_25_output="/home/juliasalas/piRNA/Workspaces/julia/per_size/map/25"
bed_output_25="/home/juliasalas/piRNA/Workspaces/julia/per_size/map/25"
piRNA_26_output="/home/juliasalas/piRNA/Workspaces/julia/per_size/map/26"
bed_output_26="/home/juliasalas/piRNA/Workspaces/julia/per_size/map/26"
piRNA_27_output="/home/juliasalas/piRNA/Workspaces/julia/per_size/map/27"
bed_output_27="/home/juliasalas/piRNA/Workspaces/julia/per_size/map/27"
piRNA_28_output="/home/juliasalas/piRNA/Workspaces/julia/per_size/map/28"
bed_output_28="/home/juliasalas/piRNA/Workspaces/julia/per_size/map/28"
piRNA_29_output="/home/juliasalas/piRNA/Workspaces/julia/per_size/map/29"
bed_output_29="/home/juliasalas/piRNA/Workspaces/julia/per_size/map/29"
piRNA_30_output="/home/juliasalas/piRNA/Workspaces/julia/per_size/map/30"
bed_output_30="/home/juliasalas/piRNA/Workspaces/julia/per_size/map/30"
piRNA_31_output="/home/juliasalas/piRNA/Workspaces/julia/per_size/map/31"
bed_output_31="/home/juliasalas/piRNA/Workspaces/julia/per_size/map/31"
piRNA_32_output="/home/juliasalas/piRNA/Workspaces/julia/per_size/map/32"
bed_output_32="/home/juliasalas/piRNA/Workspaces/julia/per_size/map/32"
piRNA_33_output="/home/juliasalas/piRNA/Workspaces/julia/per_size/map/33"
bed_output_33="/home/juliasalas/piRNA/Workspaces/julia/per_size/map/33"
species_sample_dict = {
	"human":["Hum1","Hum2"]
} 
for sps,samples in species_sample_dict.items():
	for sample in samples:
		genome_index=f'{index}{sps}/{sps}_index'
        
		#20
		read_20=f'{reads}{sample}/{sample}_20.fq.gz'
		piRNA_sample_20= f'{piRNA_20_output}/{sample}/'
		if not os.path.exists(piRNA_sample_20):
			os.makedirs(piRNA_sample_20)
		out_map_sai_20=f'{piRNA_20_output}/{sample}_map.sai'
		out_map_bam_20=f'{piRNA_20_output}/{sample}_map.bam'
		gwf.target_from_template(f'{sample}_piRNA_20',
			map_20(genome_index,read_20, out_map_sai_20, out_map_bam_20))
		
		#bam to bed
		bed_sample_20=f'{bed_output_20}'
		if not os.path.exists(bed_sample_20):
			os.makedirs(bed_sample_20)
		out_map_bed_20=f'{bed_output_20}/{sample}_map.bed'
		gwf.target_from_template(f'{sample}_bed_20',
			map_bed_20(out_map_bam_20, out_map_bed_20))
		
		#21
		read_21=f'{reads}{sample}/{sample}_21.fq.gz'
		piRNA_sample_21= f'{piRNA_21_output}/{sample}/'
		if not os.path.exists(piRNA_sample_21):
			os.makedirs(piRNA_sample_21)
		out_map_sai_21=f'{piRNA_21_output}/{sample}_map.sai'
		out_map_bam_21=f'{piRNA_21_output}/{sample}_map.bam'
		gwf.target_from_template(f'{sample}_piRNA_21',
			map_21(genome_index,read_21, out_map_sai_21, out_map_bam_21))
		
		#bam to bed
		bed_sample_21=f'{bed_output_21}'
		if not os.path.exists(bed_sample_21):
			os.makedirs(bed_sample_21)
		out_map_bed_21=f'{bed_output_21}/{sample}_map.bed'
		gwf.target_from_template(f'{sample}_bed_21',
		 	map_bed_21(out_map_bam_21, out_map_bed_21))
		
		#22
		read_22=f'{reads}{sample}/{sample}_22.fq.gz'
		piRNA_sample_22= f'{piRNA_22_output}/{sample}/'
		if not os.path.exists(piRNA_sample_22):
			os.makedirs(piRNA_sample_22)
		out_map_sai_22=f'{piRNA_22_output}/{sample}_map.sai'
		out_map_bam_22=f'{piRNA_22_output}/{sample}_map.bam'
		gwf.target_from_template(f'{sample}_piRNA_22',
			map_22(genome_index,read_22, out_map_sai_22, out_map_bam_22))
		
		#bam to bed
		bed_sample_22=f'{bed_output_22}'
		if not os.path.exists(bed_sample_22):
			os.makedirs(bed_sample_22)
		out_map_bed_22=f'{bed_output_22}/{sample}_map.bed'
		gwf.target_from_template(f'{sample}_bed_22',
		 	map_bed_22(out_map_bam_22, out_map_bed_22))
		
		#23
		read_23=f'{reads}{sample}/{sample}_23.fq.gz'
		piRNA_sample_23= f'{piRNA_23_output}/{sample}/'
		if not os.path.exists(piRNA_sample_23):
			os.makedirs(piRNA_sample_23)
		out_map_sai_23=f'{piRNA_23_output}/{sample}_map.sai'
		out_map_bam_23=f'{piRNA_23_output}/{sample}_map.bam'
		gwf.target_from_template(f'{sample}_piRNA_23',
			   map_23(genome_index,read_23, out_map_sai_23, out_map_bam_23))
		
		#bam to bed
		bed_sample_23=f'{bed_output_23}'
		if not os.path.exists(bed_sample_23):
			os.makedirs(bed_sample_23)
		out_map_bed_23=f'{bed_output_23}/{sample}_map.bed'
		gwf.target_from_template(f'{sample}_bed_23',
		 	map_bed_23(out_map_bam_23, out_map_bed_23))
		
		#24
		read_24=f'{reads}{sample}/{sample}_24.fq.gz'
		piRNA_sample_24= f'{piRNA_24_output}/{sample}/'
		if not os.path.exists(piRNA_sample_24):
			os.makedirs(piRNA_sample_24)
		out_map_sai_24=f'{piRNA_24_output}/{sample}_map.sai'
		out_map_bam_24=f'{piRNA_24_output}/{sample}_map.bam'
		gwf.target_from_template(f'{sample}_piRNA_24',
			map_24(genome_index,read_24, out_map_sai_24, out_map_bam_24))
		
		#bam to bed
		bed_sample_24=f'{bed_output_24}'
		if not os.path.exists(bed_sample_24):
			os.makedirs(bed_sample_24)
		out_map_bed_24=f'{bed_output_24}/{sample}_map.bed'
		gwf.target_from_template(f'{sample}_bed_24',
			map_bed_24(out_map_bam_24, out_map_bed_24))
		
		#25
		read_25=f'{reads}{sample}/{sample}_25.fq.gz'
		piRNA_sample_25= f'{piRNA_25_output}/{sample}/'
		if not os.path.exists(piRNA_sample_25):
			os.makedirs(piRNA_sample_25)
		out_map_sai_25=f'{piRNA_25_output}/{sample}_map.sai'
		out_map_bam_25=f'{piRNA_25_output}/{sample}_map.bam'
		gwf.target_from_template(f'{sample}_piRNA_25',
			map_25(genome_index,read_25, out_map_sai_25, out_map_bam_25))
		
		#bam to bed
		bed_sample_25=f'{bed_output_25}'
		if not os.path.exists(bed_sample_25):
			os.makedirs(bed_sample_25)
		out_map_bed_25=f'{bed_output_25}/{sample}_map.bed'
		gwf.target_from_template(f'{sample}_bed_25',
			map_bed_25(out_map_bam_25, out_map_bed_25))
		
		#26
		read_26=f'{reads}{sample}/{sample}_26.fq.gz'
		piRNA_sample_26= f'{piRNA_26_output}/{sample}/'
		if not os.path.exists(piRNA_sample_26):
			os.makedirs(piRNA_sample_26)
		out_map_sai_26=f'{piRNA_26_output}/{sample}_map.sai'
		out_map_bam_26=f'{piRNA_26_output}/{sample}_map.bam'
		gwf.target_from_template(f'{sample}_piRNA_26',
			   map_26(genome_index,read_26, out_map_sai_26, out_map_bam_26))
		
		#bam to bed
		bed_sample_26=f'{bed_output_26}'
		if not os.path.exists(bed_sample_26):
			os.makedirs(bed_sample_26)
		out_map_bed_26=f'{bed_output_26}/{sample}_map.bed'
		gwf.target_from_template(f'{sample}_bed_26',
		 map_bed_26(out_map_bam_26, out_map_bed_26))
		
		#27
		read_27=f'{reads}{sample}/{sample}_27.fq.gz'
		piRNA_sample_27= f'{piRNA_27_output}/{sample}/'
		if not os.path.exists(piRNA_sample_27):
			os.makedirs(piRNA_sample_27)
		out_map_sai_27=f'{piRNA_27_output}/{sample}_map.sai'
		out_map_bam_27=f'{piRNA_27_output}/{sample}_map.bam'
		gwf.target_from_template(f'{sample}_piRNA_27',
			   map_27(genome_index,read_27, out_map_sai_27, out_map_bam_27))
		
		#bam to bed
		bed_sample_27=f'{bed_output_27}'
		if not os.path.exists(bed_sample_27):
			os.makedirs(bed_sample_27)
		out_map_bed_27=f'{bed_output_27}/{sample}_map.bed'
		gwf.target_from_template(f'{sample}_bed_27',
		 map_bed_27(out_map_bam_27, out_map_bed_27))
		
		#28
		read_28=f'{reads}{sample}/{sample}_28.fq.gz'
		piRNA_sample_28= f'{piRNA_28_output}/{sample}/'
		if not os.path.exists(piRNA_sample_28):
			os.makedirs(piRNA_sample_28)
		out_map_sai_28=f'{piRNA_28_output}/{sample}_map.sai'
		out_map_bam_28=f'{piRNA_28_output}/{sample}_map.bam'
		gwf.target_from_template(f'{sample}_piRNA_28',
			   map_28(genome_index,read_28, out_map_sai_28, out_map_bam_28))
		
		#bam to bed
		bed_sample_28=f'{bed_output_28}'
		if not os.path.exists(bed_sample_28):
			os.makedirs(bed_sample_28)
		out_map_bed_28=f'{bed_output_28}/{sample}_map.bed'
		gwf.target_from_template(f'{sample}_bed_28',
		 map_bed_28(out_map_bam_28, out_map_bed_28))
		
		#29
		read_29=f'{reads}{sample}/{sample}_29.fq.gz'
		piRNA_sample_29= f'{piRNA_29_output}/{sample}/'
		if not os.path.exists(piRNA_sample_29):
			os.makedirs(piRNA_sample_29)
		out_map_sai_29=f'{piRNA_29_output}/{sample}_map.sai'
		out_map_bam_29=f'{piRNA_29_output}/{sample}_map.bam'
		gwf.target_from_template(f'{sample}_piRNA_29',
			   map_29(genome_index,read_29, out_map_sai_29, out_map_bam_29))
		
		#bam to bed
		bed_sample_29=f'{bed_output_29}'
		if not os.path.exists(bed_sample_29):
			os.makedirs(bed_sample_29)
		out_map_bed_29=f'{bed_output_29}/{sample}_map.bed'
		gwf.target_from_template(f'{sample}_bed_29',
		 map_bed_29(out_map_bam_29, out_map_bed_29))
		
		#30
		read_30=f'{reads}{sample}/{sample}_30.fq.gz'
		piRNA_sample_30= f'{piRNA_30_output}/{sample}/'
		if not os.path.exists(piRNA_sample_30):
			os.makedirs(piRNA_sample_30)
		out_map_sai_30=f'{piRNA_30_output}/{sample}_map.sai'
		out_map_bam_30=f'{piRNA_30_output}/{sample}_map.bam'
		gwf.target_from_template(f'{sample}_piRNA_30',
			   map_30(genome_index,read_30, out_map_sai_30, out_map_bam_30))
		
		#bam to bed
		bed_sample_30=f'{bed_output_30}'
		if not os.path.exists(bed_sample_30):
			os.makedirs(bed_sample_30)
		out_map_bed_30=f'{bed_output_30}/{sample}_map.bed'
		gwf.target_from_template(f'{sample}_bed_30',
		 map_bed_30(out_map_bam_30, out_map_bed_30))
		
		#31
		read_31=f'{reads}{sample}/{sample}_31.fq.gz'
		piRNA_sample_31= f'{piRNA_31_output}/{sample}/'
		if not os.path.exists(piRNA_sample_31):
			os.makedirs(piRNA_sample_31)
		out_map_sai_31=f'{piRNA_31_output}/{sample}_map.sai'
		out_map_bam_31=f'{piRNA_31_output}/{sample}_map.bam'
		gwf.target_from_template(f'{sample}_piRNA_31',
			   map_31(genome_index,read_31, out_map_sai_31, out_map_bam_31))
		

		
			#32
		read_32=f'{reads}{sample}/{sample}_32.fq.gz'
		piRNA_sample_32= f'{piRNA_32_output}/{sample}/'
		if not os.path.exists(piRNA_sample_32):
			os.makedirs(piRNA_sample_32)
		out_map_sai_32=f'{piRNA_32_output}/{sample}_map.sai'
		out_map_bam_32=f'{piRNA_32_output}/{sample}_map.bam'
		gwf.target_from_template(f'{sample}_piRNA_32',
			   map_32(genome_index,read_32, out_map_sai_32, out_map_bam_32))
	
		#33
		read_33=f'{reads}{sample}/{sample}_33.fq.gz'
		piRNA_sample_33= f'{piRNA_33_output}/{sample}/'
		if not os.path.exists(piRNA_sample_33):
			os.makedirs(piRNA_sample_33)
		out_map_sai_33=f'{piRNA_33_output}/{sample}_map.sai'
		out_map_bam_33=f'{piRNA_33_output}/{sample}_map.bam'
		gwf.target_from_template(f'{sample}_piRNA_33',
			   map_33(genome_index,read_33, out_map_sai_33, out_map_bam_33))
		
