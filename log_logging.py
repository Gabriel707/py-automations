import logging

logging.basicConfig(level=logging.DEBUG, filename='app.log',
                    filemode='a', format='%(levelname)s - %(message)s')
logging.debug('Logging no nível debug')
logging.info('Logging no nível info')
logging.warning('Logging no nível warning')
logging.error('Logging no nível error')
logging.critical('Logging nível critical')
