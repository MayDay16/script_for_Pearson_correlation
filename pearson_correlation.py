from functools import reduce
import math

def calculate_mean(values):
    return sum(values) / len(values)

def calculate_pearson_correlation(arr1, arr2):
    n = len(arr1)

    mean_arr1 = calculate_mean(arr1)
    mean_arr2 = calculate_mean(arr2)

    subtract_mean = lambda xi, mean: xi - mean

    subtracted_arr1 = list(map(subtract_mean, arr1, [mean_arr1] * n))
    subtracted_arr2 = list(map(subtract_mean, arr2, [mean_arr2] * n))

    multiply = lambda xi, yi: xi * yi
    product_sum = reduce(lambda acc, pair: acc + multiply(*pair), zip(subtracted_arr1, subtracted_arr2), 0)

    sum_squared_diff_arr1 = sum(map(lambda xi: xi ** 2, subtracted_arr1))
    sum_squared_diff_arr2 = sum(map(lambda yi: yi ** 2, subtracted_arr2))

    denominator = math.sqrt(sum_squared_diff_arr1 * sum_squared_diff_arr2)

    if denominator == 0:
        return 0

    correlation = product_sum / denominator
    return correlation

# Пример использования
arr1 = [874, 456, 212, 495, 23]
arr2 = [198, 432, 221, 499, 72]

correlation = calculate_pearson_correlation(arr1, arr2)
print(f"The Pearson correlation coefficient: {correlation}")
