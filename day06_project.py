"""
练习 6（综合项目）：灌溉决策小工具
知识点：把前面学的变量、条件、循环、函数、字典全部用上
玩法：这是一个完整的小程序。先运行看看效果，再完成「你的任务」。
"""

# ============ 主程序（已写好，先运行看看） ============

# def irri_advice(humidity, temp):
#     """根据土壤湿度和温度给出灌溉建议，返回一句话。"""
#     if humidity < 30:
#         if temp > 30:
#             return "土壤缺水且气温高，建议立即灌溉 20 分钟"
#         return "土壤缺水，建议灌溉 10 分钟"
#     elif humidity < 60:
#         return "湿度适中，暂不灌溉"
#     else:
#         return "湿度过大，注意排水"

# def main():
#     """主函数：程序从这里开始运行。"""
#     print("=== 灌溉决策小工具 v1.0 ===")
#     # 三块田的湿度、温度数据（字典套列表）
    # fields = [
    #     {"name": "田块A", "humidity": 25, "temp": 33},
    #     {"name": "田块B", "humidity": 45, "temp": 28},
    #     {"name": "田块C", "humidity": 70, "temp": 26},
    # ]
#     for field in fields:
#         advice = irri_advice(field["humidity"], field["temp"])
#         print(f"{field['name']}：{advice}")

# # 程序入口：只有直接运行这个文件时才执行 main()。
# # （以后你的项目都会这样写，先记住这个套路）
# if __name__ == "__main__":
#     main()

# ============ 你的任务 ============
# 任务 1：把 fields 列表改造成用 input() 输入湿度（不要温度），
#         让用户输入一块田的湿度，然后打印灌溉建议。
#         提示：h = float(input("请输入土壤湿度："))

# 任务 2：在 irri_advice 里加一个条件：湿度在 30~60 之间 且 温度低于 15，
#         返回"湿度合适但温度低，注意保温"。（改函数体即可，注意顺序）

# 任务 3（挑战）：给 fields 里每块田增加一个"面积(亩)"字段，
#         并在 main() 里统计：需要灌溉（湿度<30）的田块总共有多少亩，
#         打印"需要灌溉的面积共 X 亩"。
def irri_advice(humidity, temp):
    if humidity < 30:
        if temp > 30:
            return "土壤缺水且气温高，建议立即灌溉 20 分钟"
  
        return "土壤缺水，建议灌溉 10 分钟"
    elif humidity < 60 :
        if temp < 15:
            return"湿度合适但温度低，注意保温"
        return "湿度适中，暂不灌溉"
    else:
        return "湿度过大，注意排水"
fields = [
        {"name": "田块A", "humidity": 25, "temp": 33,"面积(亩)":200},
        {"name": "田块B", "humidity": 45, "temp": 28,"面积(亩)":200},
        {"name": "田块C", "humidity": 70, "temp": 26,"面积(亩)":200},
    ]
def main():
    """主函数：程序从这里开始运行。"""
    print("=== 灌溉决策小工具 v1.0 ===")
    total=0
    for field in fields:
        if field["humidity"]<50:
            total+=field["面积(亩)"]
    print(f"需要灌溉的面积共：{total}亩")

# 程序入口：只有直接运行这个文件时才执行 main()。
# （以后你的项目都会这样写，先记住这个套路）
if __name__ == "__main__":
    main()
