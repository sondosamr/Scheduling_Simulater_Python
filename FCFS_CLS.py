from SchedulingCLS import Scheduling

class FCFS(Scheduling):

    def __init__(self):
        Scheduling.__init__(self)

    def run(self):
        while(self.c):
            self.readyQueue()
            if self.ready_queue ==[] :
                continue
            self.process = self.ready_queue.pop(0)
            self.gantt.append(self.process[0])

            #setting the Start Time
            if self.process[0] not in self.start_t:
                self.start_t[self.process[0]] = self.t

            #setting the Response Time
            if self.process[0] not in self.RT:
                self.RT[self.process[0]] = self.t - self.process[1]

            self.finish()
        self.calc()

