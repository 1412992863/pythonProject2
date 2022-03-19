import random

if __name__ == '__main__':
    i = -1
    num = random.randint(0, 100)
    count = 1
    while i != num:
        i = int(input("请输入1-100之间的数字\n"))
        if i > 100 or i < 0:
            continue
        elif i < num:
            print("遗憾，太小了")
        elif i > num:
            print("遗憾，太大了")
        else:
            print("预测%d次，你猜中了！" % count)
            break
        count = count + 1
