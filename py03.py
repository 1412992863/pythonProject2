if __name__ == '__main__':
    n = int(input("请输入n\n"))
    sum_n = 0
    t = 1
    for i in range(1, n + 1):
        t *= i
        sum_n += t
    print("1!+...%d!=%d" % (n, sum_n))
