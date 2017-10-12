import requests
import json

headers = {
       'content-type':'application/json'
}

class Client(object):
    def __init__(self):
        object.__init__(self)
        self.session = requests.session()

    def ShowInfo(self):
        r = self.session.get("http://158.125.165.2:5000/todo/api/v1.0/tasks", headers=headers)
        print r.text

    def ShowItem(self, id):
        r = self.session.get("http://158.125.165.2:5000/todo/api/v1.0/tasks/" + str(id), headers=headers)
        print r.text

    def CreateItem(self, item):
        r = self.session.post("http://158.125.165.2:5000/todo/api/v1.0/tasks", data=item, headers=headers)
    
    def ModifyItem(self, id, item):
        r = self.session.put("http://158.125.165.2:5000/todo/api/v1.0/tasks/" + str(id), data=item, headers=headers)
    
    def DeleteItem(self, id):
        r = self.session.delete("http://158.125.165.2:5000/todo/api/v1.0/tasks/" + str(id), headers=headers)

if __name__ == "__main__":
    c = Client()
    print "show all items:"
    c.ShowInfo()
    
    print "show id == 1"
    c.ShowItem(1)
    print "create new item"
    data = {"title":"Python class", "description":"Easy"}
    data = json.dumps(data)
    c.CreateItem(data)
    c.ShowInfo()
    
    print "modify id-3 item"
    data = {"id":"3", "title":"Java Class", "description":"Hard", "done":False}
    data = json.dumps(data)
    c.ModifyItem(3, data)
    c.ShowInfo()
    
    print "delete id-3 item"
    c.DeleteItem(3)
    c.ShowInfo() 
