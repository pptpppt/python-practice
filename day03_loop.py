"""
练习 3：循环与列表
知识点：for 循环、列表 list、len()、sum()、max()、min()
玩法：先看懂「模仿示例」，再完成下面的任务。
"""

# # ============ 模仿示例：一周温度统计 ============
# # 列表 = 一组数据排成队，用 [] 包起来，用下标取（从 0 开始）：temps[0] 是第一个数。
# # for 循环 = 把列表里的每个值挨个拿出来，执行一遍循环体。
# temps = [22, 25, 27, 24, 26, 28, 30]  # 一周 7 天的温度

# # 方式一：直接遍历每个值
# for t in temps:
#     print(f"温度：{t} 度")

# # 方式二：用 range(次数) 生成序号，配合下标
# for i in range(7):
#     print(f"第 {i + 1} 天：{temps[i]} 度")

# # Python 内置函数：len(长度) sum(总和) max(最大) min(最小)
# print(f"平均温度：{sum(temps) / len(temps):.1f} 度")  # :.1f 表示保留 1 位小数
# print(f"最高温度：{max(temps)} 度，最低温度：{min(temps)} 度")

# # ============ 任务区 ============
# # 任务 1：定义一个列表存放 5 块田的产量（斤）：850, 920, 780, 1000, 860，
# #         用 for 循环打印每块田的产量，再用 sum/len/max 打印总产量、平均产量、最高产量。

# # 任务 2：用 range() 打印 1 到 10 的平方（1²=1, 2²=4, ...），
# #         每行打印一个，格式："3 的平方是 9"。

# # 任务 3（挑战）：遍历下面的产量列表，用 if 判断，把超过 900 斤的田块
# #         打印出来（"第 X 块田产量 920 斤，超过 900"）。
# #         提示：用 range 配合下标，或者直接用 enumerate(列表)（用法：for i, v in enumerate(列表)）。
yields = [850, 920, 780, 1000, 860, 950, 810]
for i in yields:
    print(f"田产:{i}斤")
print(f"平均田产：{sum(yields) / len(yields):.1f}")
print(f"最高田产:{max(yields)},最低田产:{min(yields)}")
for i in range (10):
    print(f"{i+1}的平方是{(i+1)*(i+1)}")
for i in range(7):
    if yields[i]>900:
        print(f"第{i+1}块地的产量为{yields[i]}斤,超过900斤")

for i in yields:
    if i >900:
        print(f"产量为{i}斤,超过900斤")