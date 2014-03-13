import logging
from logging.handlers import RotatingFileHandler
import util


class Logger(logging.Logger):
    ACTION = 11
    SEND = 12
    RECEIVE = 13
    HANDLER = 14
    def __init__(self, name, consoleLvl=0, debug=False):
        logging.Logger.__init__(self, name)
        logging.addLevelName(Logger.ACTION, 'ACTION')
        logging.addLevelName(Logger.SEND, 'SEND')
        logging.addLevelName(Logger.RECEIVE, 'RECEIVE')
        logging.addLevelName(Logger.HANDLER, 'HANDLER')
        self.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s :: %(levelname)-7s :: %(message)s')
        file_handler = RotatingFileHandler(util.configPath('{}.log'.format(name)), 'a', 100000, 1)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        self.addHandler(file_handler)
        if debug:
            steam_handler = logging.StreamHandler()
            handler_formatter = logging.Formatter('%(levelname)-7s: %(message)s')
            steam_handler.setLevel(0)
            steam_handler.setFormatter(formatter)
            steam_handler.setFormatter(handler_formatter)
            self.addHandler(steam_handler)
            
    def action(self, msg, *args, **kwargs):
        self.log(Logger.ACTION, msg, *args, **kwargs)
        
    def send(self, msg, *args, **kwargs):
        self.log(Logger.SEND, msg, *args, **kwargs)

    def recv(self, msg, *args, **kwargs):
        self.log(Logger.RECEIVE, msg, *args, **kwargs)
        
    def handler_(self, msg, *args, **kwargs):
        self.log(Logger.HANDLER, msg, *args, **kwargs)
