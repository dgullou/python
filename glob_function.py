import glob

files = glob.glob("totalsize.py")+glob.glob("os*.py")

for file in files:
    print(file)