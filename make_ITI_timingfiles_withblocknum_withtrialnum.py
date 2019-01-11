import numpy as np
from scipy.stats import truncexpon
def Mean(lst):
    return sum(lst) / len(lst)
import csv

#shape parameter controls skew
#shape*scale = estimated mean
shape_par = 6
scale_par = .6666666666666666666666666666666666666666667

#these set the acceptable mean range
mean_max = 4.04
mean_min = 3.96

#this is if you want to impose a maximum ITI
#currently this won't do anything
max_ITI = 99

#for range of subnums desired
firstsub = 1003
lastsub = 1030
#for number of sessions desired
sessionNum = 2
#number of blocks
numBlocks = 10
#number of trials per block
numTrials = 46


for i in range(firstsub,lastsub + 1):

    for j in range(1,sessionNum + 1):

        f = open(str(i)+'_'+str(j)+'_timing.csv', 'wb')
        writer = csv.writer(f)
        for k in range(1, numBlocks + 1):

            distmean = 0
            distmax = 0
            mean_good = False
            max_good = False
            makedist = True
            while makedist:
                dist = np.random.gamma(shape = shape_par, scale = scale_par, size = numTrials)
                distmean = Mean(dist)
                if distmean > mean_min and distmean < mean_max:
                    mean_good = True
                else:
                    mean_good = False
                if distmax < max_ITI:
                    max_good = True
                else:
                    max_good = False
                if max_good and mean_good:
                    makedist = False

            m = 1 #trialnum
            for val in dist:
                writer.writerow([val, k, m])
                m = m+1
        
        f.close()
