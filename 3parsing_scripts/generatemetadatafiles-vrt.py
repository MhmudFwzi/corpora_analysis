from html.parser import HTMLParser
import os,sys
from pathlib import Path
from tqdm import tqdm

class clmetParser(HTMLParser):
    data_tags = ["text","p","page"]
    capture_meta = False
    meta_data = {}
    key = ""
    def handle_starttag(self, tag, attrs):
        if tag not in self.data_tags:
            self.capture_meta = True
            self.key = tag

    def handle_endtag(self, tag):
        if tag not in self.data_tags:
            self.capture_meta = False

    def handle_data(self, data):
        if self.capture_meta:
            self.meta_data[self.key] = data
    
    def get_meta_data(self):
        return self.meta_data

corpus = sys.argv[1]
try:
    output_folder = corpus + "-metadata"
    os.mkdir(output_folder)
except:
    print("Folder already exists or no create access")
for d in tqdm(os.listdir(corpus)):
    parser = clmetParser()
    doc_path = Path(corpus) / d
    f = open(doc_path)
    parser.feed(f.read())
    meta_path = Path(output_folder) / (d[:-4] + ".metadata")
    mf = open(meta_path,"a")
    mf.write("<text ")
    doc_meta_data = parser.get_meta_data()
    for i,m in enumerate(doc_meta_data):
        mf.write(m + "=\"" + doc_meta_data[m] + "\"")
        if i != len(doc_meta_data) - 1:
            mf.write(" ")
    mf.write(">\n</text>")
