import excel_data
import os

for i in excel_data.__dict__:
    if isinstance(excel_data.__dict__[i], dict) and i != "__builtins__":
        os.system("python3 heat_map.py " + i)