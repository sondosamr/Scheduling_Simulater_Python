from prettytable  import PrettyTable


def read(inpFile, lst):
    with open(inpFile, "r") as inp:
        data = inp.readlines()
    for line in data:
        w = line.split()
        lst.append(w)
    lst.remove(lst[0])
    for p in lst:
        for i,e in enumerate(p):
            try:
                p[i] = int(e)
            except:
                continue


def output (fcfs,rr,sjf,srf,edf):

    fcfs_table = PrettyTable(["Task","Start Time","End Time","Duration","Status"])
    for T in fcfs.burst_time.keys():
        fcfs_table.add_row([T,fcfs.start_t[T],fcfs.end_t[T],fcfs.TT[T],fcfs.state[T]])
    fcfs_table.vrules = 2

    rr_table = PrettyTable(["Task","Start Time","End Time","Duration","Status"])
    for T in rr.burst_time.keys():
        rr_table.add_row([T,rr.start_t[T], rr.end_t[T] ,rr.TT[T],rr.state[T]])
    rr_table.vrules = 2

    sjf_table = PrettyTable(["Task","Start Time","End Time","Duration","Status"])
    for T in sjf.burst_time.keys():
        sjf_table.add_row([T,sjf.start_t[T],sjf.end_t[T],sjf.TT[T],sjf.state[T]])
    sjf_table.vrules = 2

    srf_table = PrettyTable(["Task","Start Time","End Time","Duration","Status"])
    for T in srf.burst_time.keys():
        srf_table.add_row([T,srf.start_t[T],srf.end_t[T],srf.TT[T],srf.state[T]])
    srf_table.vrules = 2

    edf_table = PrettyTable(["Task","Start Time","End Time","Duration","Status"])
    for T in edf.burst_time.keys():
        edf_table.add_row([T,edf.start_t[T],edf.end_t[T],edf.TT[T],edf.state[T]])
    edf_table.vrules = 2

    with open("output.txt","w") as file:
        file.write("AWT               FCFS({}) \t  RR({}) \t  SJF({}) \t  SRTF({}) \t  EDF({})\n".format(fcfs.avr_WT ,rr.avr_WT,sjf.avr_WT,srf.avr_WT,edf.avr_WT))
        file.write("ART               FCFS({}) \t  RR({}) \t  SJF({}) \t  SRTF({}) \t  EDF({})\n".format(fcfs.avr_RT ,rr.avr_RT,sjf.avr_RT,srf.avr_RT,edf.avr_RT))
        file.write("ATT               FCFS({}) \t  RR({}) \t  SJF({}) \t  SRTF({}) \t  EDF({})\n".format(fcfs.avr_TT ,rr.avr_TT,sjf.avr_TT,srf.avr_TT,edf.avr_TT))
        file.write("Throughput        FCFS({}) \t  RR({}) \t  SJF({}) \t  SRTF({}) \t  EDF({})\n".format(fcfs.thro ,rr.thro,sjf.thro,srf.thro,edf.thro))
        file.write("Utilizationuti    FCFS({}) \t  RR({}) \t  SJF({}) \t  SRTF({}) \t  EDF({})\n".format(fcfs.uti ,rr.uti,sjf.uti,srf.uti,edf.uti))
        file.write("Proportionality   FCFS({}) \t  RR({}) \t  SJF({}) \t  SRTF({}) \t  EDF({})\n \n".format(fcfs.prop ,rr.prop,sjf.prop,srf.prop,edf.prop))
        file.write("="*100 +"\n" +"\n")
        file.write("Policy: FCFS"+"\n")
        file.write(fcfs_table.get_string()+"\n"+"\n")
        file.write("Policy: RR"+"\n")
        file.write(rr_table.get_string()+"\n"+"\n")
        file.write("Policy: SJF" + "\n")
        file.write(sjf_table.get_string() + "\n"+"\n")
        file.write("Policy: SRF" + "\n")
        file.write(srf_table.get_string() + "\n"+"\n")
        file.write("Policy: EDF" + "\n")
        file.write(edf_table.get_string() + "\n"+"\n")

