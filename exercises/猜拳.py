import random  # 引入库一般在代码的开头

player = int(input('请输入：1、剪刀；2、石头；3、布\n'))
computer = random.randint(1, 3)
print('【测试用】电脑出的是%d' % computer)  # 测试
# 判断
if player == computer:
    print('平局')
elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 1):
    print('你赢了')
elif (player == 3 and computer == 1) or (player == 1 and computer == 2) or (player == 1 and computer == 3):
    print('你输了')
else:
    print('输入错误')
