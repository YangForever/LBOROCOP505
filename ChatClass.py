class User():
   def __init__(self, fullname, nickname):
        self.Ufullname = fullname
        self.Unickname = nickname

class Group():
    
    def __init__(self, name):
        self.Gname = name
        self.UserList = []

    def addUser(self, user):
        self.UserList.append([user.Ufullname, user.Unickname])

    def removeUser(self, user):
        if [user.Ufullname, user.Unickname] in self.UserList:
            self.UserList.remove([user.Ufullname, user.Unickname])
    
    def printByUsername(self):
        print "Print by Username:"
        for item in self.UserList:
            print item[0]
    
    def printByNickname(self):
        print "Print by Nickname:"
        for item in self.UserList:
            print item[1]

user1 = User("James", "mango")
user2 = User("May", "flower")

group = Group("Super group")

print "UserGroupName:" + group.Gname


group.addUser(user1)
group.addUser(user2)


group.printByUsername()
group.printByNickname()

group.removeUser(user1)

group.printByUsername()

