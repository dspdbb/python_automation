import requests


# 封装工具判断url的请求方法

def in_request(method, url, data):
    if method == "get":
        # 将拿到的数据改为字典类型
        # 因为只能接受字典类型,不能接受字符串
        data1 = eval(data)
        res = requests.get(url, data1)
    elif method == "post":
        res = requests.post(url, data)
    elif method == "delete":
        res = requests.delete(url, data)
    return res
