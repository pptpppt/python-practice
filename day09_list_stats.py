"""
练习 9：列表进阶 + 数据统计（生成大棚日报）
知识点：append 建列表、len / sum / max / min、sorted 排序、切片、f-string 排版
玩法：前两天你把传感器日志读出来了，但算个平均还得手动累加、一行行比大小。
      今天把数据装进「列表」，Python 自带的统计武器就能直接用了——
      这是从「会读数据」到「会出报告」的一步。拖拉机驾驶室里的仪表盘，
      显示的日产报表，底层逻辑就是这个。
"""

# ============ 模仿示例 1：先建一个空列表，往里装数据 ============
# 你其实已经见过列表：split 拆出来的就是。现在主动建一个：
# temps = []                # 空列表，准备装东西
# temps.append(26.5)        # append = 往末尾塞一条
# temps.append(28.1)
# print(temps)              # [26.5, 28.1]
# print(len(temps))         # 2（len = 数一数里面有几条）
#
# 常用套路：读文件时把每行数据 append 进列表，读完就得到一个"数据池"：
# temps = []
# with open("sensors.log", "r", encoding="utf-8") as f:
#     for line in f:
#         parts = line.strip().split(",")
#         temps.append(float(parts[1]))    # 温度在第 2 段（下标 1）

# ============ 模仿示例 2：列表自带统计四件套 ============
# 只要列表里全是数字，一行一个答案，不用再写累加器了：
# nums = [26.5, 28.1, 24.9, 30.2, 25.0]
# print(len(nums))      # 5       条数
# print(sum(nums))      # 总和    （你 day07/day08 手写的 total = total + t，从此退休）
# print(max(nums))      # 30.2    最高
# print(min(nums))      # 24.9    最低
# print(sum(nums)/len(nums))    # 平均——还是这两位配合
#
# 注意：sum/max/min 只对「装满数字的列表」有效，装字符串就会报错。

# ============ 模仿示例 3：排序 sorted() 和切片 [ : ] ============
# sorted(列表) 返回一个「排好序的新列表」，原列表不动：
# nums = [26.5, 28.1, 24.9, 30.2]
# up = sorted(nums)         # [24.9, 26.5, 28.1, 30.2]  从小到大
# down = sorted(nums, reverse=True)   # [30.2, 28.1, 26.5, 24.9] 从大到小
#
# 切片 = 从列表里切一段出来，格式 列表[起:止]（含头不含尾）：
# print(up[0:3])        # 前 3 个（最小的三个）
# print(up[-1])          # -1 = 最后一个，也就是最大值
# print(up[-3:])        # 最后 3 个（最大的三个）
# 记法：[-3:] 读作"倒数第三个一直到最后"。

# ============ 模仿示例 4：f-string 精确排版（今天必学） ============
# print("平均温度" ,pw,"℃") 会打出 26.518181818181817 这种长尾。
# 用 f-string 的「格式说明符」控制小数位数：
# avg = 26.518181818181817
# print(f"平均温度 {avg:.1f} ℃")    # 平均温度 26.5 ℃   （.1f = 保留 1 位小数）
# print(f"平均温度 {avg:.2f} ℃")    # 平均温度 26.52 ℃  （.2f = 保留 2 位）
# 以后所有报表打印，一律用 f"{变量:.1f}" 这个套路，告别逗号拼 print。

# ============ 任务区 ============


# 任务 1（数据池）：读 sensors.log，把每行的温度 float 后 append 进列表 temps，
#         湿度同理装进 humis（两个列表，下标一一对应：temps[0] 和 humis[0] 是同一时刻的）。
#         然后用 len / sum / max / min 打印温度日报，格式自己定，但必须全用 f-string，
#         平均值保留 1 位小数。参考输出：
#             ===== 大棚温度日报 =====
#             采集 12 条 | 平均 26.5℃ | 最高 30.2℃ | 最低 21.8℃
#         提示1：参考模仿示例 1 的"读文件建列表"套路
#         提示2：把 sum(temps)/len(temps) 先存进变量 avg，再 f"{avg:.1f}" 打印

# 任务 2（排行榜）：找出温度最高的 3 个时刻，按温度从高到低打印：
#             今日温度 Top3：
#             1. 14:00 → 30.2℃
#             2. 15:00 → 29.8℃
#             3. 13:00 → 29.1℃
#         提示1：光排 temps 列表会丢掉"时刻"信息——把每行拆成 (温度, 时刻) 小列表
#                再排序也行，或者干脆用 day05 学过的字典：rows.append({"time": parts[0], "t": float(parts[1])})
#         提示2：sorted 可以按 key 挑字段排：
#                rows.sort(key=lambda r: r["t"], reverse=True)
#                lambda 读作"按哪个值排"，现在照抄会跑就行，后面会讲
#         提示3：排完取前 3 条（切片或 for i in range(3)），用 f"{i+1}. {r['time']} → {r['t']:.1f}℃"
#         注意 r['t'] 里面单引号、外层 f-string 用双引号，别撞车


# 任务 3（挑战·中位数）：统计里的"中位数"= 所有数据排序后位于正中间的那个。
#         奇数条取正中间；偶数条取中间两个的平均。打印温度中位数。
#         提示1：先 sorted(temps) 存进新变量 s
#         提示2：n = len(s)，正中间的下标是 n // 2（// 是整除）
#         提示3：偶数时中间两个是 s[n//2 - 1] 和 s[n//2]，加起来除 2




temps=[]
humis=[]
with open("sensors.log","r",encoding="utf-8") as f:
    for line in f:
        parts=line.strip().split(",")
        temps.append(float(parts[1]))
        humis.append(float(parts[2]))
avg_temps=sum(temps)/len(temps)
avg_humis=sum(humis)/len(humis)
print("共录入",len(temps),"条数据")
print("最大温度：",max(temps))
print(f"平均温度：{avg_temps:.1f}")
print(f"平均湿度:{avg_humis:.2f}")
print("最大湿度：",max(humis))
parts2=[]
with open("sensors.log","r",encoding="utf-8") as f:
      for line in f:
          parts=line.split(",")
          parts2.append({"时间":parts[0],"温度":float(parts[1])})
down=sorted(parts2,key=lambda r:r['温度'],reverse=True)
print("高温排行榜:")
for i in range(3):
     print(f"{i+1}.{down[:3][i]['时间']}→{down[:3][i]['温度']:.1f}℃")
s=sorted(temps)
n=len(s)
if n%2==0:
     t=s[n//2]
else:
     t=(s[n//2]+s[n//2-1])/2
print(f"中位数温度：{t:.1f}")