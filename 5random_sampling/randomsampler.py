import pyconll
import os
import random

folder_path = "./"

sample = pyconll.load_from_file(folder_path + "fixed_acl_sc1650de_..conllu")

for f in os.listdir(folder_path):
    sample.clear()
    print(f)
    big_file_iterator = pyconll.iter_from_file(folder_path + f)
    try:
        big_file_length =  sum(1 for _ in big_file_iterator)
    except:
        print("Format error, iterator crashed")
        continue
    print(big_file_length)
    random_indices = []
    for i in range(20):
        r = random.randint(0, big_file_length)
        random_indices.append(r)
    big_file_iterator = pyconll.iter_from_file(folder_path + f)
    for i,s in enumerate(big_file_iterator):
        if i in random_indices:
            sample.append(s)
    with open(f + "_20_samples.conllu", 'w', encoding='utf-8') as wr:
        sample.write(wr)
