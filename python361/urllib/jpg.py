# coding=utf-8
import re
import urllib
import urllib.request

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()# <class bytes>
    html = html.decode("utf-8")
    return html
    
def getImg(html):
    reg = r'src="(.*?\.jpg)"' # 分组 正则表达式
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    priFix = "http://www.trustrobot.cn"
    imglist = [priFix + url for url in imglist]
    print(imglist)
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'%s.jpg'%x)
        x += 1
 
html = getHtml("http://www.trustrobot.cn/index.php/Index/companyculture")
getImg(html)
