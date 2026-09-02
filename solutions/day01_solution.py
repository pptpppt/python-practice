"""练习 1 参考答案（先自己做，实在做不出来再看）"""

# 任务 1
a = 3.2
b = 750
zong = a * b
print(f"这块 {a} 亩的田，预计收 {zong} 斤")

# 任务 2
mian_ji = float(input("请输入亩数："))
chan_liang = mian_ji * 800
print(f"{mian_ji} 亩的田，产量是 {chan_liang} 斤")

# 任务 3
tian1_mian = 3.2
tian1_chan = tian1_mian * 750
tian2_mian = 1.8
tian2_chan = tian2_mian * 900
zong_chan = tian1_chan + tian2_chan
print(f"第一块田 {tian1_chan} 斤，第二块田 {tian2_chan} 斤，总共 {zong_chan} 斤")
