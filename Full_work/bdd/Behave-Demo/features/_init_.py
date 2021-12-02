import os
from distutils.command.config import config

from helper.helper_web import get_browser

my_file = (os.path.join(os.getcwd(), 'setup.cfg'))
config.read(my_file)
helper_func = get_browser(config.get('Environment', 'Browser'))
