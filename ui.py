import tkinter as tk
import pc
from tkinter import ttk

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
    main()



filter_button = ttk.Button(root, text="开始", command=filter_questions)


label_difficulty.grid(row=0, column=0)
label_algorithm.grid(row=1, column=0)
difficulty_combobox.grid(row=0, column=1)
algorithm_combobox.grid(row=1, column=1)
filter_button.grid(row=2, column=0, columnspan=2)


root.mainloop()
