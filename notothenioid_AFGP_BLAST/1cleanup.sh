#!/bin/bash
#Automate the filtering of AFGP blast output
#USAGE : ./1cleanup.sh blastout6.out

BLAST6_HEAD="qseqid  sseqid  pident  length  mismatch        gapopen qstart  qend    sstart  send    evalue  bitscore"

#Step 0 : Run blast, save the output as outfmt 6 (also remember to document the blast version)
#I'm gonna use the example Dmaw12_HSL-TOMM40_11genes.out throughout this snippet

#This is a blast6 output for the 11 AFGP genes query file
query=$1

#Step 1 : find out which scaffold the locus is in
scaffold=`cut -f 2 $query | sort -nk 1 | uniq -c | head -n 1 | awk '{print $2}'`
#Step 2 : Only filter out the scaffold you need, and add headers to export to R
grep $scaffold $query | awk -v h="$BLAST6_HEAD" 'BEGIN { print h } {print$0}' | awk '{print $1,$7,$8,$9,$10}' > genes_list.tsv

tmp_head=`head -n 1 genes_list.tsv`
grep -v "qseqid" genes_list.tsv | sort -nk 4 |awk -v h="$tmp_head" 'BEGIN { print h } {print$0}' > genes_list_sorted.tsv 
echo "Check the genes_list_sorted tsv file. The scaffold is $scaffold"
