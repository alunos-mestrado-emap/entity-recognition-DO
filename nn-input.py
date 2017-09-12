"""
NN demands as input a sentence per line, with each token being separated by a space.
"""

#
## build input to neural network model
import os
import nltk
nltk.download('punkt')

def preprocess_sent(text):
    return [token.strip() for token in nltk.tokenize.word_tokenize(text)]

def ato_to_sents(text):
    return nltk.sent_tokenize(text, language='portuguese')

def process_ato(ato):
    return map(lambda x: ' '.join(preprocess_sent(x)), ato_to_sents(ato))

def split_in_atos(text, separator="---"):
    return text.split(separator)

def atos_to_string(atos):
    return '\n\n'.join(map(lambda x: '\n'.join(process_ato(x)), atos))

def atos_string_to_input(atos, filepath):
    with open(filepath, 'w') as f:
        f.write(atos)

def do_to_input(filepath):
    dirname, filename = os.path.split(filepath)
    with open(filepath, 'r') as f:
        atos_text = f.read()
        atos = split_in_atos(atos_text)
        atos_str = atos_to_string(atos)
        atos_string_to_input(atos_str, os.path.join(dirname, 'input-'+filename))
