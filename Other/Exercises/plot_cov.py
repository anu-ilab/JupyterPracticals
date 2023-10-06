#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 12:43:57 2020

@author: malcolm
"""


# ----------------------------------------------------------------------------
# Calculate covariance matrix from error distribution for each pair of solution parameters
# ----------------------------------------------------------------------------
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import plot_cov_ellipse

def plot_error_ellipses(mls,Cm):
    CmProj01 = Cm[np.ix_([0,1],[0,1])]
    CmProj02 = Cm[np.ix_([0,2],[0,2])]
    CmProj12 = Cm[np.ix_([1,2],[1,2])]

    sig_param1 = np.sqrt(Cm[0,0]) # standard error for parameter 1
    sig_param2 = np.sqrt(Cm[1,1]) # standard error for parameter 2
    sig_param3 = np.sqrt(Cm[2,2]) # standard error for parameter 3

    l68 = np.sqrt(stats.chi2.ppf(q=0.68,df=2)) # number of standard deviations equivalent to 68% confidence ellipse
    l95 = np.sqrt(stats.chi2.ppf(q=0.95,df=2)) # number of standard deviations equivalent to 95% confidence ellipse

    fig = plt.figure(figsize=(9,6))
    fig.suptitle("Error ellipses for solution", fontsize=16)

    ax1 = plt.subplot("221")
    plot_cov_ellipse(CmProj01,mls[0:2], ax=ax1,nstd=l68,color='Blue',alpha=0.4,label="68% Confidence")
    plot_cov_ellipse(CmProj01,mls[0:2], ax=ax1,nstd=l95,color='Green',alpha=0.4,label="95% Confidence")
    ax1.set_xlim(mls[0]-1.3*1.96*sig_param1,mls[0]+1.3*1.96*sig_param1)
    ax1.set_ylim(mls[1]-1.3*1.96*sig_param2,mls[1]+1.3*1.96*sig_param2)
    ax1.set_xlabel('m1')
    ax1.set_ylabel('m2')

    ax2 = plt.subplot("222")
    plot_cov_ellipse(CmProj12,mls[1:], ax=ax2,nstd=l68,color='Blue',alpha=0.4,label='68% Confidence')
    plot_cov_ellipse(CmProj12,mls[1:], ax=ax2,nstd=l95,color='Green',alpha=0.4,label='95% Confidence')
    ax2.set_xlim(mls[1]-1.3*1.96*sig_param2,mls[1]+1.3*1.96*sig_param2)
    ax2.set_ylim(mls[2]-1.3*1.96*sig_param3,mls[2]+1.3*1.96*sig_param3)
    ax2.set_xlabel('m2')
    ax2.set_ylabel('m3')

    ax3 = plt.subplot("223")
    plot_cov_ellipse(CmProj02,[mls[0],mls[2]], ax=ax3,nstd=l68,color='Blue',alpha=0.4,label='68% Confidence')
    plot_cov_ellipse(CmProj02,[mls[0],mls[2]], ax=ax3,nstd=l95,color='Green',alpha=0.4,label='95% Confidence')
    ax3.set_xlim(mls[0]-1.3*1.96*sig_param1,mls[0]+1.3*1.96*sig_param1)
    ax3.set_ylim(mls[2]-1.3*1.96*sig_param3,mls[2]+1.3*1.96*sig_param3)
    ax3.set_xlabel('m1')
    ax3.set_ylabel('m3')

    plt.show()