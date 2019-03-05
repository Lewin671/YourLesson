from . import session, vode_item, login_item, batch_item
from . import setting
from . import item
import json
import os


def get_vode():
    response = session.get(setting.VODE_URL, headers=setting.HEADERS)
    json_data = json.loads(response.text)
    print(json_data['msg'])

    data = json_data['data']

    vode_item.setTimestamp(json_data['timestamp'])
    vode_item.setToken(data['token'])

    response = session.get("http://210.39.12.30/xsxkapp/sys/xsxkapp/student/vcode/image.do?vtoken=%s"%vode_item.token)
    path = os.path.abspath('pic/img.png')
    with open(path,mode="wb+") as f:
        f.write(response.content)



def login():
    get_vode()
    headers = setting.HEADERS
    headers['Referer'] = "http://210.39.12.30/xsxkapp/sys/xsxkapp/*default/index.do"

    while(True):
        vode = input("请输入验证码（在pic文件夹下的img.png)： ")
        vode_item.setVode(vode)
        data = {
            "loginName": setting.USER_ID,
            "loginPwd": setting.PASSWORD,
            "verifyCode": vode_item.vode,
            "vtoken": vode_item.token
        }

        response = session.post(
            url="http://210.39.12.30/xsxkapp/sys/xsxkapp/student/check/login.do?timestrap={}".format(
                vode_item.timestamp),
            headers=headers,
            data=data)
        if "登录成功" in response.text:
            print("登录成功")
            break
        else:
            print("验证码不正确，请重新输入")

    json_data = json.loads(response.text)
    login_item.setToken(json_data['data']['token'])


def query_dict():
    response = session.get(
        "http://210.39.12.30/xsxkapp/sys/xsxkapp/publicinfo/dictionary.do?timestamp=1551364761473")
    print(response.text)


# 查询选课结果（已经选中的课程）
def query_result():
    headers = setting.HEADERS
    headers['token'] = login_item.token
    response = session.get(
        url="http://210.39.12.30/xsxkapp/sys/xsxkapp/elective/courseResult.do?timestamp=1551366163666&studentCode={}".format(
            setting.USER_ID),
        headers=headers)

    # print(response.text)
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
        'addParam':(r'''{"data":{"operationType":"1","studentCode":%s,"electiveBatchCode":%s,"teachingClassId":%s,"isMajor":"1","campus":"01","teachingClassType":%s}}''' % (
            setting.USER_ID, batch_item.batch, class_id, teaching_class_type))
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        'Referer': 'http://210.39.12.30/xsxkapp/sys/xsxkapp/*default/grablessons.do?token={}'.format(login_item.token),
        'token': login_item.token
    }

    response = session.post(
        url="http://210.39.12.30/xsxkapp/sys/xsxkapp/elective/volunteer.do",
        data=form_data,
        headers=headers)

    return response.text


def bash_open():
    response = session.get(
        "http://210.39.12.30/xsxkapp/sys/xsxkapp/elective/batch.do?timestamp=1551403192473")
    json_data = json.loads(response.text)
    batch_item.setBatch(json_data['dataList'][0]['code'])
    #print("bashcode is ", json_data['dataList'][0]['code'])
