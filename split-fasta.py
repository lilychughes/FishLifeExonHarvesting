#!/usr/bin/env python

import argparse
import re
from sys import argv

###### Documentation

parser = argparse.ArgumentParser(description="Requires python 2.7 and biopython. Splits a multifasta file into single fasta file.")
parser.add_argument('-f', '--fasta' , dest = 'fasta' , type = str , default= None , required= True, help = 'Multifasta to process')
parser.add_argument('-c', '--clean' , dest = 'clean' , type = str , default= 'True' , required= False, help = 'If true, leaves only the taxon name')
parser.add_argument('-s', '--separator' , dest = 'separator' , type = str , default= '|' , required= False, help = 'Character that separates the taxon name and the gene name.')
args, unknown = parser.parse_known_args()


import Bio
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

for seq_record in SeqIO.parse(args.fasta , "fasta"):
	species = seq_record.id.split(args.separator)[0]
	locus = seq_record.id.split(args.separator)[1]
	if 'True' in args.clean:
		clean_seq = SeqRecord(seq_record.seq, id=species, description='')
		output = open(species+"."+locus+".fa" , "w")
		output.write(clean_seq.format("fasta"))
		output.close()
	else:
		output = open(species+"."+locus+".fa" , "w")
		output.write(seq_record.format("fasta"))
		output.close()