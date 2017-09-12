"""
this is a very dirty script for renaming some DO's from prefeitura municipal de mesquita. 
because this is specific to a few DOs, I haven't taken the time to clean up the code, 
make it efficient or anything of the sort.
"""
import os
import dateutil.parser as dparser
import datetime as dt


day_first_parser = lambda x: dparser.parse(x, fuzzy=True, dayfirst=True)

def replace_month(filename):
    dictionary = {'janeiro':'01', 'fevereiro':'02', 'março':'03', 'abril':'04', 'maio':'05', 'junho':'06', 'julho':'07', 'agosto':'08', 'setembro':'09', 'outubro':'10', 'novembro':'11', 'dezembro':'12'}
    for key in dictionary:
        if filename.find(key) != -1:
            return filename.replace('de-{}-de'.format(key), dictionary[key])


def rename_dos():
    for root, dirs, files in os.walk("../dos/"):
        for ix, name in enumerate(files):
            if name[:4] == '2017':
                os.rename(os.path.join(root,name), os.path.join(root,  dt.datetime.strptime(name[:8], '%Y%m%d').strftime('%Y-%m-%d')+'.pdf'))
            elif name[:8] == "PUBLICAÇ":
                os.rename(os.path.join(root,name), os.path.join(root, day_first_parser(replace_month(name)[15:25]).strftime('%Y-%m-%d')+'.pdf'))
            elif True:
                print(replace_month(name))
