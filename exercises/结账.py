total_money = 0
total_number = 0
while True:  # 不清楚循环条件，让它恒循环，后期用if跳出
    price = float(input('输入价格：'))
    number = int(input('输入数量：'))
    total_money += price * number
    total_number += number
    answer = input('是否还要继续添加商品？（y,n)')
    if answer == 'n':
        break
print('总件数为：%d件 总金额为：%.2f元' % (total_number, total_money))
