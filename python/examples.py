import sys
import os

# log
import System.LogMoudle
System.LogMoudle.set_filepath(base_dir=os.path.dirname(sys.argv[0]),pre_dir='files')
System.LogMoudle.init()
import logging
logging.info('test')

