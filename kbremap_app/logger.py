# This file is part of the kbremap project.
# Copyright (C) 2014 Nicolas Malarmey
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
# contact: elmamyra@gmail.com

import logging
from logging.handlers import RotatingFileHandler
import util
import os

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
        path = util.configPath('{}.log'.format(name))
        if not os.path.exists(util.configPath('')):
            os.makedirs(util.configPath(''))
        file_handler = RotatingFileHandler(path, 'a', 100000, 1)
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
