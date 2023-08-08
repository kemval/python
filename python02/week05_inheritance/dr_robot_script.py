import random

class Robot:

    def __init__(self, name):
        
        self.name = name
        self.health_lvl = random.randint(1, 100)

    def salute(self):

        print(f"Hello, I am a Robot called {self.name}", sep='\n')

    def i_need_a_doctor(self):
        
        return self.health_lvl < 75


class DoctorRobot(Robot):

    def salute(self):

        print(f"I am the Robot-Dr. {self.name}")
        print("I will help you today.")

    def heal(self, robot):

        heal_amount = random.randint(1, 15)
        robot.health_lvl += heal_amount
        print(f"{self.name} healed {robot.name} by {heal_amount} health points.")
        
robo_doc = DoctorRobot("Super Doc")
print("\n")
robo_doc.salute()

robots = {}

for i in range(3):

    robot_name = f"Robot{i + 1}"
    robot = Robot(robot_name)
    print("\n")
    robot.salute()


    if robot.i_need_a_doctor():
        robo_doc.heal(robot)
    
    robots[robot.name] = robot.health_lvl

print("\nRobots and their Health Levels:\n")

for name, health_lvl in robots.items():

    print(f"{name}: {health_lvl}", sep='\n')
