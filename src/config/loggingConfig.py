import logging


<<<<<<< HEAD
def setup_logger(logger_name, log_file, level=logging.INFO):
=======
def setup_logger(logger_name, log_file, level=logging.DEBUG):
>>>>>>> 10bf5d926e78f5ba9d17be3c1cda14ef765eda8d
    l = logging.getLogger(logger_name)
    formatter = logging.Formatter('[ %(asctime)s ] [ %(levelname)-4s ] %(message)s')
    fileHandler = logging.FileHandler(log_file, mode='w')
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    l.setLevel(level)
    l.addHandler(fileHandler)
    l.addHandler(streamHandler)


<<<<<<< HEAD
setup_logger('dao_log', r'../log/controller_log.log')
controller_log = logging.getLogger('controller_log')

setup_logger('controller_log', r'../log/service_log.log')
service_log = logging.getLogger('service_log')

setup_logger('controller_log', r'../log/dao_log.log')
=======
setup_logger('dao_log', r'log/controller_log.log')
controller_log = logging.getLogger('controller_log')

setup_logger('controller_log', r'log/service_log.log')
service_log = logging.getLogger('service_log')

setup_logger('controller_log', r'log/dao_log.log')
>>>>>>> 10bf5d926e78f5ba9d17be3c1cda14ef765eda8d
dao_log = logging.getLogger('dao_log')
