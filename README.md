# FishLifeExonHarvesting
Scripts for mining exons from genomes or transcriptomes. See Hughes et al. (2018) in PNAS for marker details.


## This pipeline is meant to mine exon markers from genomes and transcriptomes using nhmmer.

### Software required:
biopython
nhmmer


# Step 0: Organize your files

You will need fasta-formatted alignments of the exons you want to mine for some set of taxa, and fasta files of the genomes & transcriptomes you want to mine. If you want to download the coding sequences only of the genome you want to mine, it will probably run faster, but this will also work with unannotated genomic scaffolds.

You need three directories, all side-by-side. The first is this github repository. The second is a directory called hmm. The third is a directory for all your genomes and transcriptomes. Call this whatever you like, as long as it is meaningful to you. Below I will refer to this as the 'Project' directory.

```
mkdir hmm
mkdir Project
```

Move all the fasta files of your genomes and transcriptomes into the Project directory. These fasta files need to be named in a manner that is meaningful to you, and end in .fasta. __Do not use special characters or spaces in naming your fasta files, only letters, numbers, or underscores.__ The names you give these files will be how they are named in the final alignments. I like to name them like this:

Family_Genus_species_AccessionNumber12345.fasta

Each genome/transcriptome is going to get it's own directory to hold all the output files within the Project directory. You can set that up like this:

```
cd Project/

for f in *.fasta;
do 
mkdir ${f%.*};
mv $f ${f%.*}/;
done
```

