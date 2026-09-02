"""
练习 1：变量与打印
知识点：变量、print()、f-string（格式化字符串）、input() 输入
玩法：先看懂下面的「模仿示例」，再完成下面的任务。不懂没关系，照抄格式改数字也行。
"""

# ============ 模仿示例：先看懂这段 ============
# 变量 = 给数据起个名字。f-string 就是把变量嵌进字符串里，外面加个 f，变量用 {} 包起来。
# input() 会等待你从键盘输入，输入的内容是字符串（文字）。
tian_kuai_mian_ji = 2.5   # 田块面积（亩）
mu_chan = 800             # 亩产（斤/亩）
zong_chan = tian_kuai_mian_ji * mu_chan
print(f"这块 {tian_kuai_mian_ji} 亩的田，预计收 {zong_chan} 斤")

name = input("name：")
print(f"你好，{name}！今天开始学 Python 了。")

# ============ 任务区 ============
# 任务 1：仿照上面的写法，定义变量 a = 3.2（一块田的面积），b = 750（亩产），
#         计算总产量并用 print 打印出来。

# 任务 2：用 input() 让用户输入一个数字（亩数），存进变量 mian_ji，
#         再用公式「产量 = 亩数 * 800」算出结果打印。提示：input 拿到的是字符串，
#         要用 float() 转成数字，例如：mian_ji = float(input("请输入亩数："))

# 任务 3（挑战）：一块 3.2 亩的田亩产 750 斤，旁边一块 1.8 亩的田亩产 900 斤，
#         两块田的总产量是多少斤？用变量把每一步算清楚，打印出来。
mian_ji = 3.5
mu_chan = 750
zong_chan = mian_ji*mu_chan
print(f"这块{mian_ji}亩的地,预计收{zong_chan}斤")

mian_ji=float(input("请输入亩数;"))
zong_chan=mian_ji*800
print(zong_chan)

mian_ji1=3.2
mian_ji2=1.8
mu_chan1=750
mu_chan2=900
zong_mu=mian_ji1+mian_ji2
zong_chan1=mian_ji1*mu_chan1
zong_chan2=mian_ji2*mu_chan2
zongchan=zong_chan1+zong_chan2
print(f"共计{zong_mu}亩的地，总收{zongchan}斤")






