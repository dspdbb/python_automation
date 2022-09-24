import openpyxl
import pytest
# 1.文件名test_或者_test_
# 2。类 大写的Test
from api_i import in_request
from pull_data import set_date


class Testcase:
    # 一个test代表一条用例，1.读取出表格数据之后  拿掉接口地址   接口参数    请求方式
    # in_request(method, url, data): 一条用例
    @pytest.mark.parametrize('case', set_date())
    def test_01(self, case):
        id = case[0]
        url = case[1]
        data = case[2]
        method = case[3]
        expect = case[4]
        res = in_request(method, url, data)
        print(res.json())
        # 断言
        # 只要id没显示错误就不报错
        try:
            assert str(expect) == res.json()['cityid']
            rel = '用例成功'
        except Exception as e:
            rel = '用例失败'
        # 写回excl
        a = openpyxl.load_workbook('whj.xlsx')
        sheet = a['Sheet1']
        print(sheet)
        # 行数不能写死
        # cell方法将获取到的表个位置的值用等号后面的参数进行替换
        sheet.cell(id+1,6).value =rel
        a.save('whj.xlsx')

