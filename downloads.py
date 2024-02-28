# -*- coding: utf-8 -*-
# 下载课程信息到本地
# 不要运行这个文件，运行download_data.py

import setting
import util
import json
import os
import time


headers = setting.headers
session = util.get_session()

# 方案内课程
def in_course(page):
    form_data = {
        "querySetting": r'''{"data":{"studentCode":"%s","campus":"01","electiveBatchCode":"%s","teachingClassType":"FANKC","checkConflict":"2","isMajor":"1","queryContent":"MOOC:2,"},"pageSize":"10","pageNumber":"%s","order":"null","orderBy":"courseNumber"}'''%(setting.user_id,setting.electiveBatchCode,str(page))
    }
    response = session.post(util.get_url("xsxkapp/sys/xsxkapp/elective/programCourse.do"),headers=setting.headers,data=form_data)
    return response.text


# 推荐班级课程
def recommended_course(page):
    url = util.get_url("xsxkapp/sys/xsxkapp/elective/recommendedCourse.do")
    form_data = {
        "querySetting": r'''{"data": {"studentCode": "%s", "campus": "01","electiveBatchCode": "%s", "isMajor": "1","teachingClassType": "TJKC", "checkConflict": "2", "checkCapacity": "2","queryContent": "MOOC:2,"}, "pageSize": "10", "pageNumber": %s, "order": "","orderBy": "courseNumber"}'''%(setting.user_id,setting.electiveBatchCode,str(page))
    }

    response = session.post(url=url,headers=headers,data=form_data)
    return response.text

# 方案外课程
def out_course(page):
    form_data = {
        "querySetting": r'''{"data": {"studentCode": "%s", "campus": "01","electiveBatchCode": "%s", "isMajor": "1","teachingClassType": "FAWKC", "checkConflict": "2", "checkCapacity": "2","queryContent": "MOOC:2,"}, "pageSize": "10", "pageNumber": %s, "order": "","orderBy": "courseNumber"}'''%(setting.user_id,setting.electiveBatchCode,str(page))
    }

    response = session.post(util.get_url("xsxkapp/sys/xsxkapp/elective/programCourse.do"),headers=setting.headers,data=form_data)
    return response.text

# 公共课程
def public_course(page):
    form_data = {
        "querySetting": r'''{"data": {"studentCode": "%s", "campus": "01","electiveBatchCode": "%s", "isMajor": "1","teachingClassType": "XGXK", "checkConflict": "2", "checkCapacity": "2","queryContent": "MOOC:2,"}, "pageSize": "10", "pageNumber": %s, "order": "","orderBy": "courseNumber"}'''%(setting.user_id,setting.electiveBatchCode,str(page))
    }

    response = session.post(util.get_url("xsxkapp/sys/xsxkapp/elective/programCourse.do"),headers=setting.headers,data=form_data)
    return response.text

# 体育课程
def sport_course(page):
    form_data = {
        "querySetting": r'''{"data": {"studentCode": "%s", "campus": "01","electiveBatchCode": "%s", "isMajor": "1","teachingClassType": "TYKC", "checkConflict": "2", "checkCapacity": "2","queryContent": "MOOC:2,"}, "pageSize": "10", "pageNumber": %s, "order": "","orderBy": "courseNumber"}'''%(setting.user_id,setting.electiveBatchCode,str(page))
    }

    response = session.post(util.get_url("xsxkapp/sys/xsxkapp/elective/programCourse.do"),headers=setting.headers,data=form_data)
    return response.text

# 辅修课程
def fuxiu_course(page):
    form_data = {
        "querySetting": r'''{"data": {"studentCode": "%s", "campus": "01","electiveBatchCode": "%s", "isMajor": "1","teachingClassType": "FXKC", "checkConflict": "2", "checkCapacity": "2","queryContent": "MOOC:2,"}, "pageSize": "10", "pageNumber": %s, "order": "","orderBy": "courseNumber"}'''%(setting.user_id,setting.electiveBatchCode,str(page))
    }

    response = session.post(util.get_url("xsxkapp/sys/xsxkapp/elective/programCourse.do"),headers=setting.headers,data=form_data)
    return response.text

# 慕课
def mooc(page):
    form_data = {
        "querySetting": r'''{"data": {"studentCode": "%s", "campus": "01","electiveBatchCode": "%s", "isMajor": "1","teachingClassType": "MOOC", "checkConflict": "2", "checkCapacity": "2","queryContent": "MOOC:2,"}, "pageSize": "10", "pageNumber": %s, "order": "","orderBy": "courseNumber"}'''%(setting.user_id,setting.electiveBatchCode,str(page))
    }

    response = session.post(util.get_url("xsxkapp/sys/xsxkapp/elective/programCourse.do"),headers=setting.headers,data=form_data)
    return response.text

# 数据下载到本地
def save_to_file(type,methods):
    for i in range(1000):
        s = methods(page=i)
        print("s=",s)
        data = json.loads(s)
        time.sleep(1)  # 延迟

        if data['dataList'] is None or len(data['dataList'])==0:
            break

        path = os.path.abspath("data/"+type+('.csv'))
        #print(path)
        file = open(path,mode="a+")
        for course in data['dataList']:
            for j in range(1000):
                if len(course['tcList']) <= j:
                    break
                teacher = "\""+str(course['tcList'][j]['teacherName'])+"\""
                item = [course['courseName'],course['tcList'][j]['teachingClassID'],str(course['tcList'][j]['teachingPlace'])]
                #print(item)
                file.write(",".join(item)+","+str(teacher)+"\n")
                """
                if course['tcList'][j]['conflictDesc'] == None and (course['tcList'][j]['numberOfSelected'] < course['tcList'][j]['classCapacity']) and (course['selected'] == False):
                    file.write(",".join(item)+","+str(teacher)+"\n")
                else:
                    pass
                """

def clear_data():
    path = os.path.abspath("data")

    for dirpath,dirnames,filenames in os.walk(path, topdown=True):
        for filename in filenames:
            filepath = os.path.join(path,filename)
            with open(filepath,mode="w+") as f:
                f.write("")
                print("清空",filename)

# 下载课程相关数据到本地
def downloads():
    # 清空文件
    clear_data()
    # 下载文件
    print("正在下载课程id到data文件夹")
    save_to_file(type="方案内课程",methods=in_course)
    save_to_file(type="方案外课程",methods=out_course)
    save_to_file(type="本班课程",methods=recommended_course)
    save_to_file(type="校公选课",methods=public_course)
    save_to_file(type="体育课程",methods=sport_course)
    save_to_file(type="辅修课程",methods=fuxiu_course)
    save_to_file(type="慕课",methods=mooc)
    print("文件下载完成")