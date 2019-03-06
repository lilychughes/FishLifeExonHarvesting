#!/bin/sh



# move to hmm directory

cd hmm/

# Run in directory of ONLY gene alignments. 

for f in *;
do
hmmbuild --dna --informat afa  -o ${f%.*}.build.out ${f%.*}.hmm $f;
done

# Move back into the project directory

cd ../