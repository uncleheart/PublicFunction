import sys
import os

# log
import system.LogMoudle
system.LogMoudle.set_filepath(base_dir=os.path.dirname(sys.argv[0]),pre_dir='files')
system.LogMoudle.init()
import logging
logging.info('test')

