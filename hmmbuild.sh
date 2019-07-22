#!/bin/sh


# Run in directory of ONLY gene alignments. 

for f in *;
do
hmmbuild --dna --informat afa  -o ${f%.*}.build.out ${f%.*}.hmm $f;
done

