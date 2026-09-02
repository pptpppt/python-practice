"""练习 3 参考答案"""

# 任务 1
yields = [850, 920, 780, 1000, 860]
for y in yields:
    print(f"产量：{y} 斤")
print(f"总产量：{sum(yields)} 斤")
print(f"平均产量：{sum(yields) / len(yields):.1f} 斤")
print(f"最高产量：{max(yields)} 斤")

# 任务 2
for i in range(1, 11):
    print(f"{i} 的平方是 {i * i}")

# 任务 3
yields = [850, 920, 780, 1000, 860, 950, 810]
for i, y in enumerate(yields):
    if y > 900:
        print(f"第 {i + 1} 块田产量 {y} 斤，超过 900")
