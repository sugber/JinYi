import requests
from lib.read_excel import *
import unittest
from config.config import *
import json
from lib.case_log import *

class BaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if cls.__name__ != 'BaseCase':
            cls.data_list = excel_to_data(data_file,cls.__name__)

    def get_to_data(self,case_name):
        return get_to_case(self.data_list,case_name)

    def send_requests(self,case):
        case_name = case.get("case_name")
        url = case.get("url")
        data = case.get("args")
        headers = case.get("headers")
        method = case.get("method")
        data_type = case.get("data_type")
        expect_res = case.get("expect_res")

        if method.upper() == 'GET':
            res =requests.get(url=url,params=data)

        elif data_type.upper == 'FROM':
            res = requests.post(url=url,data=data,headers=headers)

        else:
            res = requests.post ( url=url, data=data, headers=json.loads(headers ))
            case_log(case_name,url,data,headers,expect_res,res.text)
            self.assertIn(expect_res, res.text)