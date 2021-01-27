import pyautogui
import pyautogui
import autopy
import time
import os
import pyperclip
import xlwings as xw

# 自动发信息（读取Excel里面对象和内容，查找）
# 设置安全区域
# 名字不匹配 容易出错。需要在查找名字后，有进一步判断。 ToDo
# 发错位置 名字没对上。然后是教科学院怎么未发名单里面。 ToDo

messageExlPath = r"C:\Users\71522\Desktop\gtihubLocal\Python\python343\wechatDemo\messages.xlsx"
headImgPath = r"C:\Users\71522\Desktop\gtihubLocal\Python\python343\wechatDemo\imgs\weChat_Head_dell.png"
friendsPath = r"C:\Users\71522\Desktop\gtihubLocal\Python\python343\wechatDemo\imgs\friends"
os.startfile(r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe")
sht1 = xw.Book(messageExlPath).sheets["sheet1"]
sht2 = xw.Book(messageExlPath).sheets["sheet2"]

class weChatAi():
    def __init__(self,name,headimgLoc):
        self.name = name
        self.headimgLoc = headimgLoc
    def getMessage(self):
        pass
    def setMessage(self):
        pass
    def sendMessage(self,friend,message):
        autopy.mouse.smooth_move(self.headimgLoc.x,self.headimgLoc.y)# 平滑到查找朋友区域
        autopy.mouse.smooth_move(self.headimgLoc.x+80,self.headimgLoc.y)# 平滑到查找朋友区域 图像区域向右边80
        pyautogui.doubleClick()
        #pyautogui.typewrite(friend) #键盘输入 auto.typewrite('test',interval=0.25)  只能输入英文
        pyperclip.copy(friend)#复制内容str1，内容可设置为中文等
        #pyperclip.paste()# paste()用不了,可能被微信禁止
        pyautogui.hotkey('ctrl','v')
        time.sleep(1)
        pyautogui.press('enter') #按下键盘的回车键
        time.sleep(1)
        if self.verify(friend) == None:
            print(friend + " Img is not found")
            return None
        pyperclip.copy(message)
        pyautogui.hotkey('ctrl','v')
        pyautogui.press('enter')
        return message
        pass
    def sendExlsMessage(self,messageLL):
        for i in range(len(messageLL)):
            if self.sendMessage(messageLL[i][0],messageLL[i][1]) != None:
                sht1.range("C"+messageLL[i][2]).value = "Done" #消息发送成功，状态改为Done
                sht1.range("D"+messageLL[i][2]).value = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())#消息发送时间记录
            else:
                sht1.range("C"+messageLL[i][2]).value = "Error" #消息发送成功，状态改为Done
                sht1.range("D"+messageLL[i][2]).value = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())#消息发送时间记录
    def clearBufferMessage(self):
        pyautogui.hotkey('ctrl','a')
        pyautogui.hotkey('delete')
    def verify(self,friend):
        imgPath = friendsPath + "\\" + friend + ".png"
        try:
            pos = pyautogui.locateOnScreen(imgPath)
            #print(pos)
        except IOError:
            return None
        return pos



def saveFriendsImgs(ImgLoc):
    friends = sht2.range("A2:A42").value
    print(friends)
    for i in friends:
        imgPath = friendsPath + "\\" + i + ".png"
        print(imgPath)
        autopy.mouse.smooth_move(ImgLoc.x,ImgLoc.y)# 平滑到查找朋友区域
        autopy.mouse.smooth_move(ImgLoc.x+80,ImgLoc.y)# 平滑到查找朋友区域 图像区域向右边80
        pyautogui.doubleClick()
        pyautogui.hotkey('ctrl','a')
        pyautogui.hotkey('delete')
        pyperclip.copy(i)#复制内容str1，内容可设置为中文等
        #pyperclip.paste()# paste()用不了,可能被微信禁止
        pyautogui.hotkey('ctrl','v')
        time.sleep(1)
        pyautogui.press('enter') #按下键盘的回车键
        time.sleep(0.5)
        #autopy.mouse.smooth_move(ImgLoc.x+300,ImgLoc.y-12)
        im = pyautogui.screenshot(region=(ImgLoc.x+300, ImgLoc.y-12, 120 ,30))
        im.save(imgPath)

def readMessageFromExls(exlsPath):
    mesLL =[]   
    nrows = sht1.used_range.last_cell.row
    ncols = sht1.used_range.last_cell.column
    #print("nrows:%d"%nrows)
    #print("ncols:%d"%ncols)
    for i in range(nrows):
        if sht1.range("C"+str(i+1)).value == "ToDo":
            mesLL.append([sht1.range("A"+str(i+1)).value,sht1.range("B"+str(i+1)).value,str(i+1)])    
    return mesLL





time.sleep(1)
ImgLoc = pyautogui.locateCenterOnScreen(headImgPath)
if ImgLoc != None:
    yangfanWeChat = weChatAi("杨帆",ImgLoc)
else:
    print("hean not found.")
    quit()
#yangfanWeChat.sendMessage("文件传输助手","测试") #单独发送信息
#saveFriendsImgs(ImgLoc)
messageList = readMessageFromExls(messageExlPath)
if messageList != []:
    yangfanWeChat.sendExlsMessage(messageList)
else:
    print("message not found.")
    quit()

'''
app = xw.App(visible=False, add_book=False)
wb=app.books.open(messageExlPath)

sheet1 = wb.sheets[0]

#获取Excel 行数和列数
nrows = sheet1.used_range.last_cell.row
ncols = sheet1.used_range.last_cell.column
print("nrows:%d"%nrows)
print("ncols:%d"%ncols)
print(wb.fullname)       # 输出打开的excle的绝对路径
print(sheet1.range("A1:D4").value)
#quit()
'''








