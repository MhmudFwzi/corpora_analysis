import xml.etree.ElementTree as ET
import os

#with open("RSC_V6_0_4_OPEN_GS.vrt") as f:
with open("RSC_V4_0_0.vrt") as f:
    lines = f.readlines()

try: os.mkdir("english_documents")
except:
    print("Folder already exists or no access is given")

n_lines = len(lines)
append_flag = False
document = ""
title = ""
counter = 0

for i,l in enumerate(lines):
    if l[0:5] == "<text":
        counter+=1
        append_flag = True
        try: title = l.split("title=")[1][1:].split("\"")[0][0:150] + "_" + l.split("year=")[1][1:5] + ".vrt"
        except: title = l.split("title=")[1][1:].split("\"")[0] + "_" + l.split("year=")[1][1:5] + ".vrt"
        title = title.replace("/","")
        #handle possible same title problem by adding number
    if append_flag == True:
        document += l
    if l[0:6] == "</text":
        while_iterator = 0
        while os.path.isfile("english_documents/" + title):
            title = title[0:-10-while_iterator] + title[-9-while_iterator:]
            print(title)
        while_iterator = 0
        with open("english_documents/" + title,"w") as f:
            f.write(document)
        append_flag = False
        document = ""
        title = ""
        #counter+=1
        print(str(i+1) + "/" + str(n_lines))

print(str(counter) + " texts parsed")
print(str(len(os.listdir("english_documents/"))) + " files created")
