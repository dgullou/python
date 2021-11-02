import os.path

cur_path = os.path.dirname(__file__)
print("現在目錄路徑:" + cur_path)

filename = os.path.abspath("dir_exist.py")
if os.path.exists(filename):
    print("完整路徑名稱:" + filename)
    print("檔案大小:", os.path.getsize(filename))

    basename = os.path.basename(filename)
    print("最後的檔案或是路徑名稱:"+ basename)

    dirname = os.path.dirname(filename)
    print("目前檔案目錄路徑:" +dirname)
    print("是否為目錄:", os.path.isdir(filename))

    fullpath,fname = os.path.split(filename)
    print("目錄路徑:" + fullpath)
    print("檔名:"+ fname)

    Drive,fpath=os.path.splitdrive(filename)
    print("磁碟機:"+ Drive)
    print("路徑名稱:", fpath)

    fullpath = os.path.join(fullpath + "\\" + fname)
    print("組合路徑:" + fullpath)

