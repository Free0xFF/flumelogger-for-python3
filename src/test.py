'''
@author: yongmao.gui
'''
import logging
from flumelogger import handler
from logging import config
config.fileConfig("conf/logger.conf")
#fh = handler.FlumeHandler(host="10.3.157.130,10.3.157.132", port=9527, type='ng')
logger = logging.getLogger("chatbot-logger")
logger.setLevel(logging.INFO)
logger.info("hello,world!")
