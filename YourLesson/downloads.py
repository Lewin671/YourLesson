from . import session
from . import login_item
from . import batch_item
from . import setting
import json
import os


def in_course(page):
    form_data = {
        "querySetting": r'''{"data": {"studentCode": "%s", "campus": "01","electiveBatchCode": "%s", "isMajor": "1","teachingClassType": "FANKC", "checkConflict": "2", "checkCapacity": "2","queryContent": "MOOC:2,"}, "pageSize": "10", "pageNumber": %s, "order": "","orderBy": "courseNumber"}'''%(setting.USER_ID,batch_item.batch,str(page))
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        'Referer': 'http://210.39.12.30/xsxkapp/sys/xsxkapp/*default/grablessons.do?token={}'.format(login_item.token),
        'token': login_item.token,
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    response = session.post("http://210.39.12.30/xsxkapp/sys/xsxkapp/elective/programCourse.do",headers=headers,data=form_data)
    return response.text


def recommended_course(page):
    url = "http://210.39.12.30/xsxkapp/sys/xsxkapp/elective/recommendedCourse.do"
    form_data = {
        "querySetting": r'''{"data": {"studentCode": "%s", "campus": "01","electiveBatchCode": "%s", "isMajor": "1","teachingClassType": "TJKC", "checkConflict": "2", "checkCapacity": "2","queryContent": "MOOC:2,"}, "pageSize": "10", "pageNumber": %s, "order": "","orderBy": "courseNumber"}'''%(setting.USER_ID,batch_item.batch,str(page))
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        'Referer': 'http://210.39.12.30/xsxkapp/sys/xsxkapp/*default/grablessons.do?token={}'.format(login_item.token),
        'token': login_item.token,
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    response = session.post(url=url,headers=headers,data=form_data)
    return response.text

def out_course(page):
    form_data = {
        "querySetting": r'''{"data": {"studentCode": "%s", "campus": "01","electiveBatchCode": "%s", "isMajor": "1","teachingClassType": "FAWKC", "checkConflict": "2", "checkCapacity": "2","queryContent": "MOOC:2,"}, "pageSize": "10", "pageNumber": %s, "order": "","orderBy": "courseNumber"}'''%(setting.USER_ID,batch_item.batch,str(page))
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        'Referer': 'http://210.39.12.30/xsxkapp/sys/xsxkapp/*default/grablessons.do?token={}'.format(login_item.token),
        'token': login_item.token,
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    response = session.post("http://210.39.12.30/xsxkapp/sys/xsxkapp/elective/programCourse.do",headers=headers,data=form_data)
    return response.text

def public_course(page):
    form_data = {
        "querySetting": r'''{"data": {"studentCode": "%s", "campus": "01","electiveBatchCode": "%s", "isMajor": "1","teachingClassType": "XGXK", "checkConflict": "2", "checkCapacity": "2","queryContent": "MOOC:2,"}, "pageSize": "10", "pageNumber": %s, "order": "","orderBy": "courseNumber"}'''%(setting.USER_ID,batch_item.batch,str(page))
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        'Referer': 'http://210.39.12.30/xsxkapp/sys/xsxkapp/*default/grablessons.do?token={}'.format(login_item.token),
        'token': login_item.token,
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    response = session.post("http://210.39.12.30/xsxkapp/sys/xsxkapp/elective/programCourse.do",headers=headers,data=form_data)
    return response.text

def save_to_file(type,methods):
    for i in range(1000):
        s = methods(page=i)
        data = json.loads(s)

        if len(data['dataList'])==0:
            break

        path = os.path.abspath("data/"+type+('.csv'))
        #print(path)
        file = open(path,mode="a+")
        for course in data['dataList']:
            for j in range(1000):
                if len(course['tcList']) <= j:
                    break
                teacher = "\""+str(course['tcList'][j]['teacherName'])+"\""
                item = [course['courseName'],course['tcList'][j]['teachingClassID']]
                if course['tcList'][j]['conflictDesc'] == None:
                    file.write(",".join(item)+","+str(teacher)+"\n")
                else:
                    pass
                    #print(course['tcList'][j]['conflictDesc'])

                #print(teacher)


def clear_data():
    path = os.path.abspath("data")

    for dirpath,dirnames,filenames in os.walk(path, topdown=True):
        for filename in filenames:
            filepath = os.path.join(path,filename)
            with open(filepath,mode="w+") as f:
                f.write("")
                print("清空",filename)
