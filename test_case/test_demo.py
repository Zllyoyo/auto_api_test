import json

import pytest

from base.api_requests import ApiRequest
from base.assert_contrast import Assert
from base.core import Core
from base.db_operation import OperationDb
from base.read_data import ReadYaml, OperationExcel
from common.handle_json import dictToString, handleExcelJson, getDict
from base.global_vars import global_instance
from common.jsonpath import extract_with_jsonpath
from common.re_match import match_param, match_sql


class TestClass:
    """用例模版编写"""
    # 读取config文件数据
    # config_data = ReadYaml('config', 'config.yml').read_data()
    # 获取yaml测试用例
    # yaml_data = ReadYaml('data', 'login.yml').read_data()
    # 获取excel用例数据
    # excel_data = OperationExcel('excel_data', 'demo.xlsx').get_excel_data()
    # 获取用例数据
    execute_data = Core().coredata()
    # print(execute_data)

    def setup_class(cls):
        """编写类启动函数"""
        pass

    def tearDown_class(cls):
        """编写类关闭函数"""
        pass

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", execute_data)
    def test_1(self, data):
        """编写测试用例"""
        if data[3] == 'GET':
            jsondict = getDict(data[5])
            for key, value in jsondict.items():
                if match_param(str(value)):
                    a, b = match_param(str(value))
                    jsondict[key] = str(extract_with_jsonpath(
                        global_instance.res_save_dict[a], b))
                if match_sql(value):
                    c = match_sql(value)
                    jsondict[key] = OperationDb().query(c)
                json_str = json.dumps(jsondict)
                data[5] = json_str
            res = ApiRequest.send_requests(
                method=data[3], url=data[4], params=data[5])
            # print(res.status_code)
            if data[7] == 'Y':
                global_instance.res_save_dict[data[0]] = dictToString(
                    res.json())
            assert Assert.asert_contrast(
                data=handleExcelJson(str(
                    data[6])),
                result_code=res.status_code,
                result_data=dictToString(res.json()))
        else:
            jsondict = getDict(data[5])
            for key, value in jsondict.items():
                if match_param(str(value)):
                    a, b = match_param(str(value))
                    jsondict[key] = str(extract_with_jsonpath(
                        global_instance.res_save_dict[a], b))
                if match_sql(value):
                    c = match_sql(value)
                    jsondict[key] = OperationDb().query(c)
                json_str = json.dumps(jsondict)
                data[5] = json_str
            res = ApiRequest.send_requests(
                method=data[3], url=data[4], data=data[5])
            if data[7] == 'Y':
                global_instance.res_save_dict[data[0]] = dictToString(
                    res.json())
            # print(res.status_code)
            assert Assert.asert_contrast(
                data=handleExcelJson(str(
                    data[6])),
                result_code=res.status_code,
                result_data=dictToString(res.json()))
        print("用例id：" + str(data[0]))
        print("用例模块：" + str(data[1]))
        print("用例标题：" + str(data[2]))
        print("请求方式：" + str(data[3]))
        print("请求地址：" + str(data[4]))
        print("请求参数：" + str(data[5]))
        print("预期结果：" + str(data[6]))


if __name__ == '__main__':
    pytest.main(["-s", "-v"])
