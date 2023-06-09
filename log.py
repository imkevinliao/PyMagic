import logging


class Log(logging.Logger):
    def __init__(self, log_filepath=None, level=logging.DEBUG, logfile_mode='a+'):
        super().__init__(name=log_filepath)
        self.logfile_mode = logfile_mode
        self.setLevel(level=level)
        self.config()
    
    def config(self):
        formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s [line:%(lineno)d] %(message)s",
                                      datefmt="%Y-%m-%d %H:%M:%S(%p)")
        stdout_handler = logging.StreamHandler()
        stdout_handler.setFormatter(formatter)
        self.addHandler(stdout_handler)
        if self.name:
            file_handler = logging.FileHandler(filename=self.name, encoding='utf-8', mode=self.logfile_mode)
            file_handler.setFormatter(formatter)
            self.addHandler(file_handler)
"""
logger = logging.getLogger("log_module_name")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s [line:%(lineno)d] %(message)s", datefmt="%Y-%m-%d %H:%M:%S(%p)")
stdout_handler = logging.StreamHandler()
stdout_handler.setFormatter(formatter)
stdout_handler.setLevel(logging.ERROR)
logger.addHandler(stdout_handler)
file_handler = logging.FileHandler(filename="log.txt", encoding='utf-8', mode="a+")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.NOTSET)
logger.addHandler(file_handler)

logger.debug("hello,debug")
logger.error("hello,error")
logger.info("hello,info")
"""
