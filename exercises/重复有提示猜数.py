import random

ran = random.randint(1, 10)
while True:
    guess = int(input('请输入你猜的数字：'))
    if guess == ran:
        print('恭喜你猜对了！')
        break
    elif ran < guess < 11:
        print('你猜大了')
    elif 0 < guess < ran:
        print('你猜小了')
    else:
        print('输入错误！请输入1~10的数字')
