if __name__ == '__main__':
    print("**********************")
    print("*       1:取款        *")
    print("*       2:存款        *")
    print("*       3:转账        *")
    print("*       4:付款        *")
    print("*       5:消费        *")
    print("*       0:退出        *")
    print("**********************")
    deposit = 10000
    while True:
        inputVal = int(input("请选择你的操作\n"))

        match inputVal:
            case 0:
                print("Bye!")
                break
            case 1:
                print("你好，您选择的操作是：取款")
                val = int(input("请输入金额\n"))
                deposit -= val
                print(deposit)
            case 2:
                print("你好，您选择的操作是：存款")
                val = int(input("请输入金额\n"))
                deposit += val
                print(deposit)
            case 3:
                print("你好，您选择的操作是：转账")
                val = int(input("请输入金额\n"))
                deposit -= val
                print(deposit)
            case 4:
                print("你好，您选择的操作是：付款")
                val = int(input("请输入金额\n"))
                deposit -= val
                print(deposit)
            case 5:
                print("你好，您选择的操作是：消费")
                val = int(input("请输入金额\n"))
                deposit -= val
                print(deposit)
            case _:
                print("输入不合法")
