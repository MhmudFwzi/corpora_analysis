import pyconll

conll_file_location = './de_gsd-ud-train.conllu'
train = pyconll.load_from_file(conll_file_location)

for sentence in train:
    potential_mistakes = set()
    for token in sentence:
        if token.xpos == "PRELAT" or token.xpos == "PRELS":
            potential_mistakes.add(token.head)
    for token in sentence:
        if token.id in potential_mistakes:
            if token.deprel == "acl":
                print(sentence.id)
                token.deprel = "acl:relcl"

with open('de_gsd-ud-train_fixed.conllu', 'w', encoding='utf-8') as f:
    train.write(f)