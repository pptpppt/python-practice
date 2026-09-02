"""练习 5 参考答案"""

# 任务 1
my_day = {"早起": "7:00", "学习Python": "2小时", "运动": "30分钟"}
my_day["学习Python"] = "3小时"      # 修改值
my_day["阅读"] = "1小时"            # 新增键值对
for key, value in my_day.items():
    print(f"{key} = {value}")

# 任务 2
sensors = [
    {"name": "湿度A", "battery": 85},
    {"name": "湿度B", "battery": 20},
    {"name": "湿度C", "battery": 55},
    {"name": "湿度D", "battery": 12},
]
for s in sensors:
    if s["battery"] < 30:
        print(f"{s['name']} 电量不足：{s['battery']}%")

# 任务 3
total = 0
for s in sensors:
    total += s["battery"]
avg = total / len(sensors)
print(f"平均电量：{avg}%")
