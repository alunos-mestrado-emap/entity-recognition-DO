#!/bin/bash
for file in *.pdf
do
pdf2txt.py $file > ${file%.pdf}.txt
done
