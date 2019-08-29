from YourLesson.setting import BATCH


class CourseItem(object):
    def __init__(self):
        self.teacher_name = ""
        self.teaching_place = ""
        self.course_name = ""

    def set_teacher_name(self,teacher_name):
        self.teacher_name = teacher_name

    def set_teaching_place(self,teaching_place):
        self.teaching_place = teaching_place

    def set_course_name(self,course_name):
        self.course_name = course_name

    def show(self):
        print("course_name is :",self.course_name)
        print("teacher is :", self.teacher_name)
        print("place and time is ",self.teaching_place)
        print("---------------------------------")

class  BatchItem(object):
    """docstring for  BatchItem"""
    def __init__(self):
        super( BatchItem, self).__init__()
        self.batch = BATCH

    def setBatch(self,batch):
        self.batch = batch