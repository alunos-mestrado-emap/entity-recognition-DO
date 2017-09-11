"""
this is a hacky script to read CoNLL-U format files and output them in 
the format needed for NER.

if you are using the bosque sintá(c)tico version, where some multiword tokens are marked with '=' (e.g., além=de), running:

cat transfbosque_CP.udep.conll | sed 's/=/\t0\n/' > transfCP.conllu

should solve your problem.

"""

import csv
import os

def should_print(element, ix=None):
    if element == 'PROPN':
        return element
    else:
        return '0'

def ownpt_conllu_transform(filepath):
    if not os.path.isfile(filepath):
        raise Exception("not file.")
    dirpath, filename = os.path.split(filepath)
    output_path = os.path.join(dirpath, 'transf'+filename)
    with open(filepath,'r') as tsvin, open(output_path, 'w') as tsvout:
        tsvin = csv.reader(tsvin, delimiter='\t')
        tsvout = csv.writer(tsvout, delimiter='\t')
        for row in tsvin:
            if not row:
                tsvout.writerow(row)
            elif row[0][0] == '#':
                continue
            else:
                tsvout.writerow([row[1], should_print(row[3])])
                indices = row[0].split('-')
                if len(indices) == 2:
                    start, end = map(lambda x: int(x), indices)
                    for i in range(start, end + 1):
                        next(tsvin)

def ud_should_print(element, ix=None):
    if element == 'PROPN' and ix == 0:
        return 'B-' + element
    elif element == 'PROPN':
        return 'I-' + element
    else:
        return '0'

def ud_conllu_transform(filepath):
    if not os.path.isfile(filepath):
        raise Exception("not file.")
    dirpath, filename = os.path.split(filepath)
    output_path = os.path.join(dirpath, 'transf'+filename)
    with open(filepath,'r') as tsvin, open(output_path, 'w') as tsvout:
        tsvin = csv.reader(tsvin, delimiter='\t')
        tsvout = csv.writer(tsvout, delimiter='\t')
        for row in tsvin:
            if not row:
                tsvout.writerow(row)
            # several mistakes in ud files which cause newlines where there shouldn't be one
            elif row[0][0] not in '0123456789':
                continue
            else:
                tokens = row[1].split('_')
                for ix, token in enumerate(tokens):
                    tsvout.writerow([token, ud_should_print(row[3], ix)])

def dir_conllu_transform(dirpath, transf_function):
    if not os.path.isdir(dirpath):
        raise Exception('must be directory.')
    for file in os.scandir(dirpath):
        if file.name.endswith(".conllu") or file.name.endswith(".conll"):
            transf_function(file.path)
        else:
            continue
                    
