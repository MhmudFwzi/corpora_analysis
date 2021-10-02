import os

try: os.mkdir("german_documents")
except:
    print("Folder already exists or no access is given")

def parse_large_file(in_file):
    append_flag = False
    document = ""
    title = ""
    counter = 0
    i = 0
    while True:
        l = in_file.readline()
        i += 1
        if l[0:4] == "<,s>":
            document += "</s>"
            continue
        if l[0:5] == "<text":
            counter+=1
            append_flag = True
            try: title = l.split("title=")[1][1:].split("\"")[0][0:150] + "_" + l.split("year=")[1][1:5] + ".vrt"
            except: title = l.split("title=")[1][1:].split("\"")[0] + "_" + l.split("year=")[1][1:5] + ".vrt"
            title = title.replace("/","")
            #handle possible same title problem by adding number
        if append_flag == True:
            if l[0:6] == "<,text":
                document += "</text>"
            else:
                document += l
        if l[0:6] == "<,text":
            print(i)
            while_iterator = 0
            while os.path.isfile("german_documents/" + title):
                title = title[0:-10-while_iterator] + title[-9-while_iterator:]
                print(title)
            while_iterator = 0
            with open("german_documents/" + title,"w") as f:
                f.write(document)
            append_flag = False
            document = ""
            title = ""
        if not l:
            break
    print(str(counter) + " texts parsed")
    print(str(len(os.listdir("german_documents/"))) + " files created")

# f1 =  open("data/sc.vrt", "r")
# parse_large_file(f1)
f2 =  open("data/nsc.vrt", "r")
parse_large_file(f2)
