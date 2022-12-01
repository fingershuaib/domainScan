import requests
import multiprocessing

def loadfile(filepath):
    result = []
    with open(filepath,'r') as f:
        for line in f:
            result.append(line.strip())
    return result

def scan(protocol,url,slist):
    for sub in slist:
        suburl = protocol + "://" + sub + "." + url
        try:
            urlreslut = requests.get(suburl,timeout=5)
            if urlreslut.status_code == 200 or urlreslut.status_code == 403:
                print("url:{} status code:{}".format(suburl,urlreslut.status_code))
        except:
            pass
if __name__ == '__main__':
    url = input("请输入你需要查询的域名:")
    # 按需求修改http或https
    proocol = "http"
    sublist = loadfile("testdic.ini")
    scan(proocol,url,sublist)