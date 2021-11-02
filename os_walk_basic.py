import os
cur_path = os.path.dirname(__file__)
sample_tree = os.walk(cur_path)
print(sample_tree)
for dirname,subdir,files in sample_tree:
    print("檔案路徑:", dirname)
    print("目錄串列:", subdir)
    print("檔案串列:", files)
    print()


# <generator object walk at 0x0000025B8621AB30>
# 檔案路徑: C:/python/venv/os_module/os
# 目錄串列: ['dir2', 'mydir']
# 檔案串列: ['dir_exist.py', 'glob_function.py', 'os.path.join_basic.py', 'os_path_file_exist_remove.py', 'os_path_function.py', 'os_system_function.py', 'os_walk_basic.py', 'totalsize.py']
#
# 檔案路徑: C:/python/venv/os_module/os\dir2
# 目錄串列: []
# 檔案串列: ['sample.txt']
#
# 檔案路徑: C:/python/venv/os_module/os\mydir
# 目錄串列: ['test1']
# 檔案串列: ['1.txt']
#
# 檔案路徑: C:/python/venv/os_module/os\mydir\test1
# 目錄串列: []
# 檔案串列: ['cisco.txt']
