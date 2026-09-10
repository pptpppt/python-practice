"""
练习 10：字典进阶 + 农产品市场日报
知识点：字典 get() 默认值、items() 遍历、字典做「频次统计」和「分组汇总」、
       按字典 value 排序、max(d, key=d.get) 找最值键
玩法：day09 你把每天的温度数据装成「列表 + 字典组合」，统计出日报。
      今天把数据再升一级：12 条农产品报价（每条一个 dict），要算出
      "每种产品出现几次 / 每种产品平均价多少 / 哪个产地最贵"。
      这是把「数据池」变成「市场报告」的标准套路——也是以后看大疆农业、
      极飞销售数据报表时会用上的同一种语言。
"""

# ============ 数据源：12 条农产品报价（已经写在下面，照抄用就行） ============
records = [
    {"产品": "番茄", "产地": "山东寿光", "价格": 4.2},
    {"产品": "黄瓜", "产地": "山东寿光", "价格": 3.5},
    {"产品": "番茄", "产地": "河北馆陶", "价格": 3.9},
    {"产品": "辣椒", "产地": "河南扶沟", "价格": 6.8},
    {"产品": "黄瓜", "产地": "河北馆陶", "价格": 3.2},
    {"产品": "茄子", "产地": "山东寿光", "价格": 2.8},
    {"产品": "番茄", "产地": "江苏沛县", "价格": 4.5},
    {"产品": "辣椒", "产地": "山东寿光", "价格": 7.1},
    {"产品": "黄瓜", "产地": "河南扶沟", "价格": 3.0},
    {"产品": "茄子", "产地": "河北馆陶", "价格": 3.1},
    {"产品": "玉米", "产地": "河南扶沟", "价格": 2.4},
    {"产品": "番茄", "产地": "河南扶沟", "价格": 4.0},
]

# ============ 模仿示例 1：get() 默认值（必学套路） ============
# 字典里取一个 key，如果这个 key 不存在会报错。get() 让你给个保底值：
# d = {"番茄": 4, "黄瓜": 3}
# print(d.get("番茄"))       # 4
# print(d.get("苹果", 0))    # 0   ← 苹果不存在，但没崩，返回默认值 0
# # 这个套路用在「累加器 / 频次统计」里 100% 会出现：
# counts = {}
# for r in records:
#     k = r["产品"]
#     counts[k] = counts.get(k, 0) + 1    # 没这个 key 就从 0 开始，否则 +1

# ============ 模仿示例 2：字典遍历的三种姿势 ============
# counts = {"番茄": 4, "黄瓜": 3, "辣椒": 2}

# for k in counts:                # 默认只拿 key
#     print(k)
#
# for k, v in counts.items():     # 一次拿 key + value（推荐）
#     print(k, "出现", v, "次")
#
# for v in counts.values():       # 只拿 value（一般用得少）
#     print(v)
# 重点记 .items()：以后做"键值对都用到"的循环就用它。

# ============ 模仿示例 3：按 value 排序（字典版 Top） ============
# 把字典变成 [(k, v), (k, v), ...]，再 sorted：
# counts = {"番茄": 4, "黄瓜": 3, "辣椒": 2}
# top = sorted(counts.items(), key=lambda x: x[1], reverse=True)
# print(top)     # [('番茄', 4), ('黄瓜', 3), ('辣椒', 2)]
# 关键：counts.items() 返回一串「小元组」，x[0]=key, x[1]=value，
#       key=lambda x: x[1] 就是"按 value 排"。

# ============ 模仿示例 4：找最值对应的 key ============
# 想知道"哪个 key 的 value 最大"，一行就行：
# counts = {"番茄": 4, "黄瓜": 3, "辣椒": 2}
# print(max(counts, key=counts.get))    # 番茄
# max(字典, key=字典.get) 是经典套路，记住就行。

# ============ 任务区 ============


# 任务 1（频次统计）：遍历 records，用模仿示例 1 的 get() 套路建一个字典
#         counts，统计每种产品各出现几次。打印：
#             产品出现次数：
#             番茄 4 次
#             黄瓜 3 次
#             辣椒 2 次
#             茄子 2 次
#             玉米 1 次
#         提示1：空字典 counts = {}，循环里 counts[k] = counts.get(k, 0) + 1
#         提示2：打印时用 for k, v in counts.items():
#                print(f"{k} {v} 次")   —— 注意空格自己排
#         提示3：想按出现次数从多到少打印？用模仿示例 3 的 sorted()
counts={}
for r in records:
    k=r["产品"]
    counts[k]=counts.get(k,0)+1
top=sorted(counts.items(),key=lambda x:x[1],reverse=True)
# print(top)
# for k,v in counts.items():
    # print(f"{k}{v}次")

# 任务 2（分组求均价）：每个产品的平均价 = 这个产品所有报价加起来 / 几条。
#         提示1：先按产品把"所有价格"收进一个字典 of 列表：
#                prices = {"番茄": [4.2, 3.9, 4.5, 4.0], ...}
#                套路和频次统计几乎一样，只是从 counts.get(k,0)+1 改成
#                prices.setdefault(k, []).append(r["价格"])
#                或者两步法：if k in prices: prices[k].append(...)
#                            else: prices[k] = [r["价格"]]
#         提示2：拿到 prices 后再遍历一次，算 sum/len 就是平均价，存进新字典 avgs
#         提示3：最后用 f-string 按"番茄 4.2 元/kg"这种格式打印所有均价
prices={}
for r in records:
    k=r["产品"]
    if k not in prices:#这里很有意思， if k in prices 那么就会跳过下一步，直接把价格加到“键”【K】里，也就是说一个“键”对应多个“值”
        prices[k]=[]
    prices[k].append(r["价格"])
# print(prices)
avg={}
for k,v in prices.items():
    avg[k]=round(sum(v)/len(v),1)
# print(avg)
    # print(f"蔬菜：{k}的均价为{avg:.1f}元/kg")

# 任务 3（综合·市场日报）：把上面两个任务的字典合并起来，输出市场报告：
#         ============ 农产品市场日报 ============
#         产品   次数   均价(元/kg)   最高价   最低价
#         番茄    4     4.2         4.5      3.9
#         黄瓜    3     3.2         3.5      3.0
#         辣椒    2     7.0         7.1      6.8
#         茄子    2     3.0         3.1      2.8
#         玉米    1     2.4         2.4      2.4
#         提示1：先建两个空字典：maxs = {}、mins = {}
#                遍历 records，套用模仿示例 1 的 get 套路——但这次是 max/min：
#                maxs[k] = max(maxs.get(k, 0), r["价格"])
#                mins[k] = min(mins.get(k, 9999), r["价格"])
#                （最大值先和"见过的最大"比，最小值先和"见过的最小"比）
#         提示2：循环打印时，让均价保留 1 位小数 f"{avg:.1f}"
#         提示3：次数多的排前面？遍历 counts.items() 时按 v 排：
#                for k, v in sorted(counts.items(), key=lambda x: x[1], reverse=True):
#                    ... 在里面用 k 去找 avgs[k] / maxs[k] / mins[k]
maxs={}
mins={}
for k,v in prices.items():
    maxs[k]=max(v)
    mins[k]=min(v)
    # print(f"{k}的最高价为{maxs[k]}元/kg")
print("=====================农产品市场日报=======================")
print("产品     次数     均价（元/kg）    最高价/元     最低价/元")
for k,v in sorted (counts.items(),key=lambda x:x[1],reverse=True):
    print(f"{k}      {v}        {avg[k]}               {maxs[k]}           {mins[k]}") 