import os

# 指定目录拼接文件名路径


def filepath(*fileName):
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), *fileName)


# print(os.path.join(os.path.dirname(os.path.dirname(__file__)), '111'))

# if __name__ == '__main__':
#     print(filepath('1', '2', '3'))