"""
练习 5：字典
知识点：字典 dict（键值对）、增删改查、遍历字典
玩法：字典 = 用「名字」找「值」，比列表的下标更好记。先看懂示例再动手。
"""

# ============ 模仿示例：管理一台传感器的数据 ============
# 字典用 {} 包起来，格式：{"键": 值, "键": 值}。用 字典名["键"] 取值。
# sensor_1 = {
#     "name": "土壤湿度传感器A",
#     "soil_humidity": 45,      # 土壤湿度 %
#     "temperature": 26,        # 温度 ℃
#     "battery": 87             # 电量 %
# }

# # 取值（两种写法，推荐第一种，键不存在会返回 None 而不是报错）
# print(sensor_1["name"])             # 写法一：直接下标
# print(sensor_1.get("battery"))      # 写法二：get()，键不存在返回 None

# # 修改值
# sensor_1["soil_humidity"] = 32
# print(f"最新土壤湿度：{sensor_1['soil_humidity']}%")

# # 新增键值对
# sensor_1["status"] = "正常"
# print(sensor_1)

# 遍历字典：.items() 同时拿到键和值
# for key, value in sensor_1.items():
#     print(f"{key} = {value}")

# ============ 任务区 ============
# 任务 1：创建一个字典表示你的一天：{"早起": "7:00", "学习Python": "2小时", "运动": "30分钟"}，
#         修改其中一个值，再新增一个键值对，最后遍历打印全部。

# 任务 2：有三个传感器的数据字典（如下），写一个 for 循环遍历 sensors 这个列表，
#         把 battery（电量）低于 30 的传感器名字打印出来（提示：遍历列表会得到字典，
#         再用 字典["键"] 取值判断）。

sensors = [
    {"name": "湿度A", "battery": 85},
    {"name": "湿度B", "battery": 20},
    {"name": "湿度C", "battery": 55},
    {"name": "湿度D", "battery": 12},
]

# 任务 3（挑战）：统计任务 2 中 sensors 的平均电量（把所有 battery 加起来除以数量），
#         打印"平均电量：XX%"。
ri_cheng={
    "起床":"7:00",
    "学习python":"2小时",
    "运动":"30分钟",
}
print(ri_cheng["起床"])
print(ri_cheng["学习python"])
ri_cheng["起床"]="11:00"
print(ri_cheng)
ri_cheng["睡觉"]="5:00"
print(ri_cheng)
for key,value in ri_cheng .items():
    print(f"{key},{value}")
for i in sensors:
    if i["battery"]<30:
        print(i["name"])
total =0
for i in sensors:
    total +=i["battery"]
a=total/len(sensors)   
print(f"平均电量为{a}%")