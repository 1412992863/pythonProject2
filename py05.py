if __name__ == '__main__':
    n = int(input("请输入重量(kg)\n"))
    if n <= 50:
        print("重量为%d的行李托运价格为：%.2f元" % (n, n * 0.6))
    else:
        print("重量为%d的行李托运价格为：%.2f元" % (n, 50 * 0.6 + (n - 50) * 0.9))
