from . import *
import json
import os

headers = setting.HEADERS

def in_course(page):
    form_data = {
        "querySetting": r'''{"data": {"studentCode": "%s", "campus": "01","electiveBatchCode": "%s", "isMajor": "1","teachingClassType": "FANKC", "checkConflict": "2", "checkCapacity": "2","queryContent": "MOOC:2,"}, "pageSize": "10", "pageNumber": %s, "order": "","orderBy": "courseNumber"}'''%(setting.USER_ID,batch_item.batch,str(page))
    }
    response = session.post("http://210.39.12.30/xsxkapp/sys/xsxkapp/elective/programCourse.do",headers=headers,data=form_data)
    return response.text


def recommended_course(page):
    url = "http://210.39.12.30/xsxkapp/sys/xsxkapp/elective/recommendedCourse.do"
    form_data = {
        "querySetting": r'''{"data": {"studentCode": "%s", "campus": "01","electiveBatchCode": "%s", "isMajor": "1","teachingClassType": "TJKC", "checkConflict": "2", "checkCapacity": "2","queryContent": "MOOC:2,"}, "pageSize": "10", "pageNumber": %s, "order": "","orderBy": "courseNumber"}'''%(setting.USER_ID,batch_item.batch,str(page))
    }


    response = session.post(url=url,headers=headers,data=form_data)
    return response.text

def out_course(page):
    form_data = {
        "querySetting": r'''{"data": {"studentCode": "%s", "campus": "01","electiveBatchCode": "%s", "isMajor": "1","teachingClassType": "FAWKC", "checkConflict": "2", "checkCapacity": "2","queryContent": "MOOC:2,"}, "pageSize": "10", "pageNumber": %s, "order": "","orderBy": "courseNumber"}'''%(setting.USER_ID,batch_item.batch,str(page))
    }

    response = session.post("http://210.39.12.30/xsxkapp/sys/xsxkapp/elective/programCourse.do",headers=headers,data=form_data)
    return response.text

def public_course(page):
    form_data = {
        "querySetting": r'''{"data": {"studentCode": "%s", "campus": "01","electiveBatchCode": "%s", "isMajor": "1","teachingClassType": "XGXK", "checkConflict": "2", "checkCapacity": "2","queryContent": "MOOC:2,"}, "pageSize": "10", "pageNumber": %s, "order": "","orderBy": "courseNumber"}'''%(setting.USER_ID,batch_item.batch,str(page))
    }

    response = session.post("http://210.39.12.30/xsxkapp/sys/xsxkapp/elective/programCourse.do",headers=headers,data=form_data)
    return response.text

def sport_course(page):
    form_data = {
        "querySetting": r'''{"data": {"studentCode": "%s", "campus": "01","electiveBatchCode": "%s", "isMajor": "1","teachingClassType": "TYKC", "checkConflict": "2", "checkCapacity": "2","queryContent": "MOOC:2,"}, "pageSize": "10", "pageNumber": %s, "order": "","orderBy": "courseNumber"}'''%(setting.USER_ID,batch_item.batch,str(page))
    }

    response = session.post("http://210.39.12.30/xsxkapp/sys/xsxkapp/elective/programCourse.do",headers=headers,data=form_data)
    return response.text

def fuxiu_course(page):
    form_data = {
        "querySetting": r'''{"data": {"studentCode": "%s", "campus": "01","electiveBatchCode": "%s", "isMajor": "1","teachingClassType": "FXKC", "checkConflict": "2", "checkCapacity": "2","queryContent": "MOOC:2,"}, "pageSize": "10", "pageNumber": %s, "order": "","orderBy": "courseNumber"}'''%(setting.USER_ID,batch_item.batch,str(page))
    }

    response = session.post("http://210.39.12.30/xsxkapp/sys/xsxkapp/elective/programCourse.do",headers=headers,data=form_data)
    return response.text

def mooc(page):
    form_data = {
        "querySetting": r'''{"data": {"studentCode": "%s", "campus": "01","electiveBatchCode": "%s", "isMajor": "1","teachingClassType": "MOOC", "checkConflict": "2", "checkCapacity": "2","queryContent": "MOOC:2,"}, "pageSize": "10", "pageNumber": %s, "order": "","orderBy": "courseNumber"}'''%(setting.USER_ID,batch_item.batch,str(page))
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
