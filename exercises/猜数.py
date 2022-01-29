# 生成一个随机数
import random  # 调出随机数标准库

ran = random.randint(1, 10)
print('【测试用】生成的随机数是：%d' % ran)
guess = input('请输入你猜的数：')
if ran == int(guess):
    print('恭喜你，你猜对了！')
else:
    print('很遗憾你猜错了。')
