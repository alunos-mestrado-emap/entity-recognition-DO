#!/bin/bash

# converts all pdf files in the current directory using pdfminer's
# pdf2txt utility

for f in *.pdf;
do
    pdf2txt.py -o ${f%.pdf}.txt ${f}
done
