import numpy as np
import os

"""
the x axis (T) is not identical for the standard
and the measured diffraction spectra. for this reason
"compare" below has to be resampled to be on the same
x scale. i assume sampling rate is high enough to just
take the nearest value.
also, function is squared because for correlation in 
our case the peaks should be enhanced and the bg noise
dimished.
"""


def resample(sample, newX):
    resampled = []
    oldX = sample[:,0]
    for x in newX:
        idx = np.searchsorted(oldX, x, side="right")
        if idx == 0:
            resampled.append(sample[0,1])
        else:
            resampled.append(sample[idx-1,1]) 
    return resampled

if __name__ == '__main__':
    standard = np.genfromtxt("standard.ASC")
    standardnorm = standard[:,1]/np.max(standard[:,1])
    standardnorm = np.power(standardnorm,2)
    for file in os.listdir("spectra"):
        if file.endswith(".ASC"):
            compare = np.genfromtxt(os.path.join("spectra", file))
            resampledcompare = resample(compare,standard[:,0])
            comparenorm = resampledcompare/np.max(compare[:,1])
            comparenorm = np.power(comparenorm,2)
            corr = np.correlate(standardnorm, comparenorm)
            integrated = np.sum(corr)
            integrated=integrated/np.sum(np.correlate(standardnorm,standardnorm))
            print("{}: CC integration {}%".format(file,round(100*integrated,4)))
