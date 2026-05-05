from timer import Timer

class Orchestrator():
    def __init__(self):
        self.timers = []
        self.current_timer = 0
        self.on = False

    def add_timer(self, time, name):
        timer = Timer(time , name)
        self.timers.append(timer)


    def countdown(self):
        if self.on:
            self.timers[self.current_timer].count_down()
        else:
            pass

    def reset_timer(self):
        self.timers[self.current_timer].delta = self.timers[self.current_timer].time