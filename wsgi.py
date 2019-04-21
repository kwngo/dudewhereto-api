import os
from api import create_app
from config import app_config

app = create_app(app_config[os.environ['APP_SETTINGS']])
