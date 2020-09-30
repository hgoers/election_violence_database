# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 16:18:23 2020

@author: hgoer
"""

# Import libraries
import pandas as pd
from clean_names import *

# Read in election dates data
df_elections = pd.read_csv("https://raw.githubusercontent.com/hgoers/election_dates_database/master/Election_dates.csv")

# Clean country names
df_elections['country'] = clean_names(df_elections['country'])

# Remove elections where no date has been set
df_elections = df_elections[df_elections["date"]!="None"]
df_elections["date"] = pd.to_datetime(df_elections["date"])

