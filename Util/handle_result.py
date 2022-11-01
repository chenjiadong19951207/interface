#coding=utf-8
import sys
import os
import configparser
base_path = os.getcwd()
sys.path.append(base_path)
import json
from deepdiff import DeepDiff
from Util.handle_json import get_value
'''[
        {"1006,":"token error"},
        {"10001":"用户名错误"},
        {"10002":"密码错误"}
    ]'''

def handle_result(url,code):
    data = get_value(url,"/Config/code_message.json")
    if data !=None:
        for i in data:
            message = i.get(str(code))
            if message:
                return message
    return None