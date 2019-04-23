#!/usr/bin/env python

"""
This script contains code used by the following jupytr notebooks:

- fitbit.ipynb

Project by Jesse J. Ruiz and Ednalyn C. De Dios.
Codeup, Ada Cohort
"""



# ===========
# ENVIRONMENT
# ===========

import os
import sys

import matplotlib.pyplot as plt
from matplotlib import cm
import seaborn as sns

import pandas as pd
import numpy as np

from env import path


# ===========
# ACQUISITION
# ===========


def get_fitbit(files):
    chunks = []
    for i, element in enumerate(files):
        i = pd.read_csv(path+element, skiprows = 35, nrows=33, engine = 'c', low_memory=False)
        chunks.append(i)
    return chunks


def clean_fitbit(chunks, cols=['Date', 'Calories Burned', 'Steps',
                            'Distance', 'Floors', 'Minutes Sedentary',
                            'Minutes Lightly Active', 'Minutes Fairly Active',
                            'Minutes Very Active', 'Activity Calories']):
    for chunk in chunks:
        chunk.columns = cols
    return chunks



# ===========
# PREPARATION
# ===========


def prepare_fitbit(chunks, num_range, column):
    df = pd.DataFrame()
    data = ([chunks[i] for i in range(num_range)])
    df = df.append(data)
    df = df.dropna(axis=0)
    df.set_index(column, inplace=True)
    return df


# The code below inspired by Michael P. Moran's missing_vals_df().
def missing_values_col(df):
    """
    Write or use a previously written function to return the
    total missing values and the percent missing values by column.
    """
    null_count = df.isnull().sum()
    null_percentage = (null_count / df.shape[0]) * 100
    empty_count = pd.Series(((df == ' ') | (df == '')).sum())
    empty_percentage = (empty_count / df.shape[0]) * 100
    nan_count = pd.Series(((df == 'nan') | (df == 'NaN')).sum())
    nan_percentage = (nan_count / df.shape[0]) * 100
    return pd.DataFrame({'num_missing': null_count, 'missing_percentage': null_percentage,
                         'num_empty': empty_count, 'empty_percentage': empty_percentage,
                         'nan_count': nan_count, 'nan_percentage': nan_percentage})

def convert_to_float(df, *cols):
    """
    takes in a dataframe and a list of columns names and returns the dataframe
    with the datatypes of those columns changed to a non-numeric type
    """
    for col in cols:
        df[col] = df[col].str.replace(',', '')
        df[col] = df[col].str.replace(' ', '')
        df[col] = df[col].astype(float)
    return df





# ===========
# EXPLORATION
# ===========


# The code below adapted from Michael P. Moran's snippet.
def summarize_data(df):
    
    df_head = df.head()
    print(f'HEAD\n{df_head}', end='\n\n')
   
    df_tail = df.tail()
    print(f'TAIL\n{df_tail}', end='\n\n')

    shape_tuple = df.shape
    print(f'SHAPE: {shape_tuple}', end='\n\n')
    
    df_describe = df.describe()
    print(f'DESCRIPTION\n{df_describe}', end='\n\n')
    
    df.info()
    print(f'INFORMATION')    

    print(f'VALUE COUNTS', end='\n\n')
    for col in df.columns:
        n = df[col].unique().shape[0]
        col_bins = min(n, 10)
        print(f'{col}:')
        if df[col].dtype in ['int64', 'float64'] and n > 10:
            print(df[col].value_counts(bins=col_bins, sort=False, dropna=False))
        else:
            print(df[col].value_counts(dropna=False))
        print('\n')


def plot_subs(df, cols):
    """
    Creates subplots of boxplots.
    """
    plt.figure(figsize=(16,20))
    for i, col in enumerate(cols):
        plot_number = i + 1
        plt.subplot(5,3,plot_number)
        plt.title(col)
        sns.boxplot(data=df[col])


def plot_hist(df, num_bins=8):
    """
    Plots the distribution of the dataframe's variables.
    """
    df.hist(figsize=(24, 20), bins=num_bins)
    plt.axes


def plot_heat(df):
    """
    Plots a heatmap of the numerical variables.
    """
    plt.figure(figsize=(12,8))
    sns.heatmap(df.corr(), cmap='RdYlBu', annot=True, center=0)


def convert_to_datetime(df, column):
    """
    Converts string object to datetime object.
    """
    datetime_format = '%Y-%m-%d'
    return pd.to_datetime(df[column], format=datetime_format)


def set_utc(df, locale):
    """
    Converts to UTC time.
    """
    return df.tz_localize('utc').tz_convert(None)


# ==================================================
# MAIN
# ==================================================


def clear():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    """Main entry point for the script."""
    pass


if __name__ == '__main__':
    sys.exit(main())
















__author__ = "Jesse J. Ruiz & Ednalyn C. De Dios"
__copyright__ = "Copyright 2019, Codeup Data Science"
__credits__ = ["Maggie Guist", "Zach Gulde", "Michael P. Moran"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Ednalyn C. De Dios"
__email__ = "ednalyn.dedios@gmail.com"
__status__ = "Prototype"