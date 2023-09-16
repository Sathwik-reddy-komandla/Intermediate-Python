# import logging
# logging.basicConfig(level=logging.DEBUG)
# logging.info('yiu have 20 unead msgs')
# logging.critical('You are breached')

import logging
logging.basicConfig(level=logging.DEBUG)

logger=logging.getLogger("BOB's Logger")
logger.setLevel(logging.DEBUG)

handler=logging.FileHandler('mylog.log')
handler.setLevel(logging.INFO)

formatter=logging.Formatter("%(levelname)s - %(asctime)s: %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info('This is Info message')
