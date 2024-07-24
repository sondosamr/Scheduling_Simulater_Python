from SchedulingCLS import Scheduling

class SJF(Scheduling):
    def run(self):
        while(self.c):
            self.readyQueue()
            if self.ready_queue == []:
                continue
            self.ready_queue = sorted(self.ready_queue, key=lambda x: x[2])
            self.process = self.ready_queue[0]
            self.gantt.append(self.process[0])
            self.ready_queue.remove(self.process)

            # setting the Start Time
            if self.process[0] not in self.start_t:
                self.start_t[self.process[0]] = self.t

            # setting the Response Time
            if self.process[0] not in self.RT:
                self.RT[self.process[0]] = self.t - self.process[1]

            self.finish()
        self.calc()


