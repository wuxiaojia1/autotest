# -*- coding:utf-8 -*-
import requests, time, sys, re
import urllib, zlib
import pymysql
from trace import CoverageResults
import json
from idlelib.rpc import response_queue
from time import sleep
HOSTNAME = '127.0.0.1'

#读取数据库中的测试步骤
def readSQLcase():
    sql="SELECT id,apiname,apiurl,apimethod,apiparamvalue,apiresult,apistatus from apitest_apistep where apitest_apistep.Apitest_id=3"
    coon = pymysql.connect(user='root',db='autotest',passwd='123456',host='127.0.0.1',charset='utf8')
    cursor = coon.cursor()
    aa = cursor.execute(sql)
    info = cursor.fetchmany(aa)
    for i in info:
        case_list = []
        case_list.append(i)
        interfaceTest(case_list)
    coon.commit()
    cursor.close()
    coon.close()

def interfaceTest(case_list):s
    res_flags = []
    request_urls = []
    responses = []
    strinfo = re.compile('{TaskId}')
    strinfo1 = re.compile("{AssetId}")
    strinfo2 = re.compile("{PointId}")
    assetinfo = re.compile("{assetno}")
    tasknoinfo = re.compile("{taskno}")
    schemainfo = re.compile("{schema}")
    for case in case_list:
        try:
            case_id = case[0]
            interface_name = case[1]
            url = case[2]
            method = case[3]
            param = case[4]
            res_check = case[5]
        except Exception as e:
            return "测试用例格式不正确%s" %e

        if param == '':
            new_url = 'http://'+'api.test.com.cn'+url
        elif param == 'null':
            new_url =  'http://'+url
        else:
            url = strinfo.sub(TaskId,url)