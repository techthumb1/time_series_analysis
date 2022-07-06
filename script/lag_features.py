# create a dataset for sales
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# configure our parameters 
p = ('Maximum level of lag: Lag_{}'.format(p))
d = ('Maximum level of lag: Lag_{}'.format(d))
q = ('Maximum level of lag: Lag_{}'.format(q))

def moving_average(p, d, q):
    first_lag = [train['sales'],:].shift - 1ß