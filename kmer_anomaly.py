#!/usr/bin/env python3

# Python script to work out weird k-mer plots
# input : Raw reads in fastq (UNCOMPRESSED -sorry, Sloppy coding), peak threshold as seen in k-mer coverage plot, and k-mer size (path, int, int)
# output : fastq in stdout containing reads consisting of high frequency (erroneous?) kmers. Pipe to gzip to compress

# Example run : kmer_anomaly.py --reads pacbio_ccs_reads.fastq --kmer 51 --peak 60
import argparse
from collections import defaultdict

def get_fastq_seqs(filepath):
    with open (filepath,'r') as f :
        # Sequence dictionary stored as header:sequence
        fq_seq={} 
        # Sequence dictionary stored as header:phred scores
        fq_phred={} 
        for line in f:
            l=line.strip()
            if l=="":
                continue
            if l[0]=="@":
                fq_seq[l[1:]]=""
                fq_phred[l[1:]]=""
                tmp=l[1:]
                ctr=1
                continue
            if l[0]=="+":
                ctr=0
                continue
            if ctr==1:
                fq_seq[tmp]+=l
                ctr=0
                continue
            else:
                fq_phred[tmp]+=l
                ctr=0
    return fq_seq,fq_phred
            

def kmerize(seq,k):
    # input is a string (a sequence, not a fasta file) and a k-mer size
    # output : list of k-mers
    l=[] # list of k-mers to return
    for i in range(0,len(seq)-k+1):
        l.append(seq[i:i+k])
    return l


if __name__=="__main__":
    #argparse stuff
    parser=argparse.ArgumentParser()
    parser.add_argument('--reads','-r',type=str,required=True)
    parser.add_argument('--kmer','-k',type=int,required=True)
    parser.add_argument('--peak','-p',type=int,required=True)
    args=parser.parse_args()
    
    peak_value=args.peak
    kmer_size=args.kmer
    f,_=get_fastq_seqs(args.reads)

    #print(kmerize("ATTGTGTGTGT",4))
    d=defaultdict(list) # d[header]=kmerize(seq)
    freq_k=defaultdict(int) # dictionary of frequencies of each k-mer

    potential_errenious_reads=[]

    for i in f:
        # fasta header: k-mers
        d[i]=kmerize(f[i],kmer_size)
        for j in d[i]:
            freq_k[j]+=1
            if freq_k[j]>peak_value:
                # potential_errenious_reads.append(i) # or just print this if you don't want to save it in memory
                print(i)
                break # if you don't use break : do | sort | uniq -c | sort -nrk 1
            # in the current state, it works like : if there's one k-mer in a read that has the frequency below the threshold, that read is in stdout (I hope this makes sense to me a week from now)
