# 读取excl用例

import openpyxl


# 封装工具获取表单中的数据
def set_date():
    # 拿到excl
    book = openpyxl.load_workbook('whj.xlsx')
    # 找到数据在表单几
    sheet = book['Sheet1']
    list1 = []
    for item in sheet.values:
        # 不要表头
        # print(item)
        # 判断去除的数据0位是否为int
        # 把数据放到列表中
        if type(item[0]) is int:
            list1.append(item)
    return list1
