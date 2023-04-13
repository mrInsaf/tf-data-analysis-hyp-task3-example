import pandas as pd
import numpy as np
from scipy.stats import t


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(train, test) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    mean_train = np.mean(train.values)
    std_train = np.std(train.values, ddof=1)
    mean_test = np.mean(test.values)
    std_test = np.std(test.values, ddof=1)
    # Вычислим доверительный интервал для разности выборочных средних
    se = np.sqrt((std_train**2)/len(train) + (std_test**2)/len(test))
    t_stat = t.ppf(0.97, df=(len(train)+len(test)-2))
    ci_low = (mean_train - mean_test) - t_stat*se
    ci_high = (mean_train - mean_test) + t_stat*se

    # Проверим, попадает ли ноль в доверительный интервал
    if (ci_low <= 0).any() and (ci_high >= 0).any():
        return False
    else:
        return True
