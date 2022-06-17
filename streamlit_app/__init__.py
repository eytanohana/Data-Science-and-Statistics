import sys
import os

APP_DIR = os.path.dirname(__file__)
APP_BACKEND = os.path.join(APP_DIR, 'backend')
BASE = os.path.dirname(APP_DIR)
sys.path.extend([BASE, APP_DIR, APP_BACKEND])
