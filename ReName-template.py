import glob, os
files = [os.path.basename(r) for r in glob.glob('*')] 
#スクリプトがあるフォルダ内のファイルおよびディレクトリーが取得される
#置換:
#検索:i.find("hoge") なかったら-1を返す
i=0
while i < len(files) :
    if -1 != files[i].find(".png"):
        print("find"+files[i])
    print(i)
    print(files[i])
    i += 1
