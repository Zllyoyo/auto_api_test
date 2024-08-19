from jsonpath_ng import jsonpath, parse

from common.handle_json import getDict


def extract_with_jsonpath(json_data, jsonpath_expr):
    json_dict = getDict(json_data)
    # 解析 JSONPath 表达式
    jsonpath_expr_compiled = parse(jsonpath_expr)

    # 使用 jsonpath 查找数据
    results = [match.value for match in jsonpath_expr_compiled.find(json_dict)]

    # 如果结果只有一个，直接返回结果；如果有多个，返回结果列表
    return results[0] if len(results) == 1 else results


if __name__ == '__main__':
    json_data = {
        "code": 400,
        "errmsg": "用户名已存在",
    }
    print(extract_with_jsonpath(json_data=json_data, jsonpath_expr='$.code'))
