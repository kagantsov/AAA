from scipy.stats import (
    norm, binom, expon
)
import numpy as numpy
from seaborn import distplot
from matplotlib import pyplot
import seaborn

import sys

sys.path.append('.')

# 3.1. Критерии сравнения средних

# Test 1000 users - ARPUt
# Control 1000 users - ARPUc

# Нормальное распределение
# Если у нас есть 2 случайные величины, то сумма этих двух случайный величин тоже имеет нормальное распределение

# инициализация
stand_norm = norm(loc=0, scale=1)

# cumulative distribution function
print(f'P(X <= 2) = {stand_norm.cdf(x=2)}')
print(f'или так {norm(loc=0, scale=1).cdf(x=2)}')

# можно указывать массивы
print(f'[P(X <= 2), P(X <= -1)] = {stand_norm.cdf([2, -1])}')

# persent point function
print(f'Quantile 0.975 = {stand_norm.ppf(0.975)}')

# probability density function
print(f'pdf(0) = {stand_norm.pdf(0)}')


# Нарисуем график нормального распределение
# check_distr = norm(loc=0, scale=2)
# x = numpy.linspace(-8, 8, 1000)
# pdf = check_distr.pdf(x)
# cdf = check_distr.cdf(x)
# sample = check_distr.rvs(10000)
#
# pyplot.figure(figsize=(22, 5))
# pyplot.title('Визуализация плотности', fontsize=12)
# pyplot.hist(sample, bins='auto', density=True, alpha=0.6, label='сгенерированные значения')
# pyplot.plot(x, pdf, label='плотность распределения')
# pyplot.legend(fontsize=12)
# pyplot.show()
#
# pyplot.subplot(1, 2, 2)
# pyplot.title('Визуализация функции распределения', fontsize=12, color='black')
# pyplot.plot(x, cdf)
# pyplot.show()

# Если наша статистика - это x средняя, то по ЦПТ, она будет распределена нормально

# def binom_generator(p, n, size):
#     return binom(p=p, n=n).rvs(size)
#
# p = 0.01
# n = 20
# size = 5000
#
# print(visualize_CLT(lambda: binom_generator(p, n, size),
#               expected_value = p * n,
#               variance = n * p * (1-p)
#               ))

# 3.2. Z-тест

def get_pvalue_by_old_logic(n, mu0, t):
    return 1 - binom.cdf(t - 1, n=n, p=mu0)


n = 30
mu0 = 0.5
t = 19

old_p_value = get_pvalue_by_old_logic(n, mu0, t)
print(f"p-value, полученное по старой, корректной формуле: {old_p_value}")

def get_pvalue_by_normal_approx(n, mu0, t):
    sum_mu = n * mu0
    sum_variance = n * mu0 * (1 - mu0)
    sum_std = numpy.sqrt(sum_variance)

    return 1 - norm(loc=sum_mu, scale=sum_std).cdf(t)

normal_dist_p_value = get_pvalue_by_normal_approx(n, mu0, t)
print(f"p-value, полученное из приближения нормальным распределением: {normal_dist_p_value}")

n = 3000
mu0 = 0.5
t = 1544

old_p_value = get_pvalue_by_old_logic(n, mu0, t)
print(f"p-value, полученное по старой, корректной формуле: {old_p_value}")
normal_dist_p_value = get_pvalue_by_normal_approx(n, mu0, t)
print(f"p-value, полученное из приближения нормальным распределением: {normal_dist_p_value}")

def z_criterion_pvalue(sample_mean, sample_size, mu0, variance):
    Z_statistic = numpy.sqrt(sample_size) * (sample_mean - mu0) / numpy.sqrt(variance)
    return 1 - norm().cdf(Z_statistic)

n = 30
t = 19
mu0 = 0.5
variance = mu0 * (1 - mu0)

old_p_value = get_pvalue_by_old_logic(n, mu0, t)
print(f"p-value, полученное по старой, корректной формуле: {old_p_value}")
normal_p_value = get_pvalue_by_normal_approx(n, mu0, t)
print(f"p-value, полученное из приближения нормальным распределением: {normal_p_value}")
z_pvalue = z_criterion_pvalue(t/n, n, mu0, variance)
print(f"Z-тест p-value: {z_pvalue}")

# 3.3. Занятие со звездочкой, Z-тест

def get_pvalue_by_normal_approx_with_addition(n, mu0, t):
    sum_mu = n * mu0
    sum_variance = n * mu0 * (1 - mu0)
    sum_std = numpy.sqrt(sum_variance)

    return 1 - norm(loc=sum_mu, scale=sum_std).cdf(t - 0.5)

n = 500
t = 250
mu0 = 0.4

old_p_value = get_pvalue_by_old_logic(n, mu0, t)
print(f"p-value, полученное по старой, корректной формуле: {old_p_value}")
normal_dist_p_value = get_pvalue_by_normal_approx(n, mu0, t)
print(f"p-value, полученное из приближения нормальным распределением: {normal_dist_p_value}")
normal_with_add_p_value = get_pvalue_by_normal_approx_with_addition(n, mu0, t)
print(f"p-value, полученное из приближения нормальным распределением с поправкой: {normal_with_add_p_value}")

def z_criterion_pvalue(sample_mean, sample_size, mu0, variance, use_continuity_correction=False):
    if use_continuity_correction:
        # корректируем значение суммы, как делали это ранее
        sample_mean = (sample_mean * sample_size - 1/2) / sample_size
    Z_statistic = numpy.sqrt(sample_size) * (sample_mean - mu0) / numpy.sqrt(variance)
    return 1 - norm().cdf(Z_statistic)

n = 500
t = 250
mu0 = 0.4
variance = mu0 * (1 - mu0)

old_p_value = get_pvalue_by_old_logic(n, mu0, t)
print(f"p-value, полученное по старой, корректной формуле: {old_p_value}")
normal_with_add_p_value = get_pvalue_by_normal_approx_with_addition(n, mu0, t)
print(f"p-value, полученное из приближения нормальным распределением с поправкой: {normal_with_add_p_value}")
z_pvalue = z_criterion_pvalue(t/n, n, mu0, variance, use_continuity_correction=True)
print(f"Z-тест p-value: {z_pvalue}")