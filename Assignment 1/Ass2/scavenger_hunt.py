import matplotlib.pyplot as plt
import numpy as np

def read_waveforms(LA, RV, RA) :
    infile = open('waveforms.csv', 'r')

    line = infile.readline()
    wf = 0 # which waveform are we trying to read (0 = LA, 1 = RV, 2 = RA)

    while line :
        line = line.strip()
        data = line.split(',')

        for i in range(0, len(data)) : 
            data[i] = float(data[i])

        if(wf == 0) :
            LA.append(data)
        elif(wf == 1) :
            RV.append(data)
        elif(wf == 2) :
            RA.append(data)
        
        wf = (wf + 1) % 3
        line = infile.readline()

    infile.close()

def read_times(TL, TR) :
    infile = open('times.csv', 'r')
    line = infile.readline()
    data = line.strip().split(',')

    for i in range(0, len(data)) : 
        data[i] = float(data[i]) * 1000

    TL.append(data)

    line = infile.readline()
    data = line.strip().split(',')

    for i in range(0, len(data)) : 
        data[i] = float(data[i]) * 1000

    TR.append(data)
    infile.close()

def plot_waveforms(LA, RV, RA, TL, TR) :
    print ('create your individual waveform plots here')
    num_instances = LA.shape[0]
    for i in range(0, num_instances) :
        plt.subplot( 311 )
   #<plot commands for linear acceleration waveform>
        plt.plot(TL, LA[i, :])
        plt.title('Waveforms for Instance' + str(i+1))
        plt.xlabel('Time (ms)')
        plt.ylabel('Linear Accel (g)')
        plt.xticks(np.arange(0, 55, step = 5))
        plt.yticks(np.arange(0, 40, step = 5))

        
        plt.subplot( 312 )
    #<plot commands for rotational velocity waveform>
        plt.plot(TR, RV[i,:])
        plt.xlabel('Time (ms)')
        plt.ylabel('Rot Vel (rad/sec)')
        plt.xticks(np.arange(0, 55, step = 5))
        plt.yticks(np.arange(0, 45, step = 5))

        plt.subplot( 313 )
    #<plot command for rotational acceleration waveform>
        plt.plot(TR, RA[i,:])
        plt.xlabel('Time (ms)')
        plt.ylabel('Rot Accel (rad/sec^2)')
        plt.xticks(np.arange(0, 55, step = 5))
        plt.yticks(np.arange(0, 16, step = 2))
        plt.savefig('Instance intitial ' + str(i + 1) + '.png')
        plt.close()


    
# make empty data and time Lists
LA_list = []
RV_list = []
RA_list = []
TL_list = []
TR_list = []

##mla_list = []
##ala_list = []
##pla_list = []

read_waveforms(LA_list, RV_list, RA_list)
read_times(TL_list, TR_list)

def plot_nine(LA, RV, RA):
    num_instances = LA.shape[0]
    mla_list = []
    ala_list = []
    pla_list = []
    mrv_list = []
    arv_list = []
    prv_list = []
    mra_list = []
    ara_list = []
    pra_list = []

    LA = np.array(LA_list)
    RV = np.array(RV_list)
    RA = np.array(RA_list)
    for i in range(0, num_instances):
        mla_list.append(np.min(LA[i, :]))
    for i in range(0, num_instances):
        ala_list.append(np.mean(LA[i, :]))
    for i in range (0, num_instances):
        pla_list.append(np.max(LA[i, :]))
    for i in range(0, num_instances):
        mrv_list.append(np.min(RV[i, :]))
    for i in range(0, num_instances):
        arv_list.append(np.mean(RV[i, :]))
    for i in range (0, num_instances):
        prv_list.append(np.max(RV[i, :]))
    for i in range(0, num_instances):
        mra_list.append(np.min(RA[i, :]))
    for i in range(0, num_instances):
        ara_list.append(np.mean(RA[i, :]))
    for i in range (0, num_instances):
        pra_list.append(np.max(RA[i, :]))
##        mla_list.append(np.max(LA[i, :]))
##        mla_list.append(np.mean(LA[i,:]))
        
    MLA = np.array(mla_list)
    ALA = np.array(ala_list)
    PLA = np.array(pla_list)
    MRV = np.array(mrv_list)
    ARV = np.array(arv_list)
    PRV = np.array(prv_list)
    MRA = np.array(mra_list)
    ARA = np.array(ara_list)
    PRA = np.array(pra_list)
