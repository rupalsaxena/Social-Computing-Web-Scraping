# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import runpy

import nltk

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')


def text_parser_synonym_finder(text: str):
    from nltk.tokenize import word_tokenize
    from nltk.corpus import wordnet
    from collections import defaultdict
    import pprint

    tokens = word_tokenize(text)
    synonyms = defaultdict(list)
    for token in tokens:
        for syn in wordnet.synsets(token):
            for i in syn.lemmas():
                synonyms[token].append(i.name())
    pprint.pprint(dict(synonyms))
    synonym_output = pprint.pformat((dict(synonyms)))
    with open(str(text[:5]) + ".csv", "a") as f:
        f.write("Starting of Synonyms of the Words from the Sentences: " + synonym_output + "\n")
        f.close()



feminine = open('Feminine_start_point.txt', 'r').read()
text_parser_synonym_finder(feminine)

masculine = open('Masculine_start_point.txt', 'r').read()
text_parser_synonym_finder(masculine)

older = open('older_stereotypes.txt', 'r').read()
text_parser_synonym_finder(older)

younger = open('younger_stereotypes.txt', 'r').read()
text_parser_synonym_finder(younger)