import datetime
import logging
import os
import requests
from simplurapi.simplurapi import SimPlurAPI


if __name__ == "__main__":
    logDir = 'test/log'
    os.makedirs( logDir, exist_ok=True )
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    logFile = f'{logDir}/{timestamp}.log'
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s.%(msecs)03d - %(name)30s - %(levelname)8s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler( logFile )])
    api = SimPlurAPI( requests )
    api.config.set_to_development_mode()
    api.config.set_connection_to_http()
    test = api.get_all_automated_timers_for_self()
    print( test )
