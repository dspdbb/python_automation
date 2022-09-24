import openpyxl
import pytest

def set_da():
    # 拿到excl
    book = openpyxl.load_workbook('whj2.xlsx')
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


class Testcase:
    @pytest.mark.parametrize('case', set_da())
    def test_01(self, case):
        id = case[0]
        url = case[1]
        if url=='汪海舰':
            print('-------------------------------------------------')


