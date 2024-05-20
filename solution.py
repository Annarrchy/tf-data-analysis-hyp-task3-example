import pandas as pd
import numpy as np


chat_id = 1063441199 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    import scipy.stats as sps
    alpha = 0.09
    return sps.ttest_ind(x, y)[1] <= alpha
