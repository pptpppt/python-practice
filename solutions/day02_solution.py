"""练习 2 参考答案"""

# 任务 1
score = float(input("请输入分数："))
if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 任务 2
soil = float(input("请输入土壤湿度(0~100)："))
if soil < 30:
    print("需要灌溉")
elif soil <= 60:
    print("湿度合适，暂不灌溉")
else:
    print("湿度过大，注意排水")

# 任务 3
t = float(input("请输入温度："))
h = float(input("请输入湿度："))
if 25 <= t <= 35 and 50 <= h <= 80:
    print("作物生长环境适宜")
else:
    print("环境不适宜，请调整")
