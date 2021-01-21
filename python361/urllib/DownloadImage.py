# coding=utf-8
import re
import urllib
import urllib.request
import chardet
import sys
import io
import gzip


#改变标准输出的默认编码
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

# 获取网页源代码
def getHtml(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}) # 请求网页
    html = urllib.request.urlopen(req).read().decode('GBK') # 指定编码请求
    #print(chardet.detect(html))
    #html = html.decode("latin-1") # 字节包可以解码成字符串
    #html = html.decode("GB2312") # 字节包可以解码成字符串
    #print(html)
    return html


# 获取网页上 图片地址并下载
def getImg(html):
    #src='http://cl.dh4.biz/htm_data/7/1609/2059947.html' 
    reg = r'img src=\'(.*?\.(jpg|bmp|gif))\'' # 分组 正则表达式
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    #print(imglist)
    print(len(imglist))
    x = 0
    for imgurl in imglist:
        try:
            urllib.request.urlretrieve(imgurl[0],'%s.jpg'%x)
        except:
            pass
        x += 1
    print("finish")
 
html = getHtml("http://www.trustrobot.cn/index.php/Index/companyculture")


getImg(html)
