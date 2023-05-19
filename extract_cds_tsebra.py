#!/home/sb65/miniconda3/bin/python3
#extract only the cds and output as a fasta sequence from the output of TSEBRA

#accept a file through the command line
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--tsebra', '-t', type=str, required=True)
parser.add_argument('--fasta', '-f', type=str,required=True)
args = parser.parse_args()

#tsebra_file=open(args.tsebra)
#fasta_file=open(args.fasta)

#linearize the fasta
#conda activate samtools (if in polar)
os.system('seqkit seq -w 0')
