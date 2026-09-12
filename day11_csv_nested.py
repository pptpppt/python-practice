"""
练习 11：CSV 文件 + 字典嵌套（智能温室传感器周报）
知识点：csv.writer / csv.DictReader、字典套字典、嵌套统计
玩法：day09-10 你玩的是「代码里硬编码数据 + 字典统计」。
      真实场景数据不会写在代码里 —— 传感器会导出 CSV，Excel 报表会另存 CSV。
      今天打通「生成 CSV → 读 CSV → 嵌套字典分析 → 出周报」完整闭环。
      主题切智能温室：5 个温室（A-E）× 3 种传感器（温度/湿度/光照）× 7 天 = 105 条。
      这是智能装备岗最常见的数据流：传感器 → CSV → Python → 决策报告。
"""

import csv
import random


# # ============ 第一步：生成数据（先跑这一段） ============
# # 运行 generate_csv() 后会在当前目录生成 sensor.csv，105 条记录。
# # random.seed(42) 保证每次跑出来的数据一样，方便对比结果。

# def generate_csv():
#     """生成 5 个温室 × 3 种传感器 × 7 天的传感器周数据"""
#     random.seed(42)                                  # 固定随机种子，结果可复现
#     records = []
#     for day in range(1, 8):                          # 9 月 1 日 ~ 9 月 7 日
#         date = f"2026-09-0{day}"
#         for gh in ["A", "B", "C", "D", "E"]:         # 5 个温室
#             for sensor, base, jitter in [               #这里的几个for有分级齿轮的意思，下级齿轮转动一圈，上级齿轮转动一齿
#                 ("温度", 25, 2),                    # 温度基准 25°C，浮动 ±2
#                 ("湿度", 65, 8),                    # 湿度基准 65%，浮动 ±8
#                 ("光照", 12000, 3000),              # 光照基准 12000 lux，浮动 ±3000
#             ]:
#                 value = round(base + random.uniform(-jitter, jitter), 1)
#                 records.append([date, gh, sensor, value])

#     with open("sensor.csv", "w", newline="", encoding="utf-8") as f:
#         writer = csv.writer(f)
#         writer.writerow(["日期", "温室", "传感器", "数值"])
#         for r in records:
#             writer.writerow(r)
#     print(f"已生成 sensor.csv，共 {len(records)} 条记录")

# generate_csv()      # ← 先取消这一行的注释跑一次


# ============ 模仿示例 1：csv.writer（写 CSV） ============
# CSV 文件本质就是「用逗号分隔的文本」，但有专门的模块处理逗号转义、换行符。
# 写：
# import csv
# with open("xxx.csv", "w", newline="", encoding="utf-8") as f:
#     writer = csv.writer(f)
#     writer.writerow(["列1", "列2", "列3"])    # 写一行（一般是表头）
#     writer.writerow(["a", "b", "c"])          # 再写一行数据
# 注意：open() 加 newline="" 是 Windows 必加，否则 CSV 里会出现空行


# ============ 模仿示例 2：csv.DictReader（按行读成字典） ← 重点 ============
# 读 CSV 两种姿势：
# ① csv.reader：每行读成 ["2026-09-01", "A", "温度", "26.5"] 这种列表，要靠下标取
# ② csv.DictReader：每行读成 {"日期": "2026-09-01", "温室": "A", ...} 这种字典
#                  （day10 records 的同款数据结构）—— 推荐用这个
#
# 用法：
# with open("sensor.csv", "r", encoding="utf-8") as f:
#     reader = csv.DictReader(f)
#     for row in reader:                # row 是字典
#         print(row["温室"], row["传感器"], row["数值"])
# 注意：csv 读出来的全是「字符串」，数值要自己 float()


