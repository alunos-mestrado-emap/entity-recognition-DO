import csv
import os
import itertools

def should_print(element):
    if element == 'PROPN':
        return element
    else:
        return '0'

def conllu_transform(filepath):
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

def dir_conllu_transform(dirpath):
    directory = os.fsencode(dirpath)
    if not os.path.isdir(directory):
        raise Exception('must be directory.')
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".conllu"): 
            conllu_transform(filename)
        else:
            continue
                    
