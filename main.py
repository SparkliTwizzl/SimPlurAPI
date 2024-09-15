import datetime
import logging
import os
from datetime_extensions import unix_epoch_timestamp
from simplurapi.simplurapi import *


def init_logging():
    logDir = 'test/log'
    os.makedirs( logDir, exist_ok=True )
    timestamp = datetime.datetime.now().strftime( '%Y-%m-%d_%H-%M-%S' )
    logFile = f'{ logDir }/{ timestamp }.log'
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s.%(msecs)03d - %(name)30s - %(levelname)8s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler( logFile )])
    return logging.getLogger( __name__ )


if __name__ == "__main__":
    logger = init_logging()

    api = SimPlurAPI()
    api.config.set_to_development_mode()
    api.config.set_connection_to_http()

    startTime = unix_epoch_timestamp( 2024, 8, 1 )
    endTime = unix_epoch_timestamp( 2024, 9, 1 )
    test = api.analytics.get( startTime, endTime )
    logger.info( test.text )
