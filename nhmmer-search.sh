#!/bin/sh


# loops over directories to perform nhmmer search on each exon

for directory in *;
do
if [  -d $directory  ];
then
if [  ! -e $directory.nhmmer.txt  ];
then
echo nhmmer search started $directory > $directory.nhmmer.txt;
cd $directory;
cp ../hmm/*.hmm .
for hmm in *hmm;
do
nhmmer --tblout $hmm-hits.txt --noali -T 100 -cpu 2 --dna $hmm $directory.fasta;
done;
rm *.hmm;
cat *-hits.txt > $directory-hits.txt;
cd ../;
echo nhmmer search finished $directory >> $directory.nhmmer.txt ;
fi;
fi;
done