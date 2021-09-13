import sys
from tqdm import tqdm

try:
    input_file = sys.argv[1]
except:
    print("please specify file")
    exit()

f = open(input_file,"r")
sf = open("separated_" + input_file,"w")
file_string = f.read()

lines = file_string.split("\n")
sf.write(lines[0])
sf.write("\n")
lines = lines[1:]

for l in tqdm(lines):
    if l[0:2] == "1\t":
        sf.write("\n")
        sf.write(l)
        sf.write("\n")
    else:
        sf.write(l)
        sf.write("\n")

sf.close()