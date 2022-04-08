# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 16:46:21 2021

@author: Dimitris Giannopoulos, Seismotech S.A.

Python version: 3.8.8
Obspy version: 1.2.2
"""

# Remove instrument response using the information from the given poles and zeros (paz), gain and sensitivity

#### Load all necessary modules ####

from obspy.core import read
import sys
import numpy as np
import warnings
#warnings.filterwarnings("ignore")          # Uncomment this line for allowing possible \
                                            # important warnings being displayed in the terminal



#### Read data and header information ####

st=read(str(sys.argv[1]))                   # Read Stream object
filename=str(sys.argv[1])
st.sort(['starttime'])
st.merge(method=1, fill_value=0)            # Fill possible data gaps with zeros
tr = st[0]                                  # Assign the final and only Trace of the Stream
sr=tr.stats.sampling_rate                   # Get sampling rate info
NyqFreq=sr/2.0
print(tr)



#### Remove mean ####

MeanValue = np.mean(tr.data)
#print(MeanValue)
tr.data=tr.data-MeanValue
#### Remove trend ####
tr.detrend(type="linear")



#### Provide necessary metadata ####

# Integra metadata in paz dictionary format
paz = {'gain': 415.746, \
       'poles': [-9.162234E+01 +6.548740E+01j, -9.162234E+01 -6.548740E+01j, -1.937840E+00 +0+0j], \
       'sensitivity': 6.263707E+08 , \
       'zeros': [0+0j, 0+0j]}


    
#### Apply instrument response correction ##### 

pre_filt = (0.5, 1, NyqFreq*0.90, NyqFreq*0.95)

tr.simulate(paz_remove=paz, remove_sensitivity=True, paz_simulate=None, 
            pre_filt=pre_filt, zero_mean=True, taper=False)



#### Write output ##### 
outsta=filename + 'corr'
tr.write(outsta, format='MSEED')