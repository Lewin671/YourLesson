# 注： 
# 本班课程： 'TJKC'
# 方案内课程: 'FANKC'
# 方案外课程： 'FAWKC'
# 校公选课： 'XGXK'
# 慕课: "ＭOOC"，
# 辅修课程: "FXKC"，
# 体育课程:"TYKC"
# example
# course =[
#    {'type':'TJKC','id':'201820192150286000103'},
#    {'type':'FAWKC','id':'201820192150286000103'}
#    ]

# 请按照以上格式填写course，课程id和类型在data文件夹 

from YourLesson import login, downloads
from YourLesson import setting
import time

courses =[
    {'id':'201920201190114000103','type':'FXKC','name':"解析几何(徐希)"},
    {'id':'201920201990008000101','type':'MOOC','name':"拓展英语词汇"},
    {'id':'201920201990039000101','type':'MOOC','name':"走进性科学"},
]

if __name__ == "__main__":

    for i in range(setting.COUNT):
        for course in courses:
            try:
                response = login.choose_lesson(course['id'],course['type'])

                if "该课程超过课容量" in response:
                    print("该课程超过课容量")
                    break
                elif "添加选课志愿成功" in response:
                    print("抢课成功")
                    break
                else:
                    print(course['name']+": "+response)
                time.sleep(setting.DELAY/1000.0)
            except:
                print("something wrong")

    print("抢课结束")

    print("======================")
    print("您现在选课的结果如下")
    login.query_result()
