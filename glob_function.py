import glob

files = glob.glob("totalsize.py")+glob.glob("os*.py")

for file in files:
    print(file)
    
# The result is as follow:
# totalsize.py
# os.path.join_basic.py
# os_path_file_exist_remove.py
# os_path_function.py
# os_system_function.py
# os_walk_basic.py
