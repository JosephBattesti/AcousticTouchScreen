#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 21:29:36 2020

@author: josephbattesti
"""

import Utils as Utils
import mic
import numpy as np
import matplotlib.pyplot as plt

"impulse response "
IRnum=3
IRList=[]

for i in range(IRnum):
    "mic.record() est declanchée et desactivée en fonction d'un treshold"
    print("Waiting for impulse number "+str(i+1))
    SampleFreq,Data = mic.record();
    print("Impulse number "+str(i+1)+" recorded")
    "On converti a une numpy Array"
    Data=np.array(Data)
    "Normalisation"
    Data=Data/max(Data)
    "Ajout a la List"
    IRList.append(Data)
    
"Plot random IR"
plt.plot(IRList[1])