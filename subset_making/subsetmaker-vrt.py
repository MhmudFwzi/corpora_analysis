import os
import sys
from pathlib import Path
from shutil import copyfile

group_start = sys.argv[1]
group_end = sys.argv[2]
source_folder = sys.argv[3]
group_start_prefix = group_start[0:3]
group_end_prefix = group_end[0:3]

try:
	os.mkdir(group_start)
except:
	pass

all_data_path = Path(os.getcwd()) / source_folder
group_data_path = Path(os.getcwd()) / group_start

for i in os.listdir(all_data_path):
	if int(i[-8:-5]) >= int(group_start_prefix) and int(i[-8:-5]) < int(group_end_prefix):
		copyfile(all_data_path / i,  group_data_path /  i)
