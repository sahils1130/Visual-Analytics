import matplotlib.pyplot as plt
import numpy as np


def read_waveforms(LA, RV, RA):
    infile = open('waveforms.csv', 'r')

    line = infile.readline()
    wf = 0  # which waveform are we trying to read (0 = LA, 1 = RV, 2 = RA)

    while line:
        line = line.strip()
        data = line.split(',')

        for i in range(0, len(data)):
            data[i] = float(data[i])

            if (wf == 0):
                LA.append(data)
            elif (wf == 1):
                RV.append(data)
            elif (wf == 2):
                RA.append(data)

            wf = (wf + 1) % 3
            # print(wf)
            line = infile.readline()

    infile.close()


def read_times(TL, TR):
    infile = open('times.csv', 'r')
    line = infile.readline()
    data = line.strip().split(',')

    for i in range(0, len(data)):
        data[i] = float(data[i]) * 1000

    TL.append(data)

    line = infile.readline()
    data = line.strip().split(',')

    for i in range(0, len(data)):
        data[i] = float(data[i]) * 1000

    TR.append(data)
    infile.close()



def plot_waveforms(LA, RV, RA, TL, TR):
   # LA = 0
    num_instances=LA.shape[0]
   # print('create your individual waveform plots here')
    for i in range(0, num_instances):
        plt.subplot(311)
        plt.plot(TL, LA[i, :])
        plt.title('Waveforms for Instance ' + str(i+1))
        plt.xlabel('Time (ms)')
        plt.ylabel('Lin Accel (g)')
        plt.xticks(np.arange(0, 55, step=5))
        plt.yticks(np.arange(0, 40, step=5))

        plt.subplot(312)
        plt.plot(TR, RV[i, :])
        plt.xlabel('Time (ms)')
        plt.ylabel('Rot Vel (rad/sec)')
        plt.xticks(np.arange(0, 55, step=5))
        plt.yticks(np.arange(0, 45, step=5))

        plt.subplot(313)
        plt.plot(TR, RA[i, :])
        plt.xlabel('Time (ms)')
        plt.ylabel('Rot Accel (rad/sec^2)')
        plt.xticks(np.arange(0, 55, step=5))
        plt.yticks(np.arange(0, 16, step=2))

      #  plt.savefig('Instance ' + str(i + 1) + '.png')
     ##   plt.close()
    plt.savefig('Instancehjshxdjschx.png')
    plt.close()

# make empty data and time Lists
LA_list = []
RV_list = []
RA_list = []
TL_list = []
TR_list = []

def plot_many(LA, RV, RA):
    mla_list=[]
    LA_list = []
    LA = np.array(LA_list)
    num_instances=LA.shape[0]
    for i in range(0,num_instances):
        mla_list.append(np.min(LA[i, :]))
    MLA=np.array(mla_list)
    print(np.min(MLA))



read_waveforms(LA_list, RV_list, RA_list)
read_times(TL_list, TR_list)
#plot_waveforms(LA, RV, RA, TL, TR)

# convert all data and time lists to numpy arrays for plotting
LA = np.array(LA_list)
RV = np.array(RV_list)
RA = np.array(RA_list)
TL = np.array(TL_list[0])
TR = np.array(TR_list[0])
# MLA = np.array(MLA_list)
plot_many(LA, RV, RA)

# plot_waveforms(LA, RV, RA, TL, TR)
# print(MLA)
#print("Hello")
# print(LA)
#print()
#print(TR)
#print(np.mean(LA))
