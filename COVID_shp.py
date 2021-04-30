#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 21:19:22 2021

@author: brianrosenthal
"""

import pandas as pd
import geopandas as gpd

class pile(dict):
    '''
    Creating dictionary object for COVID-19 cases and deaths.
    Can use object accessors for a dictionary
    Uses Object.key vs Object["key"]
    '''
    def __getattr__(self, attr):
        return self[attr]
    
    def __setattr__(self, attr, val):
        self[attr]=val
        
    def __getstate__(self):
        return self
    
    def __setstate__(self, state):
        self = state

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
        
def daily(df, scol):
    '''
    Converts cummulative data into daily data
    
    Parameters
    ----------
    takes a (Geo)Pandas (Geo)DataFrame
    df : DataFrame

    Returns
    -------
    odf : GeoDataFrame
    
    Used for the COVID dataset, will need to be manipulated if using
    another dataset.
    '''
    cols = df.columns
    odf = gpd.GeoDataFrame()
    for c in range(scol, len(cols)):
        odf.insert(c-scol, cols[c], df.iloc[:,c] - df.iloc[:,c-1])
    odf[odf < 0] = 0
    for c in range(scol):
        odf.insert(c, cols[c], df.iloc[:,c])
    return odf



cov_case = ["COVID_DEATH_CUM", "COVID_CASE_DAY"]
COVID_DEATHS = pd.read_csv("COVID_DEATH_CUM.csv")
COVID_CASES = pd.read_csv("COVID_CASE_DAY.csv")
MN_COUNTY = gpd.read_file("MN_COUNTY/COUNTY_BOUNDARIES_IN_MINNESOTA.shp")

#printCols(MN_COUNTY)

case = pile()
for c in cov_case:
    case.inp = pd.read_csv(f"{c}.csv")
    if c == "COVID_CASE_DAY":
        case.inp = daily(case.inp, 12)
        case.inp.to_csv(f"{c}_daily.csv")
    cols = case.inp.columns
    for col in cols[12:]:
        case.inp[col] = case.inp[col]/case.inp["TOT_POP"]
    #printCols(dat)
    #print("new line")
    case.shp = pd.merge(MN_COUNTY, case.inp, how="left", on="COUNTY_NAM")
    case.shp.to_file(f"{c}/{c}.shp")
    
    
    