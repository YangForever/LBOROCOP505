import requests
import json
import random
import time
import string

PATH = 'http://127.0.0.1:5000/todo/api/v1.0/tasks'
headers = {
       'content-type':'application/json'
}

class BaseStation():
    def __init__(self, b_id, location, capacity):
        self.UniqueID = b_id
        self.location = location
        self.capacity = capacity
        self.session = requests.session()
   
#def ShowInfo(self):
#    r = self.session.get("http://158.125.165.2:5000/todo/api/v1.0/tasks", headers=headers)
#    print r.text   


   
#    def ShowItem(self, id):
#        r = self.session.get("http://158.125.165.2:5000/todo/api/v1.0/tasks/" + str(id), headers=headers)
#        print r.text   

# Inform Base Info to Data processor
    def Base_inform(self, info):
        r = self.session.post(PATH, data=info, headers=headers)
        
# Transfer Phone info
    def Phone_data(self, info):
        r = self.session.post(PATH, data=info, headers=headers)

#   def ModifyItem(self, id, item):
#        r = self.session.put("http://158.125.165.2:5000/todo/api/v1.0/tasks/" + str(id), data=item, headers=headers)   """
    
#   def DeleteItem(self, id):
#        r = self.session.delete("http://158.125.165.2:5000/todo/api/v1.0/tasks/" + str(id), headers=headers)"""

def InitPhoneConn(b_capacity):
    p_num = random.randint(1, b_capacity)
    p_number = []
    for i in range(0, p_num):
        p_number.append("".join(['0']+ random.sample(string.digits, 10)))
    return p_num, p_number

def InitBase():
    b_info = raw_input("Input valid infomation of Base in a format (id,base_location,capacity): ")
    b_info = b_info.strip('\n').split(',')
    base = BaseStation(int(b_info[0]), b_info[1], int(b_info[2]))
    return base

def ShowPhoneInfo(p_number):
    info_list = []
    for number in p_number:
        dic = {}
        dic['number'] = number
        dic['basestation'] = b.location
        dic['conntime'] = time.ctime(time.time())
        print "phone: " + number + " connected with base " + b.location + ' ' + str(b.UniqueID) + ' on ' + time.ctime(time.time())
        info_list.append(dic)
        time.sleep(2)
    return info_list

def SendPhoneInfo(Base, info_list):
    info_list = json.dumps(info_list)
    print info_list
    Base.Phone_data(info_list)

def SendBaseInfo(Base):
    dic = {"b_id":str(b.UniqueID), "b_location":b.location, "b_capacity":b.capacity}
    info = json.dumps(dic)
    Base.Base_inform(info)

if __name__ == "__main__":
    b = InitBase()
    print b.UniqueID, b.location, b.capacity
    SendBaseInfo(b)
    time.sleep(1)
    p_num, p_number = InitPhoneConn(b.capacity)
    info_list = ShowPhoneInfo(p_number)
    SendPhoneInfo(b, info_list)
