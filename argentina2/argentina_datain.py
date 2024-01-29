import pandas as pd
import numpy as np
import os
from os.path import expanduser
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import statsmodels.tsa.filters.hp_filter
from datetime import datetime

home = expanduser("~")
target_path = "/git/school/research/bianchim_rf_ltd/argentina2"
os.chdir(home + target_path)


data = pd.read_csv("datay.csv")
data["gdp_log"] = np.log(data["Real GDP"])

(data["gdp_cycle"], data["gdp_trend"]) = statsmodels.tsa.filters.hp_filter.hpfilter(data["gdp_log"], lamb=6.25)
data.to_csv("datay_clean.csv")


