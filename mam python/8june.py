#                                                                        inheritance

class Parent:
    def __init__(self,value):
        self.value=value

    def apple(self):
        print(f"parent apple block {self.value}")

    def google(self):
        print("parent google block")
        self.apple()

#p=Parent(10)
#p.apple()       
#p.google()

#case1#....child class having independent method

class child1(Parent):
    def __init__(self,value):
        super().__init__(value)

    def yahoo(self):
        print("child1 yahoo")

#case2#....child class overridding parrent class

class child2(Parent):
    def __init__(self,value):
        super().__init__(value)

    def apple(self):
        print(f"child2 apple {self.value}")

#child2(10).google()

#case3#child class overriding parent class function and re-implementing same function of parent class..

class child3(Parent):
    def __init__(self,value):
        super().__init__(value)

    def apple(self):
        print(f"child2 apple {self.value}")
        super().apple()

#child3(10).apple()   

#case4#child class having a seperate attribute in __init__ method

class child4(Parent):
    def __init__(self,value,extra_value):
        #super.__init__(value)
        
        Parent.__init__(self,value)
        self.extra_value = extra_value
        

#child4(10,20).apple() 
    
#case5# child ineheriting from multiple parents

class Parent2:
    def __init__(self,a):
        self.a=self

    def facebook(self):
        print("executing parent2 facebook")
        
class child5(Parent,Parent2):
    def __init__(self,x,y):
        Parent.__init__(self,x)
        Parent.__init__(self,y)

    def whatsapp(self):
        print("executing child5 whatsapp")

#a=child5(10,20)
#a.whatsapp()
#a.facebook()

        
                                                                            #Multi-level inheritance

class A:
    def demo(self):
        print("A")

class B(A):
    def demo(self):
        print("B")
        super().demo()
        #A.demo(self)
        
class C(B):
    def demo(self):
        print("C")
        super().demo()


        
#print(C().demo())

                                                                            #hybrid inheritance

class Parent:
    def spam(self):
        print("Parent Spam")

class Child1(Parent):
    def spam(self):
        print("child1 spam")
        super().spam()

class Child2(Parent):
    def spam(self):
        print("child2 spam")
        super().spam()
       
        
class Child3(Child1,Child2):
    pass

#print(Child3.__mro__) #__mro__ method will show tha execution of class orderwise..
c=Child3()
c.spam()

class Spam:
    a=10 #class variable
    def apple (self):
        print(f"spam Apple {self.__class__.a}")

class Demo(Spam):
     #overriding class variable
    def google(self):
        print("Google")
    


