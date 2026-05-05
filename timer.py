import time
from datetime import datetime as dt, timedelta
class Timer():
    def __init__(self, timer: tuple, name: str):
        self.time = timedelta(hours=timer[0], minutes=timer[1], seconds=timer[2])
        self.delta = self.time
        self.done = False
        self.name = name

    def count_down(self):
        if self.delta > timedelta(seconds=0):
            self.delta -= timedelta(seconds=1)
        else:
            self.done = True

    def get_time_str(self):
        return str(self.delta)


