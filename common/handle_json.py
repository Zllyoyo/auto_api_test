import json

# 将res.json()获取到的json字典转换为json字符串
def dictToString(json_data):
    json_string = json.dumps(json_data, ensure_ascii=False) # 禁用ascii码
    return json_string


# 将excel断言中的字符串转为字典再重新序列化为json格式，这样不会因为excel中断言的填写格式而报错
def handleExcelJson(excel_json):
    json_dict = json.loads(excel_json)
    json_string = json.dumps(json_dict, ensure_ascii=False)
    return json_string

def getDict(data):
    data_dict = json.loads(data)
    return data_dict


if __name__ == '__main__':
    print(getDict('{"username": "wrfwrf"}'))
    print(type(getDict('{"username": "wrfwrf"}')))




