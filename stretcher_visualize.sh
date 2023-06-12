#!/bin/bash
#visualize emboss stretcher output on a smaller scale
# match (stacked based on match length input) : | ; gap (stacked based on gap length input) : _
#usage : ./stretcher_visualizer.sh <filename.stretcher>[[necessary]] <match length>[[optional, default 9]] <gap length>[[optional, default 3]]

file=$1
match=${2:-9}
gap=${3:-3}
echo "Stretcher file : $file"
echo "Match length : $match ; gap length : $gap"
grep -v "#" $file | grep ":" | sed 's/^[ \t]*//' | tr -d '\n' | sed -E s"/:{$match,}/M/g" | sed -E s"/ {$gap,}/G/g" | sed s'/://g' | sed -E s'/ {1,}//g' | sed s'/M/|/'g | sed s'/G/_/g'
echo ""
