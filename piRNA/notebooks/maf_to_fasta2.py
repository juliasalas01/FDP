from Bio import AlignIO, SeqIO
from Bio.SeqRecord import SeqRecord
from collections import defaultdict

def maf_to_fasta(maf_file, output_file):
    # Create a dictionary to store sequences by species
    species_seqs = defaultdict(list)

    # Parse the MAF file
    alignments = AlignIO.parse(maf_file, "maf")

    # Iterate through each alignment
    for alignment in alignments:
        # Iterate through each sequence in the alignment
        for sequence in alignment:
            # Extract species name from sequence id
            species = sequence.id.split('.')[0]
            
            # Append the sequence to the corresponding species in the dictionary
            species_seqs[species].append(sequence.seq)

    # Create a list to store the concatenated sequences
    concat_seqs = []

    # Concatenate the sequences of each species
    for species, sequences in species_seqs.items():
        concat_seq = ''.join(sequences)
        record = SeqRecord(Seq(concat_seq), id=species, description='')
        concat_seqs.append(record)

    # Write the concatenated sequences to a FASTA file
    with open(output_file, 'w') as fasta_file:
        SeqIO.write(concat_seqs, fasta_file, "fasta")

maf_file = "/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr21.filtered.region.44468861.maf"
fasta_file = "/home/juliasalas/piRNA/PrimaryData/primate.multiz_tarsier/chr21.filtered.region.44468861.fasta"
maf_to_fasta(maf_file, fasta_file)
