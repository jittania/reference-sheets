# class Adult:
#     def make_phone_call(self):
#         print("I'm picking up the phone and dialing a number and using my voice!")

# class Texter(Adult):
#     def make_phone_call(self):
#         print("I'm waiting four days")
#         print("Now I'll forget to call them back")
#         print("Now I'm just texting them instead")
#     def make_emergency_phone_call(self):
#         super().make_phone_call()

# terry = Texter()
# terry.make_phone_call()
# terry.make_emergency_phone_call()

#=================================================================

# class Automobile:
#     def __init__(self, speed):
#         self.speed = speed

#     def accelerate(self, speed_delta):
#         self.speed += speed_delta
#         return self.speed

# bus = Automobile(45)
# bus.accelerate(5)
# print("The speed of the bus should be 50:", bus.speed)
# bus.accelerate(-2)
# print("The speed of the bus should be 48:", bus.speed)

#=================================================================

class BasketballTeam:
    def __init__(self):
        self.members = [] 

    def add_member(self, name):
        self.members.append(name)
        return True 

green_team = BasketballTeam()
print("Initially, the green_team has no members:", green_team.members)

yellow_team = BasketballTeam()
print("Initially, the yellow_team has no members:", yellow_team.members)

green_team.add_member("Charly")
yellow_team.add_member("Martina")
green_team.add_member("Rahma")
yellow_team.add_member("Lilly-Ann")
green_team.add_member("Gillian")

print("The green_team has the members Charly, Rahma, and Gillian", green_team.members)
print("The yellow_team has the members Martina and Lilly-Ann", yellow_team.members)
