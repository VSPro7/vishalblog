import os

rootdir = r"D:\DPS\VISHAL\Website\blog\vishalblog\content"

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        print (os.path.join(subdir, file))
        # filepath = subdir + os.sep + file

        # if filepath.endswith(".md"):
        #     print (filepath)