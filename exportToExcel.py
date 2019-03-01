# 目标：实现从文件目录拉取多语言标记中的文本，整理成excel文档
import os,sys,pdb,os.path,re,xlwt
# 获取当前路径
path = sys.path[0] or os.getcwd()
# 1.拉取当前目录目录下的所有.shtml或者html后缀的文件
# os.listdir(path)
# pdb.set_trace()
fileTypeArr = ['.shtml','.html','.js']
# 判断是否为文件
os.path.isfile(path)
# 获取文件后缀
os.path.splitext(path)

# 迭代遍历查找后缀为.shtml和html的文件
def searchFile(path,fileUrlArr):
    fileArr = os.listdir(path)
    for value in fileArr:
        valuePath = path + '\\' + value
        if os.path.isfile(valuePath) and (os.path.splitext(valuePath)[1] in fileTypeArr ) :
            fileUrlArr.append(valuePath)
            # print('对的：' + valuePath)
        if not os.path.isfile(valuePath): 
            fileUrlArr = searchFile(valuePath,fileUrlArr)
    return fileUrlArr

# 查找文档中被{#  #}包裹的多语言文本
def searchLangKey(fileUrl):
    langArr = {}
    with open(fileUrl,'r',encoding='UTF-8') as f :
        htmlString = f.read()

    list1 = re.findall("{#\s+(.*?)\s+#}",htmlString,re.M) 
    return list1

fileUrlArr = searchFile(path,[])
result = []
# 合并多语言文本到一个数组
for u in fileUrlArr:
    result = list(set(searchLangKey(u) + result))
# print(result)

# 设置表格样式
def setStyle(name,height,bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.height = height
    font.color_index = 4
    style.font = font
    return style

# excel写入
def writeExcel(fileArr):
    # 创建一个workbook并设置编码
    workbook = xlwt.Workbook(encoding = 'utf-8')
    # 创建一个workbook
    workSheet = workbook.add_sheet('i18n')

    # 写入excel
    # 参数对应 行，列，值
    # workSheet.write(0,0,'test')
    titleCol = ['msgid','en-US','en','ru','de','ja','ko','zh','HK','zh-HK','zh-TW','TW','th','vi','id','pt','fr','es','tr','ar']
    # 设置表头
    for tIndex in range(0,len(titleCol)):
        workSheet.write(0,tIndex,titleCol[tIndex])
    
    # 填充msgid内容
    for mIndex in range(1,len(fileArr)):
        workSheet.write(mIndex,0,fileArr[mIndex])

    # 保存
    workbook.save('i18n.xlsx')

# 创建入口文件
if __name__ == '__main__':
    writeExcel(result)
