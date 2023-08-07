import glob, os
import json


parent_dir = os.getcwd()

# parent_dir = parent_dir.replace("01. Python Scripts","99. Notebooks")

files = []
os.chdir(parent_dir)
for file in glob.glob("*.ipynb"):
    files.append(file)


filenames = [parent_dir+"\\" + x for x in files]


for file in filenames:
    code = json.load(open(file))
    py_path = file[0:len(file)-6]
#    py_path = py_path.replace("\\99. Notebooks\\","\\01. Python Scripts\\")
    py_file = open(f"{py_path}.py", "w+")

    for cell in code['cells']:
        if cell['cell_type'] == 'code':
            for line in cell['source']:
                py_file.write(line)
            py_file.write("\n")
        elif cell['cell_type'] == 'markdown':
            py_file.write("\n")
            for line in cell['source']:
                if line and line[0] == "#":
                    py_file.write(line)
            py_file.write("\n")

    py_file.close()
