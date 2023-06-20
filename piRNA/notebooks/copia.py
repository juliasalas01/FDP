gwf.target(f"chr1_maffilter",
    inputs=['/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr1.maf.gz'],
    outputs=['/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/chr1.filtered.maf'],
    cores=1,
    memory='4g',
    walltime= '12:00:00',
    account='piRNA') << f"""
maffilter param=/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/options_2.txt file=/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr1 sp1=Homo_sapiens sp2=Pan_troglodytes sp3=Gorilla_gorilla_gorilla sp4=Pongo_abelii sp5=Nomascus_leucogenys sp6=Papio_anubis sp7=Pan_paniscus sp8=Lemur_catta ref=Homo_sapiens > /home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/chr1.filtered.maf
"""
gwf.target(f"chr2_maffilter",
    inputs=['/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr2.maf.gz'],
    outputs=['/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/chr2.filtered.maf'],
    cores=1,
    memory='4g',
    walltime= '12:00:00',
    account='piRNA') << f"""
maffilter param=/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/options_2.txt file=/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr2 sp1=Homo_sapiens sp2=Pan_troglodytes sp3=Gorilla_gorilla sp4=Pongo_abelii sp5=Nomascus_leucogenys sp6=Papio_anubis sp7=Pan_paniscus sp8=Lemur_catta ref=Homo_sapiens
"""
gwf.target(f"chr3_maffilter",
    inputs=['/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr3.maf.gz'],
    outputs=['/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/chr3.filtered.maf'],
    cores=1,
    memory='4g',
    walltime= '12:00:00',
    account='piRNA') << f"""
maffilter param=/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/options_2.txt file=/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr3 sp1=Homo_sapiens sp2=Pan_troglodytes sp3=Gorilla_gorilla sp4=Pongo_abelii sp5=Nomascus_leucogenys sp6=Papio_anubis sp7=Pan_paniscus sp8=Lemur_catta ref=Homo_sapiens
"""
gwf.target(f"chr4_maffilter",
    inputs=['/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr4.maf.gz'],
    outputs=['/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/chr4.filtered.maf'],
    cores=1,
    memory='4g',
    walltime= '12:00:00',
    account='piRNA') << f"""
maffilter param=/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/options_2.txt file=/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr4 sp1=Homo_sapiens sp2=Pan_troglodytes sp3=Gorilla_gorilla sp4=Pongo_abelii sp5=Nomascus_leucogenys sp6=Papio_anubis sp7=Pan_paniscus sp8=Lemur_catta ref=Homo_sapiens
"""
gwf.target(f"chr5_maffilter",
    inputs=['/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr5.maf.gz'],
    outputs=['/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/chr5.filtered.maf'],
    cores=1,
    memory='4g',
    walltime= '12:00:00',
    account='piRNA') << f"""
maffilter param=/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/options_2.txt file=/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr5 sp1=Homo_sapiens sp2=Pan_troglodytes sp3=Gorilla_gorilla sp4=Pongo_abelii sp5=Nomascus_leucogenys sp6=Papio_anubis sp7=Pan_paniscus sp8=Lemur_catta ref=Homo_sapiens
"""
gwf.target(f"chr6_maffilter",
    inputs=['/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr6.maf.gz'],
    outputs=['/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/chr6.filtered.maf'],
    cores=1,
    memory='4g',
    walltime= '12:00:00',
    account='piRNA') << f"""
maffilter param=/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/options_2.txt file=/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr6 sp1=Homo_sapiens sp2=Pan_troglodytes sp3=Gorilla_gorilla sp4=Pongo_abelii sp5=Nomascus_leucogenys sp6=Papio_anubis sp7=Pan_paniscus sp8=Lemur_catta ref=Homo_sapiens
"""
gwf.target(f"chr7_maffilter",
    inputs=['/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr7.maf.gz'],
    outputs=['/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/chr7.filtered.maf'],
    cores=1,
    memory='4g',
    walltime= '12:00:00',
    account='piRNA') << f"""
maffilter param=/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/options_2.txt file=/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr7 sp1=Homo_sapiens sp2=Pan_troglodytes sp3=Gorilla_gorilla sp4=Pongo_abelii sp5=Nomascus_leucogenys sp6=Papio_anubis sp7=Pan_paniscus sp8=Lemur_catta ref=Homo_sapiens
"""
gwf.target(f"chr8_maffilter",
    inputs=['/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr8.maf.gz'],
    outputs=['/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/chr8.filtered.maf'],
    cores=1,
    memory='4g',
    walltime= '12:00:00',
    account='piRNA') << f"""
maffilter param=/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/options_2.txt file=/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr8 sp1=Homo_sapiens sp2=Pan_troglodytes sp3=Gorilla_gorilla sp4=Pongo_abelii sp5=Nomascus_leucogenys sp6=Papio_anubis sp7=Pan_paniscus sp8=Lemur_catta ref=Homo_sapiens
"""
gwf.target(f"chr9_maffilter",
    inputs=['/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr9.maf.gz'],
    outputs=['/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/chr9.filtered.maf'],
    cores=1,
    memory='4g',
    walltime= '12:00:00',
    account='piRNA') << f"""
maffilter param=/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/options_2.txt file=/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr9 sp1=Homo_sapiens sp2=Pan_troglodytes sp3=Gorilla_gorilla sp4=Pongo_abelii sp5=Nomascus_leucogenys sp6=Papio_anubis sp7=Pan_paniscus sp8=Lemur_catta ref=Homo_sapiens
"""
gwf.target(f"chr10_maffilter",
    inputs=['/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr10.maf.gz'],
    outputs=['/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/chr10.filtered.maf'],
    cores=1,
    memory='4g',
    walltime= '12:00:00',
    account='piRNA') << f"""
maffilter param=/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/options_2.txt file=/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr10 sp1=Homo_sapiens sp2=Pan_troglodytes sp3=Gorilla_gorilla sp4=Pongo_abelii sp5=Nomascus_leucogenys sp6=Papio_anubis sp7=Pan_paniscus sp8=Lemur_catta ref=Homo_sapiens
"""
gwf.target(f"chr11_maffilter",
    inputs=['/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr11.maf.gz'],
    outputs=['/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/chr11.filtered.maf'],
    cores=1,
    memory='4g',
    walltime= '12:00:00',
    account='piRNA') << f"""
maffilter param=/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/options_2.txt file=/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr11 sp1=Homo_sapiens sp2=Pan_troglodytes sp3=Gorilla_gorilla sp4=Pongo_abelii sp5=Nomascus_leucogenys sp6=Papio_anubis sp7=Pan_paniscus sp8=Lemur_catta ref=Homo_sapiens
"""
gwf.target(f"chr12_maffilter",
    inputs=['/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr12.maf.gz'],
    outputs=['/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/chr12.filtered.maf'],
    cores=1,
    memory='4g',
    walltime= '12:00:00',
    account='piRNA') << f"""
maffilter param=/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/options_2.txt file=/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr12 sp1=Homo_sapiens sp2=Pan_troglodytes sp3=Gorilla_gorilla sp4=Pongo_abelii sp5=Nomascus_leucogenys sp6=Papio_anubis sp7=Pan_paniscus sp8=Lemur_catta ref=Homo_sapiens
"""
gwf.target(f"chr13_maffilter",
    inputs=['/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr13.maf.gz'],
    outputs=['/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/chr13.filtered.maf'],
    cores=1,
    memory='4g',
    walltime= '12:00:00',
    account='piRNA') << f"""
maffilter param=/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/options_2.txt file=/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr13 sp1=Homo_sapiens sp2=Pan_troglodytes sp3=Gorilla_gorilla sp4=Pongo_abelii sp5=Nomascus_leucogenys sp6=Papio_anubis sp7=Pan_paniscus sp8=Lemur_catta ref=Homo_sapiens
"""
gwf.target(f"chr14_maffilter",
    inputs=['/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr14.maf.gz'],
    outputs=['/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/chr14.filtered.maf'],
    cores=1,
    memory='4g',
    walltime= '12:00:00',
    account='piRNA') << f"""
maffilter param=/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/options_2.txt file=/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr14 sp1=Homo_sapiens sp2=Pan_troglodytes sp3=Gorilla_gorilla sp4=Pongo_abelii sp5=Nomascus_leucogenys sp6=Papio_anubis sp7=Pan_paniscus sp8=Lemur_catta ref=Homo_sapiens
"""
gwf.target(f"chr15_maffilter",
    inputs=['/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr15.maf.gz'],
    outputs=['/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/chr15.filtered.maf'],
    cores=1,
    memory='4g',
    walltime= '12:00:00',
    account='piRNA') << f"""
maffilter param=/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/options_2.txt file=/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr15 sp1=Homo_sapiens sp2=Pan_troglodytes sp3=Gorilla_gorilla sp4=Pongo_abelii sp5=Nomascus_leucogenys sp6=Papio_anubis sp7=Pan_paniscus sp8=Lemur_catta ref=Homo_sapiens
"""
gwf.target(f"chr16_maffilter",
    inputs=['/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr16.maf.gz'],
    outputs=['/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/chr16.filtered.maf'],
    cores=1,
    memory='4g',
    walltime= '12:00:00',
    account='piRNA') << f"""
maffilter param=/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/options_2.txt file=/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr16 sp1=Homo_sapiens sp2=Pan_troglodytes sp3=Gorilla_gorilla sp4=Pongo_abelii sp5=Nomascus_leucogenys sp6=Papio_anubis sp7=Pan_paniscus sp8=Lemur_catta ref=Homo_sapiens
"""
gwf.target(f"chr17_maffilter",
    inputs=['/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr17.maf.gz'],
    outputs=['/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/chr17.filtered.maf'],
    cores=1,
    memory='4g',
    walltime= '12:00:00',
    account='piRNA') << f"""
maffilter param=/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/options_2.txt file=/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr17 sp1=Homo_sapiens sp2=Pan_troglodytes sp3=Gorilla_gorilla sp4=Pongo_abelii sp5=Nomascus_leucogenys sp6=Papio_anubis sp7=Pan_paniscus sp8=Lemur_catta ref=Homo_sapiens
"""
gwf.target(f"chr18_maffilter",
    inputs=['/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr18.maf.gz'],
    outputs=['/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/chr18.filtered.maf'],
    cores=1,
    memory='4g',
    walltime= '12:00:00',
    account='piRNA') << f"""
maffilter param=/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/options_2.txt file=/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr18 sp1=Homo_sapiens sp2=Pan_troglodytes sp3=Gorilla_gorilla sp4=Pongo_abelii sp5=Nomascus_leucogenys sp6=Papio_anubis sp7=Pan_paniscus sp8=Lemur_catta ref=Homo_sapiens
"""
gwf.target(f"chr19_maffilter",
    inputs=['/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr19.maf.gz'],
    outputs=['/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/chr19.filtered.maf'],
    cores=1,
    memory='4g',
    walltime= '12:00:00',
    account='piRNA') << f"""
maffilter param=/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/options_2.txt file=/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr19 sp1=Homo_sapiens  sp2=Pan_troglodytes sp3=Gorilla_gorilla sp4=Pongo_abelii sp5=Nomascus_leucogenys sp6=Papio_anubis sp7=Pan_paniscus sp8=Lemur_catta ref=Homo_sapiens
"""
gwf.target(f"chr20_maffilter",
    inputs=['/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr20.maf.gz'],
    outputs=['/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/chr20.filtered.maf'],
    cores=1,
    memory='4g',
    walltime= '12:00:00',
    account='piRNA') << f"""
maffilter param=/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/options_2.txt file=/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr20 sp1=Homo_sapiens sp2=Pan_troglodytes sp3=Gorilla_gorilla sp4=Pongo_abelii sp5=Nomascus_leucogenys sp6=Papio_anubis sp7=Pan_paniscus sp8=Lemur_catta ref=Homo_sapiens 
"""
gwf.target(f"chr21_maffilter",
    inputs=['/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr21.maf.gz'],
    outputs=['/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/chr21.filtered.maf'],
    cores=1,
    memory='4g',
    walltime= '12:00:00',
    account='piRNA') << f"""
maffilter param=/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/options_2.txt file=/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr21 sp1=Homo_sapiens  sp2=Pan_troglodytes sp3=Gorilla_gorilla sp4=Pongo_abelii sp5=Nomascus_leucogenys sp6=Papio_anubis sp7=Pan_paniscus sp8=Lemur_catta ref=Homo_sapiens
"""
gwf.target(f"chr22_maffilter",
    inputs=['/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr22.maf.gz'],
    outputs=['/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/chr22.filtered.maf'],
    cores=1,
    memory='4g',
    walltime= '12:00:00',
    account='piRNA') << f"""
maffilter param=/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/options_2.txt file=/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr22 sp1=Homo_sapiens sp2=Pan_troglodytes sp3=Gorilla_gorilla sp4=Pongo_abelii sp5=Nomascus_leucogenys sp6=Papio_anubis sp7=Pan_paniscus sp8=Lemur_catta ref=Homo_sapiens
"""
gwf.target(f"chrX_maffilter",
    inputs=['/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chrX.maf.gz'],
    outputs=['/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/chrX.filtered.maf'],
    cores=1,
    memory='4g',
    walltime= '12:00:00',
    account='piRNA') << f"""
maffilter param=/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/options_2.txt file=/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chrX sp1=Homo_sapiens sp2=Pan_troglodytes sp3=Gorilla_gorilla sp4=Pongo_abelii sp5=Nomascus_leucogenys sp6=Papio_anubis sp7=Pan_paniscus sp8=Lemur_catta ref=Homo_sapiens
"""

def filter_species(raw_data):
    inputs = [f'{raw_data}.maf.gz']
    options = {"account":"piRNA", "memory":"120gb"}
    spec = '''
    maffiter param=/home/juliasalas/piRNA/Workspaces/julia/sequence_diversity/options_2.txt file={} sp1=Homo_sapiens sp2=Pan_troglodytes sp3=Gorilla_gorilla_gorilla sp4=Pongo_abelii sp5=Nomascus_leucogenys sp6=Papio_anubis sp7=Pan_paniscus sp8=Lemur_catta ref=Homo_sapiens output="/home/juliasalas/piRNA/Workspaces/juliasalas/seqeuence_diversity/filtered/"
    '''.format(raw_data)
    return inputs, options, spec

input_data="/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier"
chromosomes=["chr1","chr2","chr3","chr4","chr5","chr6","chr7","chr8","chr9","chr10","chr11","chr12","chr13","chr14","chr15","chr16","chr17","chr18","chr19","chr20","chr21","chr22","chrX"]
for number in chromosomes:
    raw_data=f'{input_data}/{number}'
    gwf.target_from_template(f'filter_{number}',
        filter_species(raw_data))