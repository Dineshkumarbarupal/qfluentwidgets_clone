import multiprocessing
import requests

def downloadFile(Url,name):
    print(f"start downloding {name}.")
    responss = requests.get(Url)
    open(f"practice/files/file{name}.jpg", "wb").write(responss.content)
    print(f"finished downloding {name}.")
if __name__== '__main__':
    proc = [] 
    Url = "https://picsum.photos/2000/3000"
    for i in range(5):
        # downloadFile(Url , i)
        p = multiprocessing.Process(target = downloadFile , args = [Url, i])
        p.start()
        proc.append(p)

    for p in proc:
        p.join()   





