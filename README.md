# python
py文件打包

1.https://github.com/pyinstaller/pyinstaller 安装pyinstaller（由于只有开发版本支持3.0的版本，所以这里安装的是3.0版本的）
下好后，使用命令：python setup.py install 进行安装

2.https://sourceforge.net/projects/pywin32/files/pywin32/Build%20221/ 安装依赖Pywin32

3.找到用到的python依赖包 F:\install\python\Lib\site-packages
放到要执行的py文件目录（注意，需要打包的py文件里面的path 路径必须使用相对路径，例如：".\\"）

4.执行命令
pyinstaller -F -w --icon=cat_m.ico exportToExcel.py

另外一种需要尝试的打包工具：
cx_Freeze
