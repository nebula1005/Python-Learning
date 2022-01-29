# 输入销售额
sold = int(input('请输入你的销售额：'))
if sold < 10000:
    print('你获得了鼓励奖，请再接再厉！')
elif 10000 <= sold < 50000:
    print('恭喜你获得奖励一千元！')
elif 50000 <= sold < 100000:
    print('恭喜你获得奖励IBM笔记本一台！')
elif 100000 <= sold < 1000000:
    print('恭喜你获得iPhone12一台！')
else:
    print('恭喜你获得特斯拉model3一辆！记得踩好刹车哦！')
