from SchedulingCLS import Scheduling

class EDF(Scheduling):
    def __init__(self):
        super().__init__()

    def dead(self,rem):
        if self.process[0] not in self.start_t:
            self.start_t[self.process[0]] = self.t

        # setting the Response Time
        if self.process[0] not in self.RT:
            self.RT[self.process[0]] = self.t - self.process[1]


        self.t+= rem
        self.end_t[self.process[0]] = self.t
        for p in self.ready_queue:
            self.WT[p[0]] +=rem
        #setting the Turnaround Time
        self.TT[self.process[0]] = self.t - self.process[1]
        #setting Proportionality
        self.Proportionality[self.process[0]]=0
        self.c-=1


    def run(self):
        while(self.c):
            self.readyQueue()
            if self.ready_queue ==[] :
                continue

            self.ready_queue = sorted(self.ready_queue, key=lambda x: x[3])
            self.process = self.ready_queue[0]
            self.gantt.append(self.process[0])
            self.ready_queue.remove(self.process)
            #📌if deadline over , just  off
            if self.t>= self.process[3]:
                self.dead(self.t-self.process[3])
                continue
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
            #📌If deadline will over before brust , off too
            if ((self.t+self.process[2])>self.process[3]):
                rem= self.process[3]-self.t
                self.unFinish(rem)
                self.ready_queue.append(self.process)
                continue
            self.finish()

        self.calc()

