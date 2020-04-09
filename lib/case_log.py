from config.config import *

def case_log(case_name,url,data,headers,expect_res,res):
    logging.info ( "测试名称：{}".format ( case_name ) )
    logging.info ( "接口地址：{}".format ( url ) )
    logging.info ( "请求参数：{}".format ( data ) )
    logging.info ( "请求类型：{}".format ( headers ) )
    logging.info ( "预期结果：{}".format ( expect_res ) )
    logging.info ( "实际结果：{}".format ( res ) )

if __name__ == '__main__':
    logging.info("hello")