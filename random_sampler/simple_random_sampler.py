import pyconll
import os
import random

folder_path = "./1800/"

for f in os.listdir(folder_path):
    print(f)
    train = pyconll.load_from_file(folder_path + f)
    x = pyconll.load_from_file(folder_path + f)
    x.clear()
    for i in range(20):
        r = random.randint(0,len(train))
        x.append(train[r])
        with open(f + "_20_samples.conllu", 'w', encoding='utf-8') as wr:
            x.write(wr)
