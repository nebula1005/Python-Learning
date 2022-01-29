# 输入一个三位数
number = int(input('请输入一个三位数：'))
# 输出个位数
print('个位数：', number % 10, sep='')
# 输出十位数
print('十位数：', number // 10 % 10, sep='')
# 输出百位数
print('百位数：', number // 100, sep='')
