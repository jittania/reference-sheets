class Adult:
    def make_phone_call(self):
        print("I'm picking up the phone and dialing a number and using my voice!")

class Texter(Adult):
    def make_phone_call(self):
        print("I'm waiting four days")
        print("Now I'll forget to call them back")
        print("Now I'm just texting them instead")
    def make_emergency_phone_call(self):
        super().make_phone_call()

terry = Texter()
terry.make_phone_call()
terry.make_emergency_phone_call()