# ============ 模仿示例 3：字典嵌套的两步法 ← 核心套路 ============
# 想建这种结构（每个温室一个字典，里面再按传感器分）：
# data = {
#     "A": {"温度": [26.5, 27.1, ...], "湿度": [...], "光照": [...]},
#     "B": {"温度": [...], "湿度": [...], "光照": [...]},
#     ...
# }
#
# 套路（两步检查 —— 第二层字典也要按需新建！）：
# data = {}
# for row in rows:                                                                              #这里的rows是哪里来的？ 难道是代指？
#     gh = row["温室"]
#     sensor = row["传感器"]
#     if gh not in data:               # 第一层：温室没出现过？
#         data[gh] = {}                #        给它建一个空字典
#     if sensor not in data[gh]:       # 第二层：这个传感器在这个温室没出现过？
#         data[gh][sensor] = []        #        给它建一个空列表
#     data[gh][sensor].append(float(row["数值"]))
#
# 关键坑：忘了写 `if sensor not in data[gh]`，
#     会 KeyError: '温度'（因为 data["A"] 一开始是 {}，根本没有"温度"这个 key）


# ============ 任务区 ============

# 任务 1（生成数据）：取消注释 generate_csv() 那一行跑一次，
#         跑完确认当前目录出现 sensor.csv。
#         进阶思考：为什么用 random.seed(42)？删掉会怎样？

# 任务 2（熟悉 DictReader）：用 csv.DictReader 读 sensor.csv，
#         打印前 5 行。
#         提示1：with open(...) as f: reader = csv.DictReader(f)
#         提示2：想只打印前 5 行？enumerate + if i >= 5: break
#                或者 reader 是迭代器，可以 list(reader)[:5]
#         提示3：想看每一行是什么类型？print(type(row))  —— 应该是 dict
with open("sensor.csv","r",encoding="utf-8")as f:
    reader=csv.DictReader(f)
    # for i,row in enumerate(reader): 
    #     if i>=5:
    #         break
        # print(i+1,row)
# 任务 3（建嵌套字典）：按模仿示例 3 的套路，建 data 字典，
#         遍历所有行，把数值转 float 后塞进去。
#         完成后做 3 个验证打印：
#             print(data.keys())               # 应该是 5 个温室
#             print(data["A"].keys())          # A 温室里有什么传感器
#             print(len(data["B"]["温度"]))    # B 温室温度应该有 7 条
#         如果对不上 7 条，说明哪一层字典漏建了，回头看模仿示例 3。
    data={}
    for row in reader:
        gh=row["温室"]
        sensor=row["传感器"]
        if gh not in data:
            data[gh]={}
        if sensor not in data[gh]:
            data[gh][sensor]=[]
        data[gh][sensor].append(float(row["数值"]))
print(data.keys())               # 应该是 5 个温室
print(data["A"].keys())          # A 温室里有什么传感器
print(len(data["B"]["温度"]))      # B 温室温度应该有 7 条      



# 任务 4（温室传感器周报）：对每个温室每种传感器算 max / min / avg，
#         按下面格式打印（参考 day10 农产品日报的同款排版）：
#             ============ 智能温室传感器周报 ============
#             温室  传感器  次数  最高   最低   平均
#             A     温度     7    27.1   24.5   25.9
#             A     湿度     7    72.0   58.3   65.4
#             A     光照     7    14520  9120   11890
#             B     温度     7    ...
#             ...
#         提示1：for gh in data:           # 温室
#                for sensor in data[gh]:  # 传感器
#                    vals = data[gh][sensor]
#                    print(f"{gh}  {sensor}  {len(vals)}  {max(vals)}  {min(vals)}  {sum(vals)/len(vals):.1f}")
#         提示2：想让表格对齐？f-string 里写宽度：
#                f"{gh:<6}{sensor:<8}{len(vals):<6}{max(vals):<8.1f}{min(vals):<8.1f}{sum(vals)/len(vals):<8.1f}"
#                （: 后面 <6 表示"左对齐占 6 个字符宽"——和 Excel 表格长得一模一样）
#         提示3：想按温室 A→B→C→D→E 顺序？sorted(data.keys()) 就好
print("============ 智能温室传感器周报 ============")
print("温室  传感器   次数   最高    最低    平均")
for gh in  sorted(data.keys()):
    for sensor in data[gh]:
        vals=data[gh][sensor]
        print(f"{gh:<6}{sensor:<8}{len(vals):<6}{max(vals):<8.1f}{min(vals):<8.1f}{sum(vals)/len(vals):<8.1f}")