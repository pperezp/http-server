class ServerConfService:

    properties = {}
    SERVER_PROPS_FILE_NAME = "server.properties"

    @staticmethod
    def load():
        with open(ServerConfService.SERVER_PROPS_FILE_NAME, 'r') as file:
            lines = file.readlines()

            for line in lines:
                key, value = line.strip().split('=')
                ServerConfService.properties[key.strip()] = value.strip()

    @classmethod
    def get_int(cls, key):
        return int(ServerConfService.get(key))

    @classmethod
    def get(cls, key):
        return ServerConfService.properties.get(key)
