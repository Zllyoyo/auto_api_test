import pymysql

from base.read_data import ReadYaml


class OperationDb:
    config_data = ReadYaml('config', 'config.yml').read_data()
    db_config = {
        'host': f'{config_data["dataBase"]["host"]}',
        'user': f'{config_data["dataBase"]["username"]}',
        'password': f'{config_data["dataBase"]["password"]}',
        'database': f'{config_data["dataBase"]["basename"]}',
        'charset': 'utf8',
        'cursorclass': pymysql.cursors.DictCursor}

    def __init__(self):
        self.connection = pymysql.connect(**self.db_config)

    def query(self, sql):
        try:
            with self.connection.cursor() as cursor:
                # 执行查询
                cursor.execute(sql)
                # 获取所有结果
                result = cursor.fetchall()
                if len(result) == 1:
                    for value in result[0].values():
                        return value
                else:
                    return result

        finally:
            self.connection.close()

if __name__ == '__main__':
    print(OperationDb().query('select username from tb_users where password = "wrf19980122"'))
