import json
from YourLesson import downloads
if __name__ == "__main__":
    #s = downloads.out_course(1)
    #data = json.loads(s)
    #for course in data['dataList']:
        #print(course['courseName'],course['tcList'][0]['teachingClassID'])
        #print(type(course))

    downloads.save_to_file(type="本班课程",methods=downloads.recommended_course)
