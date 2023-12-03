from scipy.stats.stats import pearsonr
from random import randint

def pirson_correlation(first_array: list, second_array: list):
    return pearsonr(first_array, second_array)



for i in range(5):
    print(pirson_correlation(first_array=[randint(0,10) for _ in range(10)],
                             second_array=[randint(0,10) for _ in range(10)]))










