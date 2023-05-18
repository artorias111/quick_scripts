#!/usr/bin/python3
#Author : Shriram Bhat 
#email : alekhshriram@gmail.com
#python script to take a gtf output (ex from an annotation pipeline such as BRAKER or TSEBRA), and return the length of intergenic sequences (with coordinates and scaffold names)
#input : a gtf file, from a tsebra output

#output : a tsv file with `scaffold_name\tstart\tend\tlength\tprevious_gene\tnext_gene

#import the packages
import re
import argparse

#input the gtf file using argparse
parser = argparse.ArgumentParser()
parser.add_argument('--gtf', type=str, required=True)
args = parser.parse_args()
temp4=0
temp_gene='none'
#start_pos,end_pos=[],[]
my_file=open(args.gtf)
my_outfile=open('intergenic_gaps.tsv','w')
my_outfile.write('Scaffold\tstart_pos\tend_pos\tintergenic_length\tupstream_gene\tdownstream_gene\n')
for line in my_file:
	if re.search('gene\s',line):
		elements=line.split()
		diff=int(elements[3])-temp4
		out_line=elements[0]+'\t'+str(temp4)+'\t'+elements[3]+'\t'+str(diff)+'\t'+temp_gene+'\t'+elements[8]
		if diff<0:
			print('checking next scaffold')
		else:
			my_outfile.write(out_line+'\n')
		temp4=int(elements[4])
		temp_gene=elements[8]
my_file.close()
my_outfile.close()
