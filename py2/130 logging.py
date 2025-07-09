import logging

print(dir(logging))


logging.basicConfig(filename='example.log',
                    filemode='a',
                    format='%(name)s %(levelname)s %(message)s %(asctime)s',
                    datefmt='%Y-%B-%d %H:%M:%S',)

logging.critical('This is a critical message')
logging.error('This is an error message')
logging.warning('This is a warning message')
logging.info('This is an info message')
logging.debug('This is a debug message')

log1 = logging.getLogger('log1')
log2 = logging.getLogger('log2')

log1.warning('This is a warning message from log1')
log2.info('This is an info message from log2')
