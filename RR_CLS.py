from SchedulingCLS import Scheduling
class RR(Scheduling):

    def __init__(self, quantam):
        Scheduling.__init__(self)
        self.quantam = quantam
    def run(self):
        while (self.c):
            self.readyQueue()
            if self.ready_queue == []:
                continue

            self.process = self.ready_queue.pop(0)
            self.gantt.append(self.process[0])

            # setting the Start Time
            if self.process[0] not in self.start_t:
                self.start_t[self.process[0]] = self.t

            # setting the Response Time
            if self.process[0] not in self.RT:
                self.RT[self.process[0]] = self.t - self.process[1]

            self.rem_bt = self.process[2]
            if self.rem_bt <=self.quantam:
                self.finish()
            else:
                #if any one come when this quantum
                coming = self.coming_after(self.quantam)
                self.unFinish(self.quantam)
                if coming>0:
                    self.readyQueue()
                self.ready_queue.append(self.process)
        self.calc()

