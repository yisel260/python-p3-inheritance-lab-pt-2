class Student:

    def __init__(self, greeting="",string=""):
        self.greeting = greeting if greeting else "Hey there! I'm so excited to learn stuff."
        self.string = string if string else "Pick me!"

    def hello(self):
        print(self.greeting)

    def raise_hand(self):
        print(self.string)
  

""" 
    @property
    def greeting(self):
        return self._greeting 

    @greeting.setter
    def greeting(self, greeting):
            self._greeting= greeting
       
 """

class ChattyStudent(Student):

    def hello(self):
        self.spoiler = "How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died..."
        super().hello()
        print (self.spoiler)

    def raise_hand(self):
        super().raise_hand()
        super().raise_hand()
        super().raise_hand()
        super().raise_hand()
        super().raise_hand()
        super().raise_hand()
        super().raise_hand()
        super().raise_hand()
        super().raise_hand()
        super().raise_hand()
         
        


    pass
