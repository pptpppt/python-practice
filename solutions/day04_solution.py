"""练习 4 参考答案"""

# 任务 1
def avg3(x, y, z):
    return (x + y + z) / 3

print(avg3(80, 90, 100))   # 90.0

# 任务 2
def jiao_wen(she_shi):
    return she_shi * 9 / 5 + 32

print(jiao_wen(25))        # 77.0

# 任务 3
def classify_temperature(t):
    if t > 35:
        return "高温"
    elif t > 25:
        return "温暖"
    elif t >= 10:
        return "适宜"
    else:
        return "低温"

temps = [12, 28, 40, 5, 20]
for t in temps:
    print(f"温度 {t} 度：{classify_temperature(t)}")
