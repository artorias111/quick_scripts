#!/home/sb65/miniconda3/bin/python
#a python script to accept a nucleotide sequence (FASTA) and a k-merize size, and output all the kmers (not just the unique ones, use unixtools later on the output if you want unique k-mers) as a text file

#input : path to a fasta file (string), kmer size (int)
#output : fasta file containing all the k-mers

import argparse

#argparse stuff
parser=argparse.ArgumentParser()
parser.add_argument('--fasta','-f',type=str,required=True)
parser.add_argument('--kmer','-k',type=int,required=True)
args=parser.parse_args()

####process fasta####
sequence=''
header_name=''
my_file=open(args.fasta)
for i in my_file:
	raw_string=str(i).strip()
	if raw_string[0]=='>':
		header_name=raw_string
		continue
	sequence+=raw_string
my_file.close()

#open the output file
out_file=open('kmerize_out.fa','w')

#rest of the code
k=args.kmer
for i in range(len(sequence)-k+1):
	j=i+k
	#print(sequence[i:j])
	out_file.write(header_name+'_kmer_'+str(i))
	out_file.write('\n')
	out_file.write(sequence[i:j])
	out_file.write('\n')

out_file.close()
