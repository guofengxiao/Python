# coding=utf-8 #源码文件的设置方式是UTF-8
import re # 内建正则库
import urllib
import urllib.request
import chardet #编码检测包

DEBUG = False

URL = "http://www.trustrobot.cn/"
global x
x = 0
#URL = "http://www.trustrobot.cn/index.php/Index/companyprogress"

# 获取网页源码
def getHtml(url):
    try:
        response = urllib.request.urlopen(url)
        html = response.read()# <class bytes> 字节码
        if DEBUG == True:
            print( "response.geturl(): ",response.geturl() )
            print( "="*47 )
            print( "response.info(): ",response.info() )
            print( "="*47 )
            print( "response.getcode(): ",response.getcode() )
            print( "="*47 )
            htmlEncoding = chardet.detect( html )
            print( "type(html): ",type(html) )
            print( "="*47 )
            print( "htmlEncoding: ",htmlEncoding )
            print( "="*47 )
            print( "html: ",html.decode("utf-8") )
        html = html.decode("utf-8")
    except:
        return None
    return html


# 从网页源码中获取图片地址
def getImg(html):
    global x
    reg = r'src[\s]*=[\s]*"(.*?\.(jpg|bmp|png|gif))"' # 分组 正则表达式模式
    #reg = r'(http.*?\.jpg)'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html) #查找字符串所有出现的正则表达式模式，返回一个匹配列表
    #priFix = "http://www.trustrobot.cn"
    #imglist = [priFix + url for url in imglist]
    print(imglist)
    for imgurl in imglist:
        try:#图片原地址直接下载
            urllib.request.urlretrieve(imgurl[0],'images/%s.jpg'%x)
            x += 1
        except:#图片原地址通过解析需要加上网址第一层域名解析
            print("the first level ExceptError: ",imgurl)
            try:
                priFix = parseURL( URL )
                imgurlNew = priFix + imgurl[0]
                print("imgurlNew: ",imgurlNew)
                urllib.request.urlretrieve(imgurlNew,'images/%s.jpg'%x)
                x += 1
            except:
                print("the second level ExceptError: ",imgurl)
            pass

def getImgRromURLLinks( html ):
    htmlLinks = getURLLinks( html )
    for link in htmlLinks:
        currentHtmlContent = getHtml(link)
        if currentHtmlContent != None:
            getImg(currentHtmlContent)
            #break
    pass

# 从单个页面出发
def getURLLinks( html ):
    htmlLinkStr = r'(?<=href=\").*?(?=\")|(?<=href=\').*?(?=\')'#正则表达式扩展表示法
    htmlLinkReg = re.compile(htmlLinkStr)
    pageLinks = re.findall(htmlLinkReg,html)
    result = []
    print( pageLinks )
    result.append(URL)
    for link in pageLinks:
        if samePreFix( link ):
            print( link )
            if link not in result:
                result.append( link )
        elif link[0] == '/':
            priFix = parseURL( URL )
            imgurlNew = priFix + link
            result.append( imgurlNew )
    print("result: ",result)
    print("len(result): ",len(result))
    
    return result
    pass

def samePreFix( link ):
    if len(link) < len( URL ):
        return False
    elif  URL == link[0:len(URL)]:
        return True
    else:
        return False
    pass

def parseURL( url ):
    head = url.split("//")[0] + "//"
    return head + url.split("//")[1].split('/')[0] 
    #return firstLevelDomain = url.split("//")[1].split('/')[0]

#html = getHtml("http://www.trustrobot.cn/index.php/Index/companyculture")
#html = getHtml("http://www.trustrobot.cn/index.php/Index/companyprogress") #川思特网页
#html = getHtml("http://www.sru.jx.cn/") # 上饶师范学院首页
html = getHtml( URL ) 
getImgRromURLLinks( html )
#getURLLinks( html )
#getImg(html)
