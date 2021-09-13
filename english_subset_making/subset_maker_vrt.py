import os
import sys
from pathlib import Path
from shutil import copyfile

group = sys.argv[1]
source_folder = sys.argv[2]
group_prefix = group[0:3]

try:
	os.mkdir(group)
except:
	pass

all_data_path = Path(os.getcwd()) / source_folder
group_data_path = Path(os.getcwd()) / group


for i in os.listdir(all_data_path):
	if i[-8:-5] == group_prefix:
		copyfile(all_data_path / i,  group_data_path /  i)
