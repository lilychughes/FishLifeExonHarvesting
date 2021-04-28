#!/bin/sh


# loops over directories to perform nhmmer search on each exon, and retrieves fasta entries for the best hits.

for directory in *;
do
if [  -d $directory  ];
then
if [  ! -e $directory.nhmmer.txt  ];
then
echo nhmmer search started $directory > $directory.nhmmer.txt;
cd $directory;
cp ../../hmm/*.hmm .
for hmm in *hmm;
do
nhmmer --tblout $hmm-hits.txt --noali -T 100 --cpu 2 --dna $hmm $directory.fasta;
done;
rm *.hmm;
cat *-hits.txt > $directory-hits.txt;
python2.7 ../../FishLifeExonHarvesting/nhmmer2fasta.py -f $directory.fasta -i $directory-hits.txt;
python2.7 ../../FishLifeExonHarvesting/split-fasta.py -f $directory.hits.fasta;
cd ../;
echo nhmmer search finished $directory >> $directory.nhmmer.txt ;
fi;
fi;
done
