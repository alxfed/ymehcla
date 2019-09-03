"""
Hello world in sqlalchemy
"""

from sqlalchemy import *
from datetime import datetime

ABS_PATH = '/media/alxfed/toca/dbase/secondbase.sqlite' # the absolute path to a database
ymehcla_path = f'sqlite:///{ABS_PATH}' # notice the _three_ slashes before the absolute path!


metadata = MetaData(ymehcla_path)