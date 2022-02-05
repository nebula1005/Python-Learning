import random  # 引入库一般在代码的开头

count1 = 0
count2 = 0
while True:
    computer = random.randint(1, 3)
    print('【测试用】电脑出的是%d' % computer)  # 测试
    player = int(input('请输入：1、剪刀；2、石头；3、布\n'))
    # 判断
    if player == computer:
        print('平局')
    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 1):
        print('你赢了')
        count1 += 1
    elif (player == 3 and computer == 1) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
        print('你输了')
        count2 += 1
    else:
        print('输入错误')
    if count1 == 2:
        print('你获得了最终的胜利！')
        break
    elif count2 == 2:
        print('电脑获得最终的胜利！')
        break
