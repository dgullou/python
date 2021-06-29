#propose:
#The file struct as follow
# root@ubuntu:/usr/local/python# ls
# os_path_walk.py  test.csv network\scapy.py

#if it need to print some file within "/usr/local/python"
# Result as follow
# Checking: /usr/local/python
# Checking: /usr/local/python/network
# File: /usr/local/python/network/scapy.py
#         last accessed: 1624971397.7009974
#         size: 0
# File: /usr/local/python/os_path_walk.py
#         last accessed: 1624969366.8474674
#         size: 601
# File: /usr/local/python/test.csv
#         last accessed: 1622786382.2200103
#         size: 99


import fire
import os



def walk_path(parent_path):
    print(f"Checking: {parent_path}")
    childs = os.listdir(parent_path)
    #從listdir can print as follow
    # os.listdir("/usr/local/python")
    # ['os_path_walk.py', 'test.csv']

    for child in childs:
        child_path = os.path.join(parent_path, child)
        if os.path.isfile(child_path):
            last_access = os.path.getatime(child_path)
            size = os.path.getsize(child_path)
            print(f"File: {child_path}")
            print(f"\tlast accessed: {last_access}")
            print(f"\tsize: {size}")
        elif os.path.isdir(child_path):
            walk_path(child_path)


if __name__ == '__main__':
    fire.Fire()