# python
py文件打包

1.https://github.com/pyinstaller/pyinstaller 安装pyinstaller（由于只有开发版本支持3.0的版本，所以这里安装的是3.0版本的）
下好后，使用命令：python setup.py install 进行安装

2.https://sourceforge.net/projects/pywin32/files/pywin32/Build%20221/ 安装依赖Pywin32

3.找到用到的python依赖包 (urllib3) F:\install\python\Lib\site-packages
放到要执行的py文件目录（注意，需要打包的py文件里面的path 路径必须使用相对路径，例如：".\\"）
注意别忘了生成exe文件的图标，例如：cat_m.ico

4.执行命令
pyinstaller -F -w --icon=cat_m.ico exportToExcel.py

另外一种需要尝试的打包工具：
cx_Freeze
下载对应蟒蛇版本的cx_freeze
https://www.lfd.uci.edu/~gohlke/pythonlibs/#cx_freeze
执行：pip install cx_Freeze-5.1.1-cp37-cp37m-win_amd64.whl 安装cx_freeze
打开命令行，cd 到 Python 脚本目录（F:\install\python\Scripts）下，执行:
python cxfreeze-postinstall 安装完成
在需要打包的文件下建的设置的的的的.py来配置打包

执行：python setup.py build 或者执行：python setup.py bdist_msi 变成可安装文件，会自动把运行所需要的包打包进去
由于cx_freeze打包生成后的exe文件依赖于lib包，所以请在lib下运行exe文件

#视频拼接打包
用pyintaller:
在目录（F:\install\python\Lib\site-packages\moviepy）下，打开editor.py文件
修改editor.py文件,详情查看存入的editor.py文件

pyinstaller -F  --icon=cat_m.ico vedio_split.py
