#logging module
print("\nlogging module")
print("\n1")
# import logging

# logging.debug('this is a debug message')
# logging.info('this is a info message')
# logging.warning('this is a warning message')
# logging.error('this is a error message')
# logging.critical('this is a critical message')

print("\n2")
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                   datefmt='%m/%d/%Y %H:%M:%S')
logging.debug('this is a debug message')
logging.info('this is a info message')
logging.warning('this is a warning message')
logging.error('this is a error message')
logging.critical('this is a critical message')