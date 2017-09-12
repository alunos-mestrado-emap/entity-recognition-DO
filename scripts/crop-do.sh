#!/bin/bash

# crops all pdf files (meant to be Mesquita's DOs) in current
# directory so that they have their headers and footers removed

mkdir -p cropped
for f in *.pdf;
do
   output_name=$(pwd)/cropped/$(basename ${f}) &&
   gs -o ${output_name} -sDEVICE=pdfwrite \
      -c "[/CropBox [0 50 595.32 710]" \
      -c " /PAGES pdfmark" -f ${f};
done
