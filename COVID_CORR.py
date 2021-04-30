#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 22:58:08 2021

@author: brianrosenthal
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def printCols(df):
    '''
    Prints the column index, column name, and column type
    
    Parameters
    ----------
    takes a (Geo)Pandas (Geo)DataFrame
    df : DataFrame

    Returns
    -------
    None.
    
    Used to print all columns and their types for debuging and testing.
    '''
    print(f"type: {type(df)}")
    for count, col in enumerate(df.columns):
        print(f"iloc: {count} name: {col} dtype: {df[col].dtypes}")
    
DEM_df = pd.read_csv("DEM_COVID.csv")
DEM_CLEAN_df = DEM_df.loc[:, "TOT_POP_1":"COVID_DEATH"]
DEM_NORM = DEM_CLEAN_df.apply(lambda x: x/DEM_CLEAN_df["TOT_POP_1"])
DEM_corr = DEM_NORM.corr(method="pearson")
DEM_corr.to_csv("corr_matrix.csv")

    
    
    
    
    
    
    
    
    
    
    
    
    
