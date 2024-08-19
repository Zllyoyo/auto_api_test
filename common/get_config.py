from base.read_data import ReadYaml


class getConfig:
    @staticmethod
    def get_config_host():
        config = ReadYaml('config', 'config.yml').read_data()
        # print(config)
        host = config.get('env').get('host')
        # print(host)
        return host
if __name__ == '__main__':
    getConfig().get_config_host()