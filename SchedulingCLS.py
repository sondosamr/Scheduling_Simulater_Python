from abc import ABC,abstractmethod

class Scheduling(ABC):


    def __init__(self):
        self.gantt = []
        self.TT = {}
        self.WT = {}
        self.RT = {}
        self.start_t = {}
        self.end_t = {}
        self.t = 0
        self.idle_t = 0
        self.Proportionality = {}
        self.state ={}
        self.ready_queue =[]
        self.process_list = []

    @abstractmethod
    def run(self):
        pass


    def finish(self ):
        self.t+= self.process[2]
        self.end_t[self.process[0]] = self.t
        for p in self.ready_queue:
           self.WT[p[0]] +=self.process[2]
        self.TT[self.process[0]] = self.t - self.process[1]
        #setting Waiting time
        self.WT[self.process[0]] = self.TT[self.process[0]] - self.burst_time[self.process[0]]
        #setting the Proportionality
        self.Proportionality[self.process[0]] = self.TT[self.process[0]] / self.burst_time[self.process[0]]
        #📌Congratolation ,proc Succeed
        self.state[self.process[0]] = "Succed"
        self.c-= 1


    def unFinish(self,rem):
        self.process[2] -= (rem)
        self.t+=rem
        for p in self.ready_queue:
            self.WT[p[0]] +=rem


    def to_String(self):
        print("order of executing the tasks: ", self.gantt)
        print("The total cpu time:", self.t)

        # getting Turnaround time
        print("The turnaround time of each process is: ", self.TT)
        print("The average of turnaround time:", self.avr_TT)

        # getting Waiting time
        print("The waiting time of each process is: ", self.WT)
        print("The average of waiting time:", self.avr_WT)

        # getting Response time
        print("The response time of each process is: ", self.RT)
        print("The average of response time:", self.avr_RT)

        # getting the Throughput
        print("The throughput: ", self.thro, " per unit")

        # getting the cpu utilaization
        print("the cpu utilaization:", self.uti, " %")

        # getting the Proportionality
        print("The Proportionality: ", self.Proportionality)

        # 📌getting the States
        print("the States:", self.state)

    def fit(self, process_list):
        process_list = sorted(process_list,key= lambda x:x[1])

        self.process_list = process_list
        self.c = len(self.process_list)
        self.num_pro = len(self.process_list)
        self.burst_time = {}
        self.arrivalTime =[]
        for p in self.process_list:
            self.arrivalTime.append(p[1])
            self.burst_time[p[0]] = p[2]
            self.WT[p[0]] = 0
            self.state[p[0]] = "False"


    def readyQueue(self):
        i = 0
        while(i<len(self.process_list)):
            if self.process_list[i][1]<=self.t:
                self.ready_queue.append(self.process_list[i].copy())
                self.process_list.remove(self.process_list[i])
            else:
                i+=1

        if self.ready_queue == [] :
            self.gantt.append("idle")
            self.idle_t += 1
            self.t += 1

    def coming_after(self , rem):
        i =0
        while(i<len(self.arrivalTime)):
            if (self.arrivalTime[i] >= self.t) & ((rem + self.t) > self.arrivalTime[i]):
                re =self.arrivalTime[i] - self.t
                self.arrivalTime.remove(self.arrivalTime[i])
                if re >0 :
                    return re
                else:
                   continue
            else:
                i+=1
        return 0

    def calc(self):
        self.avr_TT = round((sum(self.TT.values()) / len(self.TT.values())) , 3)

        self.avr_WT = round((sum(self.WT.values()) / len(self.WT.values())) , 3)

        self.avr_RT = round((sum(self.RT.values()) / len(self.RT.values())) , 3)

        self.thro = round((self.num_pro / self.t) , 3)

        self.uti = round((((self.t - self.idle_t) / self.t) * 100) , 3)

        self.prop = round((sum(self.TT.values())/sum(self.burst_time.values())) , 3)
