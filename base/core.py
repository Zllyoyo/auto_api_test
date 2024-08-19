import json
import os

from base.public import filepath
from base.read_data import OperationExcel, ReadYaml
from common.handle_json import getDict


class Core:
    def __init__(self):
        pass

    # 判定excel文件中的API列对应的yaml文件，并返回yaml文件字典  文件名：yaml数据
    def ensure_data(self):
        data = OperationExcel('excel_data', 'demo.xlsx').get_excel_data()
        filenames = []
        yaml_data_dict = {}
        for filename in os.listdir(filepath('data')):
            # 检查是否为文件
            if os.path.isfile(filepath('data', filename)):
                # 分割文件名和后缀名
                basename, extension = os.path.splitext(filename)
                filenames.append(basename)
        for i in data:
            # print(i)
            api_data = str(i[3])
            if api_data in filenames:
                yaml_data = ReadYaml('data', api_data + '.yml').read_data()
                yaml_data_dict[api_data] = yaml_data
        # print(yaml_data_dict)
        return yaml_data_dict

    # 组装数据最后用来传给pytest
    def coredata(self):
        coredata_list = []  # 所有的用例数据
        excel_data = OperationExcel('excel_data', 'demo.xlsx').get_excel_data()
        yaml_data_dict = self.ensure_data()
        for key, value in yaml_data_dict.items():
            for case_data in excel_data:
                if case_data[3] == key:
                    element_list = []
                    element_list.append(case_data[0])   # 用例id
                    element_list.append(case_data[1])   # 用例模块
                    element_list.append(case_data[2])   # 用例标题
                    element_list.append(value.get('method'))    # 请求方法
                    element_list.append(value.get('url'))   # 接口地址
                    # 用excel中的参数对yaml文件中的参数进行替换
                    try:
                        for key1, value1 in getDict(case_data[4]).items():
                            for key2, value2 in yaml_data_dict[key]['param'].items():
                                if key1 == key2:
                                    yaml_data_dict[key]['param'][key2] = value1
                        element_list.append(json.dumps(yaml_data_dict[key]['param']))
                    except Exception as e:
                        print(f'{key}接口中的excel中参数为空，没有需要替换的参数')
                    # element_list.append(case_data[4])   # 请求参数
                    element_list.append(case_data[5])   # 预期结果
                    element_list.append(case_data[6])   # 是否保存响应字段
                    coredata_list.append(element_list)
        print(coredata_list)
        return coredata_list