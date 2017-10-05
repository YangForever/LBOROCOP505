class Student():
    def __init__(self, name):
        self.sname = name
        self.modules = []
    def AddModules(self, mName):
        self.modules.append(mName)
    def DeleteModules(self, mName):
        self.modules.remove(mName)
    def ChangeModules(self, mName, newName):
        self.modules.remove(mName)
        self.modules.append(newName)
    def ShowModules(self):
        print self.modules

stu = Student("Yang")
stu.AddModules('cop505')
stu.AddModules('cop404')
stu.AddModules('cop303')
print 'add finished'
stu.ShowModules()
print 'delet 303'
stu.DeleteModules('cop303')
stu.ShowModules()
print 'change 404 and 606'
stu.ChangeModules('cop404', 'cop606')
stu.ShowModules()


