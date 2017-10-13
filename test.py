#!coding=utf8
'''
@author: yongmao.gui
'''
import logging
from flumelogger import handler
from logging import config
#config.fileConfig("conf/logger.conf")


fh = handler.FlumeHandler(host="localhost", port=8167, type='ng')
logger = logging.getLogger("flume-logger")
logger.setLevel(logging.INFO)
logger.addHandler(fh)

logger.info("hello,world")