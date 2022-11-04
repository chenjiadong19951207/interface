import os
import configparser
base_path = os.getcwd()
sys.path.append(base_path)
import requests
import json
from Util.handle_cookie import write_cookie
from Util.handle_json import get_value
from Util.handle_init import handle_ini