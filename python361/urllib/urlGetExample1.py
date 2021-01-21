# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432688314740a0aed473a39f47b09c8c7274c9ab6aee000/
# https://www.cnblogs.com/zhaof/p/6910871.html
# 进行抓取，并返回响应
# 发送一个GET请求到指定的页面 然后返回HTTP的响应


# urllib python内置的HTTP请求库
# urllib.request 请求模块
#
#
#
from urllib import request


'''
with request.urlopen('http://www.trustrobot.cn/index.php/Index/companyprogresswww.trustrobot.cn/index.php/Index/companyculture') as f:
    data = f.read()
    print("Status:",f.status,f.reason)
    for k,v in f.getheaders():
        print('%s: %s'%(k,v))
    print('Data: ', data.decode('utf-8'))
'''
response = request.urlopen('http://www.baidu.com')
print(response.read().decode('utf-8'))
