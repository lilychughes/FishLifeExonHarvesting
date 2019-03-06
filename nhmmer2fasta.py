#!/usr/bin/env python
from __future__ import division
import re
from sys import argv
import argparse

##### Documentation #####

parser = argparse.ArgumentParser(description="Requires python 2.7 and Biopython. Returns fasta file of the top hit of nhmmer search.")
parser.add_argument('-i', '--input' , dest = 'input' , type = str , default= None , required= True, help = 'Tabular output from nhmmer search')
parser.add_argument('-f', '--fasta' , dest = 'fasta' , type = str , default= None , required= True, help = 'Fasta file of reference genome')
args, unknown = parser.parse_known_args()


##########################
import Bio
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord



# Open the result from the nhmmer search

nhmmer = open(args.input)
name = args.input.split(".")[0]
taxon_id = name.split("-")[0]

hits = []

filtered_hits = []

loci = []

# Process lines of input, save lines that contain hits (they don't start with a '#'), and remove extra spaces  

for line in nhmmer:	
	if line.startswith("#"):	
		pass	
	else:		
		single_spaces = re.sub(" +"," ", line)		
		locus = single_spaces.split(" ")[2]		
		if locus not in loci:		
			hits.append(single_spaces)			
			loci.append(locus)
		
nhmmer.close()

# If the file contains no hits

if len(hits) == 0:
	print("No hits found for locus" + locus_id)

# Process hits

else:
	reference = open(args.fasta)
	seq_dict = SeqIO.to_dict(SeqIO.parse(reference, "fasta"))
	reference.close()
	for line in hits:
		columns = line.split(" ")		
		scaffold = columns[0]		
		query_locus = columns[2]		
		align_start = int(columns[6]) - 1		
		align_end = int(columns[7]) - 1		
		align_len = abs(align_start - align_end)		
# only return hits above 100 bp		
		if align_len >= 100:		
			if align_start < align_end:			
				seq_record = seq_dict[scaffold]				
				seq_slice = seq_record.seq[align_start:align_end]				
				new_seq_record = SeqRecord(seq_slice, id = taxon_id + "|" + query_locus)
				filtered_hits.append(new_seq_record)		
# reverse complement sequences if necessary
			elif align_start > align_end:                              				
				seq_record = seq_dict[scaffold]				
				whole_seq = seq_record.seq				
				seq_revcomp = whole_seq.reverse_complement()				
				seq_length = len(whole_seq)				
				new_start = seq_length - align_start -1				
				new_end = new_start + align_start - align_end -1				
				seq_slice = seq_revcomp[new_start:new_end]	
				new_seq_record = SeqRecord(seq_slice, id = taxon_id + "|" + query_locus) 	
				filtered_hits.append(new_seq_record)	

if len(filtered_hits) > 0:	
	myfasta = open(taxon_id + ".single.hits" + ".fasta", "w")	
	for entry in filtered_hits:
		myfasta.write(entry.format("fasta"))