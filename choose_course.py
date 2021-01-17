# -*- coding: utf-8 -*-
# 选课相关逻辑

import setting
import util
import json
import os

headers = setting.headers
session = util.get_session()


# 查询选课结果（已经选中的课程）
def query_result():
    response = session.post(
        url=util.get_url("xsxkapp/sys/xsxkapp/elective/courseResult.do?timestamp={}&studentCode={}").format(
            util.get_timestamp(), setting.user_id),
        headers=headers)

    json_data = json.loads(response.text)
    # print(json_data['dataList'])
    index = 1
    for obj in json_data['dataList']:
        teacher_name = obj['teacherName']
        course_name = obj['courseName']
        teaching_place = obj['teachingPlace']

        print(index, end=" ")
        index = index + 1

        print("course_name is :", course_name)
        print("teacher is :", teacher_name)
        print("place and time is ", teaching_place)
        print("---------------------------------")


# 选课
def start_choose(class_id, teaching_class_type):
    form_data = {
        'addParam': (r'''{"data":{"operationType":"1","studentCode":%s,"electiveBatchCode":%s,"teachingClassId":%s,"isMajor":"1","campus":"01","teachingClassType":%s,"chooseVolunteer":"1"}}''' % (
            setting.user_id, setting.electiveBatchCode, class_id, teaching_class_type))
    }

    response = session.post(
        url=util.get_url("xsxkapp/sys/xsxkapp/elective/volunteer.do"),
        data=form_data,
        headers=headers)

    return response.text
