import setting
import util
import json
import os

headers = setting.headers
session = util.get_session()


# 获取coolie值
def get_cookie():
    response = session.get(util.get_url("xsxkapp/sys/xsxkapp/*default/index.do"),headers=headers)
    return response.headers['Set-Cookie']

def set_cookie():
    headers['Cookie'] = get_cookie()

def get_token():
    post_data = {
        "timestamp" : str(util.get_timestamp())
    }
    response = session.post(url=util.get_url("xsxkapp/sys/xsxkapp/student/4/vcode.do"),headers=headers,data=post_data)
    # 注意此时返回的是json数据文本
    # 用json工具转换成对象
    obj = json.loads(response.text)
    return obj['data']['token']



def query_dict():
    data = {"timestamp",util.get_timestamp()}
    response = session.get(util.get_url("xsxkapp/sys/xsxkapp/publicinfo/dictionary.do"),data=data)
    print(response.text)


# 查询选课结果（已经选中的课程）
def query_result():
    response = session.post(
        url="http://210.39.12.30/xsxkapp/sys/xsxkapp/elective/courseResult.do?timestamp=1551366163666&studentCode={}".format(
            setting.user_id),
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
            setting.user_id, batch_item.batch, class_id, teaching_class_type))
    }

    response = session.post(
        url="http://210.39.12.30/xsxkapp/sys/xsxkapp/elective/volunteer.do",
        data=form_data,
        headers=headers)

    return response.text