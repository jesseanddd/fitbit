#!/usr/bin/env python

"""
This script contains code used by the following jupytr notebooks:

- fitbit.ipynb

Special care taken to avoid hardcoding as much as possible.
"""



# ===========
# ENVIRONMENT
# ===========


import pandas as pd
import numpy as np
from datetime import datetime
import itertools

# data visualization
import matplotlib
import seaborn as sns
import statsmodels.api as sm

%matplotlib inline

# ignore warnings
import warnings
warnings.filterwarnings("ignore")

import glob
import os