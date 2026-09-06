"""练习 7 参考答案（先自己动手，卡住了再看）"""

# ---------- 任务 1 + 任务 2：温度录入器 + 写入文件 ----------

count = 0
while True:
    t = input("请输入温室温度（输入 q 退出）：")
    if t == "q":
        print(f"已退出，共录入 {count} 条")
        break
    count = count + 1
    with open("records.txt", "a", encoding="utf-8") as f:
        f.write(t + "\n")

# ---------- 任务 3：读取文件并统计 ----------

temps = []                          # 用列表把每条温度存起来，方便算 max
with open("records.txt", "r", encoding="utf-8") as f:
    for line in f:
        t = float(line.strip())     # "26.5\n" -> 26.5
        temps.append(t)

if len(temps) > 0:                  # 防止文件是空的，除以 0 会报错
    total = 0
    for t in temps:
        total = total + t
    print(f"共 {len(temps)} 条记录")
    print(f"平均温度：{total / len(temps):.1f} ℃")
    print(f"最高温度：{max(temps)} ℃")
else:
    print("文件里还没有记录")

# 更省事的写法（了解即可，以后会经常见）：
# print("平均：", sum(temps) / len(temps))
