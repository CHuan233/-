import re
import urllib.request,urllib.error
import bs4
import time
import tkinter as tk
from tkinter import ttk

baseUrl = "https://www.luogu.com.cn/problem/"
savePath = "C:\\Users\\Unayh\\Desktop\\洛谷\\"


def main(level):

    html1 = getHTML("https://www.luogu.com.cn/problem/list?difficulty="+str(level)+"&page=1")

    pattern = r'<li>(P\d+)&nbsp;<a href="P\d+">\[([^]]+)\]([^<]+)</a></li>'
    matches = re.findall(pattern, html1)

    for match in matches:
        problem_code = match[0]
        contest_info = match[1]
        problem_title = match[2]
        print(f"问题代码: {problem_code}, 比赛信息: {contest_info}, 问题标题: {problem_title}")
        print('\n')
        print("正在爬取...")
        html = getHTML(baseUrl + match[0])
        if html == "error":
            print("爬取失败，可能是不存在该题或无权查看")
        else:
            problemMD = getMD(html)
            print("爬取成功！正在保存...",end="")
            saveData(problemMD,match[0]+match[2]+".md")
            print("保存成功!")
        time.sleep(5)
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



# 创建主窗口
root = tk.Tk()
root.title("洛谷爬虫")

# 创建标签
label_difficulty = ttk.Label(root, text="难度:")
label_algorithm = ttk.Label(root, text="算法标签:")

# 创建下拉框
difficulty_options = ["暂无评定", "入门","普及-","普及/提高-","普及+/提高","提高+/省选-","省选/NOI-","NOI/NOI+/CTSC"]
algorithm_options = ["排序", "搜索", "动态规划"] 

difficulty_var = tk.StringVar()
algorithm_var = tk.StringVar()

difficulty_combobox = ttk.Combobox(root, textvariable=difficulty_var, values=difficulty_options)
algorithm_combobox = ttk.Combobox(root, textvariable=algorithm_var, values=algorithm_options)

# 创建筛选按钮的回调函数
def filter_questions():
    selected_difficulty = difficulty_var.get()
    selected_algorithm = algorithm_var.get()
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
    print(level)
    main(level)



filter_button = ttk.Button(root, text="开始", command=filter_questions)


label_difficulty.grid(row=0, column=0)
label_algorithm.grid(row=1, column=0)
difficulty_combobox.grid(row=0, column=1)
algorithm_combobox.grid(row=1, column=1)
filter_button.grid(row=2, column=0, columnspan=2)


root.mainloop()