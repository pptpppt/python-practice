"""
练习 7：while 循环 + 文件读写
知识点：while 循环、break、文件读写（open / write / with）
玩法：前面的程序运行完，数据就没了。今天让程序把数据「存」到文件里——
      这是你的程序第一次拥有「记忆」。以后机器人记录传感器日志，底层就是这么回事。
"""

# ============ 模仿示例 1：while 循环 ============
# while 后面跟一个条件，条件成立就一直重复执行，直到条件不成立。
# 小心：条件永远成立就是「死循环」，只能按 Ctrl+C 强行停止。

# count = 1
# while count <= 3:
#     print(f"第 {count} 次巡检")
#     count = count + 1    # 每次加 1。忘了这句就死循环了

# 效果等价于 for i in range(1, 4)。
# 但 while 更适合「不知道要循环多少次」的场景，比如：用户想输几条就输几条。

# ============ 模仿示例 2：while True + break（最常用套路） ============
# while True = 永远循环，用 break 在合适的时机跳出来。

# while True:
#     answer = input("请输入温度（输入 q 退出）：")
#     if answer == "q":
#         print("已退出")
#         break            # break = 立刻跳出整个 while 循环
#     print(f"你输入的是 {answer}")

# ============ 模仿示例 3：写文件 ============
# open 的模式："w" = 写（覆盖旧内容），"a" = 追加（接着写，不覆盖），"r" = 只读
# with open(...) 的意思：代码块结束自动关文件，不用记 close()，以后都这么写。
# encoding="utf-8" 固定带上，防止中文乱码。

# with open("test.txt", "w", encoding="utf-8") as f:
#     f.write("土壤湿度 45%\n")     # \n 是换行。写记录时每条后面都要加，一行一条
#     f.write("土壤湿度 32%\n")

# ============ 模仿示例 4：读文件 ============
# 读法一：一次性读出全部内容（一个大字符串）
# with open("test.txt", "r", encoding="utf-8") as f:
#     content = f.read()
#     print(content)

# 读法二（更常用）：按行读。for line in f 每次拿到一行，
# 注意每行末尾自带一个 \n，用 .strip() 把它去掉。
# with open("test.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         print("这条记录是：", line.strip())

# ============ 任务区 ============

# 任务 1：写一个「温度录入器」：用 while True + break 不断让用户输入温室温度，
#         输入 q 退出；退出后打印"共录入 X 条"。
#         提示：开头先 count = 0，每录入一条就 count = count + 1（这叫累加器套路）

# 任务 2：把任务 1 录入的每条温度写进 records.txt（用 "a" 追加模式），一行一条。
#         写完把程序运行两次，再用记事本打开 D:\Projects\python-practice\records.txt
#         看看——这就是程序「记住」了数据。
#         提示：f.write(t + "\n")，t 是 input 拿到的字符串

# 任务 3（挑战）：另写几行代码（或另建一个文件），读取 records.txt 并统计：
#         共多少条、平均温度、最高温度分别是多少。
#         提示1：文件里读出来的每行是字符串，比如 "26.5\n"，要转成数字才能算：
#                t = float(line.strip())
#         提示2：又用累加器：total = 0，每读一条就 total = total + t，
#                平均 = total / 条数；最高温可以用 max() 或自己比大小

# count = 0
# while True:
#     answer=input("请输入温度(输入q退出)：")
#     print(f"你输入的是{answer}")
#     if answer == "q":
#         print("已退出")
#         break
#     else:
#         with open("records.txt","a",encoding="utf-8" ) as f:
#             f.write(answer+"\n")
#         count=count+1
# print(f"你输入的次数是{count}")
total=0
a=0
z=0
with open ("records.txt","r",encoding="utf-8")as f:
    for line in f:
      t=float(line.strip())
      if total==0:
         z=t
      else:
          if z<t:
             z=t
      total=total+1
      a=a+t
p=a/total
print("平均温度" ,p,"℃")
print("共",total,"条")
print("最高温度",z,"℃")
      

