import pyautogui
import autopy
import time
import threading
import xlwings as xw
from pynput.keyboard import Key,Listener,Controller# 包含控制和监控键盘的类

# 设置安全区域
# 循环直到终止键盘
# ps 会更改图片数据（libpng warning: iCCP: known incorrect sRGB profile）; 用faststone capture工具截图可被pyautoTest工具使用
#im1 = pyautogui.screenshot(r"E:\fan.yang\githubLocal\Python\Python\python343\pyautogui\imgs\screenshot1.pngmy_screenshot.png")
#button7location = pyautogui.locateOnScreen(r"E:\fan.yang\githubLocal\Python\Python\python343\pyautogui\imgs\target.png")
#采用多线程结束程序

ImgsPath = r"C:\Users\71522\Desktop\gtihubLocal\Python\python343\pyautoDemo\imgs"
keyboard = Controller()

global exitFlag
exitFlag = 0
def on_press(key):
    #print("{0} pressed".format(key))
    pass

#键盘释放监听 输出键盘按键 按ESC键退出
def on_release(key):
    global exitFlag
    print("{0} release".format(key))
    if key == Key.esc:
        exitFlag = 1
        return False

# 多线程退出判断
def exitFun():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

global imgCount
imgCount = 0   
def saveFriendsImgs():
    global imgCount,exitFlag
    while imgCount <= 12:
        t = time.gmtime()
        timeImgName = str(t.tm_year)+"_"+str(t.tm_mon)+"_"+str(t.tm_mday)+"_"+str(t.tm_hour)+"_"+str(t.tm_min)+"_"+str(t.tm_sec)
        print(timeImgName)
        imgCount = imgCount + 1
        imgPath = ImgsPath + "\\" + str(imgCount) + ".png"
        im = pyautogui.screenshot(region=(0, 0, 1920 ,1080))#全屏幕截图
        im.save(imgPath)
        time.sleep(1)
        if imgCount == 12:
            imgCount = 0
        if exitFlag == 1:
                break

#
def autoFun():
    global exitFlag
    while True:
        if exitFlag == 1:
            break
        
        point = pyautogui.locateCenterOnScreen(ImgsPath+r"\test.png")
        if point == None:
            print("未识别图片!，退出线程1，线程2还在监听！")
            #break
        saveFriendsImgs()
        #thank = pyautogui.locateCenterOnScreen(r"E:\fan.yang\githubLocal\Python\Python\python343\pyautogui\imgs\jxgb_thank.png")
        
        #print(point.x)
        #print(point.y)
        ##afpyautogui.click(x, y)#鼠标左击一次
        #autopy.mouse.smooth_move(point.x,point.y)
        #autopy.mouse.smooth_move(100,100)
        #time.sleep(1)
        ##autopy.mouse.smooth_move(280,186)
        '''
        if thank != None:
            print(x)
            print(y)
            pyautogui.click(x, y)#鼠标左击一次
            pyautogui.doubleClick()
            '''

class myThread (threading.Thread):#继承类 重写类
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开始线程：" + self.name)
        thread_fun(self.name)
        print ("退出线程：" + self.name)

def thread_fun(threadName):
    if threadName == "Thread-auto":
        autoFun()
    elif threadName == "Thread-exit":
        exitFun()

# 创建新线程
thread1 = myThread(1, "Thread-auto", 1)
thread2 = myThread(2, "Thread-exit", 2)
# 开启新线程
thread1.start()
thread2.start()
thread2.join()
thread1.join()
print ("退出主线程")



#print(button7location)



def endJudge():
    #视频正常结束(固定结束标志)
    #视频卡主不动
    pass

def back():
    pass

def selectClass():
    pass
# 获取当前屏幕分辨率
#screenWidth, screenHeight = pyautogui.size()

# 获取当前鼠标位置
#currentMouseX, currentMouseY = pyautogui.position()

# 2秒钟鼠标移动坐标为100,100位置  绝对移动
#pyautogui.moveTo(100, 100,2)
#pyautogui.moveTo(x=100, y=100,duration=2, tween=pyautogui.linear)

#鼠标移到屏幕中央。
#pyautogui.moveTo(screenWidth / 2, screenHeight / 2)

