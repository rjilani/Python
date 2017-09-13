import ConfigParser



class ConfigReader(object):
    config = ConfigParser.ConfigParser()

    def __init__(self, path, tweetstype):
        self._path = path
        ConfigReader.config.read(self._path)
        self._tagstoparse = ConfigReader.config.get(tweetstype, 'tags_to_watch').split(',')
        self._index_type = ConfigReader.config.get(tweetstype, 'index')
        self._doc_type = ConfigReader.config.get(tweetstype, 'doc_type')
        self._searchtags = [i.replace('|', ' ') for i in self._tagstoparse]

        # Variables that contains the user credentials to access Twitter API
        ConfigReader.config.read('./config/config.ini')
        self._access_token = ConfigReader.config.get('Default', 'access_token')
        self._access_token_secret = ConfigReader.config.get('Default', 'access_token_secret')
        self._consumer_key = ConfigReader.config.get('Default', 'consumer_key')
        self._consumer_secret = ConfigReader.config.get('Default', 'consumer_secret')

    @property
    def tagstoparse(self):
        return str(self._tagstoparse)

    @property
    def index_type(self):
        return self._index_type

    @property
    def doc_type(self):
        return self._doc_type

    @property
    def searchtags(self):
        return self._searchtags

    @property
    def access_token(self):
        return self._access_token

    @property
    def access_token_secret(self):
        return self._access_token_secret

    @property
    def consumer_key(self):
        return self._consumer_key

    @property
    def consumer_secret(self):
        return self._consumer_secret
