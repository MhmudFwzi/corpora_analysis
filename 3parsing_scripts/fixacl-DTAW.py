import pyconll
import sys

conll_file_location = sys.argv[1]
if conll_file_location == "sc1850de_..conllu" or conll_file_location == "sc1650de_..conllu":
    train = pyconll.iter_from_file(conll_file_location)
    f = open("fixed_acl_" + conll_file_location, 'w', encoding='utf-8')  
else:
    train = pyconll.load_from_file(conll_file_location)
    print("file loaded successfully")

for i,sentence in enumerate(train):
    potential_mistakes = set()
    for token in sentence:
        if token.xpos == "PRELAT" or token.xpos == "PRELS":
            potential_mistakes.add(token.head)
    for token in sentence:
        if token.id in potential_mistakes:
            if token.deprel == "acl":
                print(sentence.id)
                token.deprel = "acl:relcl"
    if i != 0:
        f.write("\n")
    f.write(sentence.conll() + "\n")
f.write("\n")

with open("fixed_acl_" + conll_file_location, 'w', encoding='utf-8') as f:
    train.write(f)