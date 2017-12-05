
Python343
  01. deleteBkFiles.py(os 操作系统模块  logging 日志模块  thinket UI模块)
    ToDo:
      01. 目录指定 
      02. 后缀添加 vcm png 可选
    Do:
      01. 12:15 2016/7/23
        filedialog  askdirectory  initialdir
      02. 16:30 2016/7/23
        tkinter:Label Entry Button ttk.Combobox grid
    sticky = w 左对齐
    grid(row = ,col = )
    Label button  设置宽度 width
    Button 设置点击事件  command = deleteEvn
    
    ToDo:
      01. 打包成可执行的文件
    
    Do:
      01. 11:16 2016/7/24
        from distutils.core import setup
        import py2exe
        python setup.py py2exe
    
    ToDo:
      01  设置日志存储路径固定，已经
      02. 多个运行程序指向通一个日志文件时，向改日志文件存读
  02. reNameByAddPrefix.py
    ToDo:
      01  指定目录
      02. 根据指定文件后缀名指定文件类型
      03. 打包成exe文件

Python361
    01.爬虫
        01.urlli/images.py  下载单个网页及网页上相关链接上图片道images文件夹下面
            ToDo:
                01. 获取整个网站相关地址以及下载图片
                    http://www.trustrobot.cn/    总共html页面个数为：，今天爬了1150个页面，一共下载5844幅图片 
                02. 合肥学院网页、广西师范大学网页抓取失败，检查原因 。
            Do：
                01. 新建页面文件夹，对应文件夹下面放置下载的图片
                