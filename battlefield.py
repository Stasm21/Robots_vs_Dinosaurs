from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()

    def run(self):
        self.welcome()

    def welcome(self):
        print('Are you ready!!!!!!!!')
