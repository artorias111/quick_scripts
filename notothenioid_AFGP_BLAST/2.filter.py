#!/usr/bin/python3

file=open('genes_list_sorted.tsv','r')
hsl,tomm40=0,0 #counters for the number of hsl and tomm40 entries in the blast results
ctr=0 #counter to keep  a record of the headers
for i in file:
    if ctr==0:
        head=i.strip().split()
    x=i.strip().split()
    if x[0]=='DmHSL_Glean_2499nt':
        hsl+=1
    else:
        hsl_final=hsl
        hsl=0
    if x[0]=='DmH1TOMM40_1008nt':
        tomm40+=1
    else:
        tomm40_final=tomm40
        tomm40=0
    ctr+=1

print(hsl_final,tomm40_final)
