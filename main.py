from FCFS_CLS import*
from EDF_CLS import*
from SRF_CLS import*
from SJF_CLS import*
from RR_CLS import*
from backEND import*

processes_list = [["A", 0, 5, 20],
                  ["B", 3, 10, 30],
                  ["c", 4, 12, 40]]

test_1 = [["p1",0,20,25],
          ["p2",25,25,75],
          ["p3",30,25,60],
          ["p4",60,15,80],
          ["p5", 100, 10, 110],
          ["p6", 105, 10, 115]]


while True :
    file_path =input("Enter file path please:")
    q = int(input("enter Quantum value pleas:"))

    fcfs = FCFS()
    rr = RR(q)
    sjf = SJF()
    srf = SRF()
    edf = EDF()

    pros = []
    read(file_path,pros)
    try:
        for line in pros:
            if len(line) < 4:
                raise Exception("un valid input in process:")
    except:
        print("un valid input in processes , please check your file")
        continue


    print(pros)

    # print(pros)
    fcfs.fit(pros)
    fcfs.run()



    rr.fit(pros)
    rr.run()

    sjf.fit(pros)
    sjf.run()

    srf.fit(pros)
    srf.run()



    edf.fit(pros)
    edf.run()


    output(fcfs,rr,sjf,srf,edf)
    print("Result File is complete in ' output.txt ' ")

    for i in [fcfs,rr,sjf,srf,edf]:
        i.to_String()