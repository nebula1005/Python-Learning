# 输入
username = input('请输入账号：')
password = input('请输入密码：')
# 验证
if username == 'admin' and password == '1234':
    print('登陆成功')
else:
    print('用户名或密码错误')
