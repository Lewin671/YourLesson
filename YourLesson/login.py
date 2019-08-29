from . import *
from . import setting
from . import item
import json
import os

headers = setting.HEADERS

def query_dict():
    response = session.get(
        "http://210.39.12.30/xsxkapp/sys/xsxkapp/publicinfo/dictionary.do?timestamp=1551364761473")
    print(response.text)


# 查询选课结果（已经选中的课程）
def query_result():
    response = session.post(
        url="http://210.39.12.30/xsxkapp/sys/xsxkapp/elective/courseResult.do?timestamp=1551366163666&studentCode={}".format(
            setting.USER_ID),
        headers=headers)

    json_data = json.loads(response.text)
    # print(json_data['dataList'])
    index = 1
    for obj in json_data['dataList']:
        course_item = item.CourseItem()

        course_item.set_teacher_name(obj['teacherName'])
        course_item.set_course_name(obj['courseName'])
        course_item.set_teaching_place(obj['teachingPlace'])

        print(index,end=" ")
        index = index + 1
        course_item.show()


def choose_lesson(class_id, teaching_class_type):
    form_data = {
        'addParam':(r'''{"data":{"operationType":"1","studentCode":%s,"electiveBatchCode":%s,"teachingClassId":%s,"isMajor":"1","campus":"01","teachingClassType":%s,"chooseVolunteer":"1"}}''' % (
            setting.USER_ID, batch_item.batch, class_id, teaching_class_type))
    }

    response = session.post(
        url="http://210.39.12.30/xsxkapp/sys/xsxkapp/elective/volunteer.do",
        data=form_data,
        headers=headers)

    return response.text