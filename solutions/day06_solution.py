"""练习 6 参考答案"""

def irri_advice(humidity, temp):
    if humidity < 30:
        if temp > 30:
            return "土壤缺水且气温高，建议立即灌溉 20 分钟"
        return "土壤缺水，建议灌溉 10 分钟"
    elif humidity < 60:
        if temp < 15:                       # 任务 2 新增的条件
            return "湿度合适但温度低，注意保温"
        return "湿度适中，暂不灌溉"
    else:
        return "湿度过大，注意排水"

def main():
    print("=== 灌溉决策小工具 v1.0 ===")
    # 任务 1：改成让用户输入湿度
    h = float(input("请输入土壤湿度："))
    print(irri_advice(h, 25))   # 温度暂时写死 25

    # 任务 3：统计需要灌溉的面积
    fields = [
        {"name": "田块A", "humidity": 25, "temp": 33, "area": 2.5},
        {"name": "田块B", "humidity": 45, "temp": 28, "area": 3.0},
        {"name": "田块C", "humidity": 70, "temp": 26, "area": 1.8},
    ]
    need_area = 0
    for field in fields:
        advice = irri_advice(field["humidity"], field["temp"])
        print(f"{field['name']}：{advice}")
        if field["humidity"] < 30:
            need_area += field["area"]
    print(f"需要灌溉的面积共 {need_area} 亩")

if __name__ == "__main__":
    main()
