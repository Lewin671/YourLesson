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

    case = input("请输入A,B,C,D： ")

    if case == "A":
        teaching_class_type="TJKC"
    elif case == "B":
        teaching_class_type = "FANKC"
    elif case == "C":
        teaching_class_type = "FAWKC"
    elif case=="D":
        teaching_class_type = "XGXK"
    else:
        print("输入不合法，程序退出")
        exit(-1)

    class_id = input("请输入课程id (在data文件夹下找): ")

    print("开始强课中...")



    for i in range(setting.COUNT):
        print("第{}次抢课中...".format(str(i)))
        login.choose_lesson(class_id,teaching_class_type)
        login.query_result()
        time.sleep(setting.DELAY/1000.0)

    print("抢课结束")

