from configparser import ConfigParser


class OnlineConfiguration:
    def __init__(self, filename: str):
        self._config_parser = ConfigParser()
        with open(filename, 'r') as fd:
            self._config_parser.read_file(fd)

    @property
    def token(self):
        return self._config_parser.get('DEFAULT', 'token')
