n=float(input("来玩个游戏吧，你在我脑子里输入一个数，然后让别人来猜，你先输入："))
input("好了，现在可以开始游戏了，按回车键开始：")
print("猜猜我心里想的数字是几？")
while True:
    t=float(input("输入你猜的数字："))
    if t>n:
        print("哈哈哈，小傻瓜，没那么大啦，再猜一下哦宝宝")
    elif t<n:
        print("笨笨笨，猜那么小干嘛，数不到大的是吧,再猜")
    else:
        print("牛逼，这么快就猜对了")
        break