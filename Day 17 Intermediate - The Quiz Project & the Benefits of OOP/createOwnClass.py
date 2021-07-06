class User:
    # constructor
    def __init__(self,user_id,fname,lname):
        self.id=user_id
        self.fname=fname
        self.lname=lname
        self.following=0
        self.followers=0
        
    def fullName(self):
        return self.fname+" "+self.lname    
    
    def follow(self,user):
        user.followers+=1
        self.following+=1


user1 = User('001','ajay','sahu')
user2 = User('002','chamman','sahu')
user1.follow(user2)
print(user1.fullName()) 
print(user1.following)
print(user1.followers)