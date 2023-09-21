import re
import urllib.request,urllib.error
import bs4

baseUrl = "https://www.luogu.com.cn/problem/P"
savePath = "C:\\Users\\Unayh\\Desktop\\洛谷\\"
level = 0

def main():
    if selected_difficulty == "暂无评定":
        level = 0
    if selected_difficulty == "入门":
        level = 1
    if selected_difficulty == "普及-":
        level = 2
    if selected_difficulty == "普及/提高-":
        level = 3
    if selected_difficulty == "普及+/提高":
        level = 4
    if selected_difficulty == "提高+/省选-":
        level = 5
    if selected_difficulty == "省选/NOI-":
        level = 6
    if selected_difficulty == "NOI/NOI+/CTSC":
        level = 7
    html1 = getHTML("https://www.luogu.com.cn/problem/list?difficulty="+str(level)+"&page=1")
    getID()

    for i in id:
        print("正在爬取P{}...".format(i),end="")
        html = getHTML(baseUrl + str(i))
        if html == "error":
            print("爬取失败，可能是不存在该题或无权查看")
        else:
            problemMD = getMD(html)
            print("爬取成功！正在保存...",end="")
            saveData(problemMD,"P"+str(i)+".md")
            print("保存成功!")
    print("爬取完毕")

def getHTML(url):
    headers = {
        "user-agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 85.0.4183.121 Safari / 537.36"
    }
    request = urllib.request.Request(url = url,headers = headers)
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
    if str(html).find("Exception") == -1:        
        return html
    else:
        return "error"

def getMD(html):
    bs = bs4.BeautifulSoup(html,"html.parser")
    core = bs.select("article")[0]
    md = str(core)
    md = re.sub("<h1>","# ",md)
    md = re.sub("<h2>","## ",md)
    md = re.sub("<h3>","#### ",md)
    md = re.sub("</?[a-zA-Z]+[^<>]*>","",md)
    return md

def saveData(data,filename):
    cfilename = savePath + filename
    file = open(cfilename,"w",encoding="utf-8")
    for d in data:
        file.writelines(d)
    file.close()

if __name__ == '__main__':
    main()