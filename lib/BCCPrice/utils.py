import os, errno, ConfigParser, logging, pdb, requests, requests_cache

from os.path import expanduser

class UtilsBase():
    # future optional introspection hooks
    pass
        
class Load(UtilsBase):

    class Config(object):
        def __init__(self, configFile=None):
            # print 'iniose %s'% path # fixne, should get path from mains calling class
     
            # pdb.set_trace()
            Load.Filesystem.mkpath(os.path.dirname(configFile))
            self.path = configFile
            self.config = ConfigParser.RawConfigParser()
            self.config.read(configFile)



        def getConfig(self, option):
            # derive the section name from self
            try:
              return self.config.get(self.__class__.__name__.lower(), option)
            except ConfigParser.NoSectionError:
              return

        def getConfigObject(self):
            return self.config

    class Logger(Config):
        def __init__(self, namespace="main", level=logging.ERROR, configFile= None):
            super( Load.Logger, self).__init__(configFile=configFile)
            self.logger = logging.getLogger(namespace)
            self.logger.setLevel(level)
            ch = logging.StreamHandler()
            ch.setLevel(level)
            format = self.getConfig("format") or '%(levelname)s:%(message)s'
            formatter = logging.Formatter(format)         
            ch.setFormatter(formatter)
            self.logger.addHandler(ch)
    
        def log(self, level, msg, *args, **kwargs):
            self.logger.log(level, msg, *args, **kwargs)
    
    class Network(Config):
            def __init__(self, cachepath="/var/tmp/utilscache", backend='sqlite', expiration= None, configFile= None):
                super( Load.Network, self).__init__(configFile=configFile)
                self.logger = Load.Logger("network", configFile = configFile)
                derived_exipration = expiration or int(self.getConfig('cache_expire'))
                self.cache = requests_cache.install_cache(cachepath, backend=backend, expire_after=derived_exipration)
        
            def get_json(self, path):
                response = requests.get(path)
                self.logger.log(logging.DEBUG, "Request %s cached: %s" % (response, response.from_cache))
                return response.json()

    class Filesystem(Config):
                @staticmethod
                def mkpath(path):
                    try:
                        os.makedirs(path)
                    except OSError as exception:
                        if exception.errno != errno.EEXIST:
                            raise

    class ErrorHandler(Config):
                @staticmethod
                def raise_error(msg):
                    print "TODO! %s" % msg

    class PromptHooks(Config):
                @staticmethod
                def create_prompthook(hook):
                    print "TODO! %s" % hook
                
                @staticmethod
                def run_prompthook(hook):
                    print "TODO! %s" % hook

