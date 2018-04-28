num = 1
li = [{'UserName':'zhangsan','PassWord':'123'},
      {'UserName':'lisi','PassWord':'123'},
      {'UserName':'wangwu','PassWord':'123'},]
while num < 4:
    Name = input("输入用户名:")
    Passwd = input("输入密码:")
    for i in li:
        if i['UserName'] == Name and Passwd == i['PassWord']:
            print("登录成功")
            num = 4
            break
    else:
        num += 1
        num1 = 4 - num
        cishu = "登录失败,您还剩余%d次机会" %num1
        print(cishu)
        if num1 == 0:
            yn = input("请输入是否还重试(Y|N)")
            if yn == "Y" or yn == "y":
                num = 1
            else:
                print("ByeBye!!!")













