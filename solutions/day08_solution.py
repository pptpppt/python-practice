"""练习 8 参考答案（先自己动手，卡住了再看）"""

# ---------- 任务 1：防崩版温度录入器（try/except 兜底） ----------

temps = []
count = 0
while True:
    s = input("请输入温室温度（输入 q 退出）：")
    if s == "q":                        # q 的判断放在转换之前
        print("已退出")
        break
    try:
        t = float(s)                    # 只有这一行可能崩
    except ValueError:
        print("输入无效，请重新输入数字")
        continue                        # 回到 while 开头，重新输入
    temps.append(t)
    count = count + 1

if count > 0:
    total = 0
    for t in temps:
        total = total + t
    print(f"共录入 {count} 条，平均温度 {total / count:.1f}℃")

# 加分项（想攒数据就打开注释）：
# with open("records.txt", "a", encoding="utf-8") as f:
#     for t in temps:
#         f.write(str(t) + "\n")

# ---------- 任务 2：日志解析器（split 拆 CSV 行） ----------

total_temp = 0
total_hum = 0
count = 0
with open("sensors.log", "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(",")     # ['08:00', '26.5', '62']
        time_str = parts[0]
        temp = float(parts[1])              # 字符串 -> 数字才能算
        hum = float(parts[2])
        print(f"{time_str} → {temp}℃ / 湿度 {hum}%")
        total_temp = total_temp + temp
        total_hum = total_hum + hum
        count = count + 1

print(f"共 {count} 条记录")
print(f"平均温度：{total_temp / count:.1f}℃")
print(f"平均湿度：{total_hum / count:.1f}%")

# ---------- 任务 3（挑战）：湿度告警过滤，写进 alert.txt ----------

with open("sensors.log", "r", encoding="utf-8") as f:
    with open("alert.txt", "w", encoding="utf-8") as out:
        for line in f:
            parts = line.strip().split(",")
            hum = float(parts[2])
            if hum > 80:                    # 有积水风险的行
                out.write(parts[0] + "," + parts[2] + "\n")
print("告警已写入 alert.txt")
