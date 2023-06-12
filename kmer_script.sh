#!/bin/bash
#all directories are according to polar
#query has to be a fasta file with only a single fasta entry
#works only with nucleotide blast for now
#example run : ./kmerize_blast.sh -q x.fa -k 8 -s dele -d genome -o x.out


eleg_scaffold_db=/data/work/Notothenioids/comparative_data/afgp_loci_blast_db/dele_Hifi16/dele_ptg000021l
maw_scaffold_db=/data/work/Notothenioids/comparative_data/afgp_loci_blast_db/dmaw_bionano/dmaw_Super-Scaffold_100006

eleg_genome_db=/data/work/Notothenioids/Dele4/Dele4_CCS_cells1-3_reads/dec_22_assembly/Dele4_cells1-2-3.asm.p_ctg
maw_genome_db=/home/sb65/work/dmaw/genomes/dmaw_bionano/EXP_REFINEFINAL1_bppAdjust_cmap_Dmaw12_3cells_HifiasmV0_16_bp_p_ctg_fa_NGScontigs_HYBRID_SCAFFOLD

db=""

while getopts ':k:q:s:d:o:' OPTIONS; do
	case "$OPTIONS" in 
		k) #k-mer size
			k=$OPTARG
			;;
		q) # query fasta file
			q=$OPTARG
			;;
		s) #species
			s=$OPTARG
			#need a bunch of if statements here
			;;
		d) #genome or scaffold only blast database
			d=$OPTARG
			#more if statements
			;;
		o) #output file name (output is a blast result)
			o=$OPTARG
			;;

		*)
			exit_abnormal
			;;
	esac

echo $k
done

#../kmerize.py --query q --k k
#blastn --db db --query query_kmerized --out x.out outfmt 6
