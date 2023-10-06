#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 12:56:19 2020

@author: malcolm
"""


import matplotlib.pyplot as plt
import numpy as np

##########################
# Random draws of feasible solutions
##########################

def plot_feasible(mls,Cm,size=500):
    fig = plt.figure(figsize=(9,6))
    fig.suptitle("Random draws of feasible solutions", fontsize=20)

    sig_param1 = np.sqrt(Cm[0,0]) # standard error for parameter 1
    sig_param2 = np.sqrt(Cm[1,1]) # standard error for parameter 2
    sig_param3 = np.sqrt(Cm[2,2]) # standard error for parameter 3

    points = np.random.multivariate_normal(mean=mls, cov=Cm, size=size)

    ax1 = plt.subplot("221")
    xp, yp = points.T[0], points.T[1]
    ax1.plot(xp, yp, 'k+')
    ax1.plot(mls[0],mls[1], 'ro')
    ax1.set_xlim(mls[0]-1.3*1.96*sig_param1,mls[0]+1.3*1.96*sig_param1)
    ax1.set_ylim(mls[1]-1.3*1.96*sig_param2,mls[1]+1.3*1.96*sig_param2)
    ax1.set_xlabel('m1')
    ax1.set_ylabel('m2')

    ax2 = plt.subplot("222")
    xp, yp =  points.T[1], points.T[2]
    ax2.plot(xp, yp, 'k+')
    ax2.plot(mls[1],mls[2], 'ro')
    ax2.set_xlim(mls[1]-1.3*1.96*sig_param2,mls[1]+1.3*1.96*sig_param2)
    ax2.set_ylim(mls[2]-1.3*1.96*sig_param3,mls[2]+1.3*1.96*sig_param3)
    ax2.set_xlabel('m2')
    ax2.set_ylabel('m3')

    ax3 = plt.subplot("223")
    xp, yp =  points.T[0], points.T[2]
    ax3.plot(xp, yp, 'k+')
    ax3.plot(mls[0],mls[2], 'ro')
    ax3.set_xlim(mls[0]-1.3*1.96*sig_param1,mls[0]+1.3*1.96*sig_param1)
    ax3.set_ylim(mls[2]-1.3*1.96*sig_param3,mls[2]+1.3*1.96*sig_param3)
    ax3.set_xlabel('m1')
    ax3.set_ylabel('m3')

    plt.show()
