import glob, os
files = [os.path.basename(r) for r in glob.glob('*')]
i=0
while i < len(files) :
    if -1 != files[i].find("AMD"):
        print("find"+files[i])
    print(i)
    print(files[i])
    i += 1
