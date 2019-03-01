from YourLesson import login, downloads
from YourLesson import setting
import time

if __name__ == "__main__":

    teaching_class_type = ""

    print("请选择你选择的课程的类型: ")
    print("(A) 本班课程")
    print("(B) 方案内课程")
    print("(C) 方案外课程")
    print("(D) 校公选课")


    while True:
        case = input("请输入A,B,C,D： ")
        if case == "A" or case=="a":
            teaching_class_type="TJKC"
            break
        elif case == "B" or case == "b":
            teaching_class_type = "FANKC"
            break
        elif case == "C" or case =="c":
            teaching_class_type = "FAWKC"
            break
        elif case=="D" or case == "d":
            teaching_class_type = "XGXK"
            break
        else:
            print("输入不合法，重新输入")


    class_id = input("请输入课程id (在data文件夹下找): ")

    print("开始抢课中...")



    for i in range(setting.COUNT):
        print("第{}次抢课中...".format(str(i)))
        response = login.choose_lesson(class_id,teaching_class_type)

        if "该课程超过课容量" in response:
            print("该课程超过课容量")
            break
        elif "添加选课志愿成功" in response:
            print("抢课成功")
            break
        else:
            print(response)
        time.sleep(setting.DELAY/1000.0)

    print("抢课结束")

    print("======================")
    print("您现在选课的结果如下")
    login.query_result()

