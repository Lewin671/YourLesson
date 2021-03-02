# -*- coding: utf-8 -*-
# 程序入口

import downloads
import setting
import time
import sys
import choose_course

if __name__ == "__main__":

    for i in range(setting.count):
        for course in setting.courses:
            try:
                response = choose_course.start_choose(
                    course['id'], course['type'])

                if "该课程超过课容量" in response:
                    print("该课程超过课容量")
                    break
                elif "添加选课志愿成功" in response:
                    print("抢课成功")
                    break
                else:
                    print(course['name']+": "+response)
                time.sleep(setting.delay/1000.0)
            except KeyboardInterrupt:
                print("通过键盘中断退出程序")
                sys.exit()
            except:
                print("出现错误，请检查设置setting.py部分是否填写正确")

    print("抢课结束")

    print("======================")
    print("您现在选课的结果如下")
    choose_course.query_result()
