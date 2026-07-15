class Robot1:
    def __init__(self, name):
        self.name = name

    def introduce(self, name1):
        return f"I am a robot named {name1}"

robot1 = Robot1("Tom")
print(robot1.introduce("Tom")) 

class Robot2:
    def __init__(self, name):
        self.name = name

    def introduce2(self, name2):
        return f"I am a robot named {name2}"
    
robot2 = Robot2("Jerry")
print(robot2.introduce2("Jerry"))