from cx_Freeze import setup, Executable
import os,sys
base = 'WIN32GUI' if sys.platform == "win32" else None
os.environ['TCL_LIBRARY'] = "D:\install\python\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = "D:\install\python\tcl\tk8.6"
    # 被打包的程序所依赖的包
packages = ['xlwt']
include_files = ['cat_m.ico']
options = {
    'build_exe': {
        'packages': packages,
        'include_files': include_files
    },

}

executables = [Executable(
    "D:\study\python\exportToExcel\exportToExcel.py", base=base, icon='cat_m.ico')]

setup(
    name="exportToExcel",
    options=options,
    version="1.0",
    description='desc of program',
    executables=executables
)
