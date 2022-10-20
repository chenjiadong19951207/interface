#coding=utf-8
import sys
import os

#拿到当前文件夹的路径C:\Users\1\PycharmProjects\interface\Run
base_path = os.getcwd()
#导入xx包在另一个项目文件，在自己写的程序中需要用到xx包
sys.path.append(base_path)
from collections.abc import Iterable
import json
from Utils.handle_header import get_header