##    ALA = np.array(ala_list)
##    PLA = np.array(pla_list)
    print ('MLA :  Min = ' + str(np.min(MLA)) + ' , Max = ' + str(np.max(MLA) )+ ' , Avg = '+ str(np.mean(MLA)))
    print ('ALA : Min = ' + str(np.min(ALA)) + ' , Max = ' + str(np.max(ALA) )+ ' , Avg = '+ str(np.mean(ALA)))
    print ('PLA : Min = ' + str(np.min(PLA)) + ' , Max = ' + str(np.max(PLA) )+ ' , Avg = '+ str(np.mean(PLA)))
    print  ()
    print ('MRV: Min = ' + str(np.min(MRV)) + ' , Max = ' + str(np.max(MRV) )+ ' , Avg = '+ str(np.mean(MRV)))
    print ('ARV : Min = ' + str(np.min(ARV)) + ' , Max = ' + str(np.max(ARV) )+ ' , Avg = '+ str(np.mean(ARV)))
    print ('PRV : Min = ' + str(np.min(PRV)) + ' , Max = ' + str(np.max(PRV) )+ ' , Avg = '+ str(np.mean(PRV)))
    print ()
    print ('MRA : Min = ' + str(np.min(MRA)) + ' , Max = ' + str(np.max(MRA) )+ ' , Avg = '+ str(np.mean(MRA)))
    print ('ARA : Min = ' + str(np.min(ARA)) + ' , Max = ' + str(np.max(ARA) )+ ' , Avg = '+ str(np.mean(ARA)))
    print ('PRA : Min = ' + str(np.min(PRA)) + ' , Max = ' + str(np.max(PRA) )+ ' , Avg = '+ str(np.mean(PRA)))
##    plt.subplot( 331 )
    #<plot command for rotational acceleration waveform>
##    plt.plot(list(range(0, num_instances)), ARA)
##    plt.xlabel('Instances')
##    plt.ylabel('Rot Accel (rad/sec^2)')
##    plt.xticks(np.arange(0, 70, step = 5))
##    plt.yticks(np.arange(0, 5, step = 0.5))
##    plt.subplot(332)
##    plt.plot(list(range(0, num_instances)), ALA)
##    plt.xlabel('Instances')
##    plt.ylabel('Rot Accel (rad/sec^2)')
##    plt.xticks(np.arange(0, 70, step = 5))
##    plt.yticks(np.arange(0, 5, step = 0.5))
##    plt.subplot(333)
##    plt.plot(list(range(0, num_instances)), PLA)
##    plt.xlabel('Time (ms)')
##    plt.ylabel('Rot Accel (rad/sec^2)')
##    plt.xticks(np.arange(0, 70, step = 5))
##    plt.yticks(np.arange(0, 5, step = 0.5))
##    plt.subplot(334)
##    plt.plot(list(range(0, num_instances)), MRV)
##    plt.xlabel('Time (ms)')
##    plt.ylabel('Rot Accel (rad/sec^2)')
##    plt.xticks(np.arange(0, 70, step = 5))
##    plt.yticks(np.arange(0, 5, step = 0.5))
##    plt.show()
    plt.scatter(PLA,PRV, color='black', label='PLA v PRV', marker='*')
##    plt.scatter(list(range(0, num_instances)), PRV, color='red', label='Versicolor', marker='+')
    ##plt.scatter(virginica_arr[:, 2], virginica_arr[:, 3], color='blue', label='Virginica', marker='o')
    plt.legend(loc='upper left')
    plt.ylabel('PLA')
    plt.xlabel('PRA')
    plt.title('Plot of PLA, PRV')
##    plt.xlim(0,65)
##    plt.ylim(0,100)
    plt.show()
    
##    plt.savefig('Instance intitialb euhfeufh.png')
##    plt.close()
 #   print ('Min = ' + np.min(MLA))

# convert all data and time lists to numpy arrays for plotting
LA = np.array(LA_list)
RV = np.array(RV_list)
RA = np.array(RA_list)
TL = np.array(TL_list[0])
TR = np.array(TR_list[0])
##ara_list = []
##ARA = np.array(ara_list)
plot_nine(LA, RV, RA)
##plot_waveforms(LA, RV, RA, TL, TR)
##plt.plot(TL, LA[6, :])
##plt.title('Linear Acceleration of Instance 7')
##plt.xlabel('Time (ms)')
##plt.ylabel('Lin Accel (g)')
##plt.xticks(np.arange(0, 55, step=5))
##plt.savefig('Instance 7.png')
##plt.close()

##print(TL)
##print(TR)
##print(np.mean(LA[2,:]))
