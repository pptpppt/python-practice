"""
练习 8：字符串拆分 + 异常处理
知识点：split() 拆字符串、try / except 防崩溃
玩法：昨天的程序有个毛病——输入 "abc" 就当场崩溃。真实世界的传感器数据
      经常有脏数据，程序不能一碰就倒。今天学两招工程师基本功：
      ① 把 "08:00,26.5,62" 这种一行日志拆成三个值（split）
      ② 遇到坏数据不崩，报个错继续跑（try / except）
"""

# ============ 模仿示例 1：字符串拆分 split ============
# "08:00,26.5,62" 是一行逗号分隔的日志（这种格式叫 CSV，传感器最爱用）。
# 想拆成三段，用 .split(",") —— 按逗号切开，返回一个列表：

# line = "08:00,26.5,62"
# parts = line.split(",")
# print(parts)          # ['08:00', '26.5', '62']
# print(parts[0])       # '08:00'（时间）
# print(parts[2])       # '62'（湿度，注意还是字符串！）

# 小细节：如果不想按逗号、想按空格拆，就 .split()（括号留空 = 按空白拆）。

# ============ 模仿示例 2：程序为什么会崩 ============
# 把下面这行注释取消，运行试试：
# t = float("abc")      # ValueError: could not convert string to float: 'abc'
# print(t)
# float("abc") 转不出数字，Python 直接报错停掉。
# 昨天你的录入器就有这毛病：手一抖输入 "26a"，整个程序就没了。
# 解决办法就是 try / except —— 见下一个示例。

# ============ 模仿示例 3：try / except（兜底） ============
# 把「可能会崩的代码」放进 try 里，崩了之后不退出，跳到 except 处理：

# try:
#     t = float("abc")
#     print("转成功：", t)
# except ValueError:
#     print("这不是一个数字，请重新输入")
# print("程序还能继续跑")        # 这句一定会执行到

# 记法：try = "试着干"，except ValueError = "如果出了这种错就…"
# 先精确写 ValueError，别一上来就万能兜底把所有错都吞掉。

# ============ 模仿示例 4：健壮输入套路（以后经常用） ============
# 三个零件拼起来：while True 死循环 + try 尝试转换 + break 成功即走

# while True:
#     s = input("请输入温度：")
#     try:
#         t = float(s)          # 这一行可能崩
#         break                 # 没崩 = 转换成功，跳出循环
#     except ValueError:
#         print("输入无效，要填数字哦")   # 崩了 = 提示再来一次
# print(f"拿到合法温度：{t}℃")

# ============ 任务区 ============

# 任务 1（防崩升级）：改造昨天的温度录入器（另建一个文件或写在下面都行）：
#         不断让用户输入温室温度，输入 q 退出；输入的不是数字时提示
#         "输入无效，请重新输入"并继续，绝不崩溃；最后打印共录入几条 + 平均温度。
#         提示1：q 的判断要放在 float 转换之前（先判断 q，再试着转数字）
#         提示2：把「float(输入)」放进 try，其余抄模仿示例 4 的套路
#         加分项：把有效温度追加写进 records.txt，攒一天真实数据

# 任务 2（日志解析器）：sensors.log 里存了大棚一天的监测记录，
#         每行格式是「时间,温度,湿度」，例如：08:00,26.5,62
#         写代码读这个文件，打印：总条数、平均温度、平均湿度，
#         并且逐条打印成这样的格式：
#             08:00 → 26.5℃ / 湿度 62%
#         提示1：for line in f → line.strip() → line.split(",") 得到 3 段
#         提示2：parts[1] 是字符串 "26.5"，要 float() 才能算平均
#         提示3：累加器套路你 day07 已经用过，直接搬

# 任务 3（挑战·告警过滤）：湿度超过 80% 说明有积水风险，要人工去查。
#         解析时把这些行挑出来，写进新文件 alert.txt，每行格式：
#         20:00,85
#         提示：拼字符串 w = parts[0] + "," + parts[2]，写文件用 day07 的 with open
count = 0
while True:
      answer=input("请输入温度(输入q退出)：")
      print(f"你输入的是{answer}")
      if answer == "q":
            print("已退出")
            break
      try:
           s=float(answer)
      except ValueError:
           print("格式错误，请输入数字")
           continue
      else:
          with open("records.txt","a",encoding="utf-8" ) as f:
              f.write(f"{s}\n")
              count=count+1
print(f"你输入的次数是{count}")
total=0
zw=0
zs=0
with open("alert.txt","w",encoding="utf-8")as f_out:
    with open ("sensors.log","r",encoding="utf-8")as f:
        for line in f:
          parts=line.strip().split(",")
          total=total+1
          zw=zw+float(parts[1])
          zs=zs+float(parts[2])
          if 80<float(parts[2]):
             w = parts[0] + "," + parts[2]
             f_out.write(w+"\n")
pw=zw/total
ps=zs/total
print("平均温度" ,pw,"℃")
print("共",total,"条")
print("平均湿度",ps,)  