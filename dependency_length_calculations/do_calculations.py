import sys
from tqdm import tqdm

try:
    input_file = sys.argv[1]
except:
    print("please specify file")
    exit()

f = open(input_file,"r")
analyzed_f = open("analyzed_" + input_file,"w")

file_string = f.read()
sentences = file_string.split("\n\n")

for sentence in tqdm(sentences):
    parse_lines = sentence.split("\n")
    words = []
    for line in parse_lines:
        if len(line.split("\t")) < 8:
            analyzed_f.write(line + "\n")
        else:
            words.append(line) 
    
    punctuation_indices = []
    for word in words:
        cells = word.split("\t")
        if cells[7] == "punct":
            punctuation_indices.append(int(cells[0]))
    
    length_without_punctuation = len(words) - len(punctuation_indices)
    dependency_lengths = []
    dependency_sum = 0
    
    for word in words:
        cells = word.split("\t")
        parent = int(cells[6])
        child = int(cells[0])
        dependency_length = abs(parent - child)
        for p in punctuation_indices:
            if p>min(parent,child) and p<max(parent,child):
                dependency_length = dependency_length - 1
        dependency_lengths.append(dependency_length)
        if cells[7].lower() != "punct" and cells[7].lower() != "root":
            dependency_sum += dependency_length
    try:
        dependency_avg = dependency_sum/(len(words) - len(punctuation_indices) - 1)
    except:
        dependency_avg = 0

    for i,word in enumerate(words):
        analyzed_f.write(word + "\t" + str(dependency_lengths[i]) + "\t" + str(length_without_punctuation) \
        + "\t" + str(dependency_sum) + "\t" + str(dependency_avg) + "\n")
    analyzed_f.write("\n")


analyzed_f.close()
