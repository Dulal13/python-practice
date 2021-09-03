class User:
    def __init__(self,name):
        self.name = name

    def username(self):
        return self.name

    def user_count(self):

        i = 0

        for item in self.name:
            if(item.isdigit()):
                i +=1
        return i

u1 = User("johnsm78ith10")
print(u1.username())
print(u1.user_count())
