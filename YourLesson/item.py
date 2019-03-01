class VodeItem(object):
    """verify code item"""
    def __init__(self):
        self.vode = ""
        self.token = ""
        self.timestamp = ""

    def setVode(self,vode):
        self.vode = vode

    def setToken(self,token):
        self.token = token

    def setTimestamp(self,timestamp):
        self.timestamp = timestamp

    def showInfo(self):
        print("vode is {}, token is {}, timestamp is {}".format(self.vode,self.token,self.timestamp))


class LoginItem(object):
    """ login item """

    def __init__(self):
        self.token = ""

    def setToken(self,token):
        self.token = token

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
        self.batch = ""

    def setBatch(self,batch):
        self.batch = batch