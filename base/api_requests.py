import requests

from base.factory import LoggerFactory
from common.handle_json import dictToString, handleExcelJson, getDict
from common.get_config import getConfig
import json


class ApiRequest:
    """封装http请求，根据实际情况传参"""
    # 禁用SSL证书验证 verify=False
    @staticmethod
    def send_requests(
            method,
            url,
            data=None,
            params=None,
            headers=None,
            cookies=None,
            json=None,
            files=None,
            auth=None,
            timeout=None,
            proxies=None,
            verify=False,
            cert=None):
        host = getConfig.get_config_host()
        if params:
            params = getDict(params)
            res = requests.request(
                method=method,
                url=host + url,
                data=data,
                params=params,
                headers=headers,
                cookies=cookies,
                json=json,
                files=files,
                auth=auth,
                timeout=timeout,
                proxies=proxies,
                verify=verify,
                cert=cert)
            LoggerFactory.get_logger().info(f'请求参数是：{res.request.url}')
            LoggerFactory.get_logger().info(f'响应数据是：{res.json()}')
            # print(res.json())
            return res
        data = handleExcelJson(data)
        res = requests.request(
            method=method,
            url=host + url + '/',
            data=data,
            params=params,
            headers=headers,
            cookies=cookies,
            json=json,
            files=files,
            auth=auth,
            timeout=timeout,
            proxies=proxies,
            verify=verify,
            cert=cert)
        LoggerFactory.get_logger().info(f'请求参数是：{res.request.body}')
        LoggerFactory.get_logger().info(f'响应数据是：{res.json()}')
        # print(res.json())
        return res

if __name__ == '__main__':
    a = ApiRequest().send_requests('GET', 'count', params='{"username": "wrfwrf"}')
    # print(type(dictToString(a.json())))
