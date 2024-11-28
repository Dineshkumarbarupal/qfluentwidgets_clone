import multiprocessing
# import multiprocessing.process
# from multiprocessing import process
import requests

def downloadFile(Url,name):
    responss = requests.get(Url)
    open(f"practice/files/file{name}.jpg", "wb").write(responss.content)

# proc = [] 
Url = "https://picsum.photos/200/300"
for i in range(5):
    downloadFile(Url , i)
#     p = multiprocessing.process(target = downloadFile , args = [Url, i])
#     p.show()
#     proc.append(p)

# for p in proc:
#     p.join()      
