#coding=utf-8
import sys
import os

#拿到当前文件夹的路径C:\Users\1\PycharmProjects\interface\Run
base_path = os.getcwd()
#导入xx包在另一个项目文件，在自己写的程序中需要用到xx包
sys.path.append(base_path)
from collections.abc import Iterable
from Util.handle_excel import excel_data
import json
from Util.handle_header import get_header
from Util.handle_result import handle_result,handle_result_json,get_result_json
from Util.handle_cookie import write_cookie,get_cookie_value
from Util.codition_data import get_data
from Base.base_request import request

class RunMain:
    def run_case(self):
        rows = excel_data.get_rows()
        for i in range(rows):
            cookie = None
            get_cookie = None
            header = None
            depend_data = None
            data =  excel_data.get_rows_value(i+2)
            is_run = data[2]
            if is_run == 'yes':
                is_depend = data[3]
                data1 = json.loads(data[7])
                if is_depend:
                    depend_key = data[4]
                    depend_data = get_data(is_depend)
                    data1[depend_key] = depend_data
                method = data[6]
                url = data[5]

                is_header = data[9]
                except_method = data[10]
                except_result = data[11]
                cookie_method = data[8]
                if cookie_method == 'yes':
                    cookie = get_cookie_value('app')
                if cookie_method == 'write':
                    get_cookie={"is_cookie":"app"}
                if is_header == 'yes':
                    header = get_header()
                res = request.run_main(method,url,data1,cookie,get_cookie,header)
                code = str(res['errorCode'])
                message = res['errorDesc']
                if except_method =='mec':
                    config_message = handle_result(url,code)
                    if message ==config_message:
                        excel_data.excel_write_data(i+2,13,'通过')
                    else:
                        excel_data.excel_write_data(i+2,13,'失败')
                        excel_data.excel_write_data(i+2,14,json.dumps(res))
                if except_method == 'errorcode':
                    if except_result == code:
                        excel_data.excel_write_data(i+2,14,"通过")
                    else:
                        excel_data.excel_write_data(i+2,13,'失败')
                        excel_data.excel_write_data(i+2,14,json.dumps(res))
                if except_method == 'json':
                    if code == 1000:
                        status_str = 'success'
                    else:
                        status_str ='error'
                    except_result = get_result_json(url,status_str)
                    result = handle_result_json(res,except_result)
                    if result:
                        excel_data.excel_write_data(i+2,13,'通过')
                    else:
                        excel_data.excel_write_data(i+2,13,"失败")
                        excel_data.excel_write_data(i+2,14,json.dumps(res))

if __name__ == "__main__":
    run = RunMain()
    run.run_case()
