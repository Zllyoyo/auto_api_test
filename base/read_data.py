import json
import os

import xlrd
from base.public import filepath
import yaml
from base.factory import LoggerFactory
from common.handle_json import getDict


class ReadYaml:
    def __init__(self, *filename):
        self.file = filename
        self.all_data = None

    def read_data(self):
        """返回数据"""
        with open(filepath(*self.file), 'r', encoding='utf-8') as docs:
            try:
                self.all_data = yaml.safe_load(docs)
            except yaml.YAMLError as e:
                print(e)
        LoggerFactory().get_logger().info("读取的yaml文件数据：\n" + str(self.all_data))
        return self.all_data


class OperationExcel(ReadYaml):
    # 获取sheet表
    def get_sheet(self):
        book = xlrd.open_workbook(filepath(*self.file))
        # 根据索引获取sheet表
        return book.sheet_by_index(0)

    # 以列表形式读取传入文件的数据
    def get_excel_data(self):
        data = []
        # 获取第一行表头
        # title = self.get_sheet().row_values(0)
        # print(self.get_sheet().nrows)
        for row in range(1, self.get_sheet().nrows):
            row_value = self.get_sheet().row_values(row)
            data.append(row_value)
        LoggerFactory().get_logger().info("读取的excel文件数据：\n" + str(data))
        return data

#
# if __name__ == '__main__':
#     # ReadYaml('config', 'config.yml').read_data()
#     # print((OperationExcel('excel_data', 'demo.xlsx').get_excel_data()[-1]))
#     ExcelEnsureYaml().coredata()
    # print(type(OperationExcel('excel_data', 'demo.xlsx').get_excel_data()))
