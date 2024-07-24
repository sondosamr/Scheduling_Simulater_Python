from SchedulingCLS import Scheduling

class SRF(Scheduling):





    def run(self):
        while(self.c):
            self.readyQueue()
            if self.ready_queue ==[] :
                continue

            self.ready_queue = sorted(self.ready_queue, key=lambda x: x[2])
            self.process = self.ready_queue[0]
            self.gantt.append(self.process[0])
            self.ready_queue.remove(self.process)

            #setting the Start Time
            if self.process[0] not in self.start_t:
                self.start_t[self.process[0]] = self.t

            #setting the Response Time
            if self.process[0] not in self.RT:
                self.RT[self.process[0]] = self.t - self.process[1]

            #📌If there is any proc hasnt came yet I wanna know when next process come
            if (len(self.ready_queue) + 1) == self.c:
                pass
            else:
                rem = self.coming_after(self.process[2])
                if rem > 0:
                    self.unFinish(rem)
                    self.ready_queue.append(self.process)
                    continue

            self.finish()
        self.calc()


