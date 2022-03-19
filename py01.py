import math as mt

if __name__ == '__main__':
    r = float(input("请输入球体半径"))
    print("球体表面积为：%.2f" % (4 * mt.pi * r ** 2))
    print("球体体积为：%.2f" % (4 / 3 * mt.pi * r ** 3))
