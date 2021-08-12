from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.bots = []
        self.bot_1 = Robot('Demolisher', 40, Weapon('Missile Launcher', 50))
        self.bot_2 = Robot('Terminator', 30, Weapon('Akimbo Tommy Guns', 60))
        self.bot_3 = Robot('Smasher', 40, Weapon('Sniper', 45))

    # def add_bots(self):
