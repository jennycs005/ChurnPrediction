#Part 1: Data Exploration
#Part 1.1: Understand the Raw Dataset
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)

churn_df = pd.read_csv('churn.all')
