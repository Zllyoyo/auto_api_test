from base.db_operation import OperationDb
from base.factory import LoggerFactory
from base.global_vars import global_instance
from common.handle_json import getDict
from common.jsonpath import extract_with_jsonpath
from common.re_match import match_sql, match_param


class Assert:
    @staticmethod
    def asert_contrast(
            code=200,
            data=None,
            result_code=None,
            result_data=None):
        """验证code码和响应数据"""
        # 预期结果中code正确且data都填写时
        if result_code != code:
            return False
        if data:
            LoggerFactory().get_logger().info(
                '进行验证data：\n预期返回：' +
                str(data) +
                '\t\t\t实际返回：' +
                str(result_data))
            try:
                for key1, value1 in getDict(data).items():
                    if key1 in getDict(result_data).keys():
                        if match_param(str(value1)):
                            a, b = match_param(str(value1))
                            # print(str(extract_with_jsonpath(
                            #     global_instance.res_save_dict[a], b)))
                            # print(getDict(result_data)[key1])
                            assert str(getDict(result_data)[key1]) == str(extract_with_jsonpath(
                                global_instance.res_save_dict[a], b))
                            continue
                        if match_sql(str(value1)):
                            a = match_sql(str(value1))
                            b = OperationDb().query(a)
                            # print(b)
                            # print(getDict(result_data)[key1])
                            assert str(getDict(result_data)[key1]) == str(b)
                            continue
                        assert str(getDict(result_data)[key1]) == str(value1)
                    else:
                        LoggerFactory().get_logger().info(
                            f'断言失败，实际结果中无该字段{key1}')
                        return False
                LoggerFactory().get_logger().info('验证通过')
                return True
            except AssertionError as e:
                LoggerFactory().get_logger().warning('断言失败：' + str(e))
                return False
