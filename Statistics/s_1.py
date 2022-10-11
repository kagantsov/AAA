from scipy.stats import binom
from scipy.stats import binom_test
import numpy
from matplotlib import pyplot


# Кумулятивная функция распределения
print(binom.cdf(k=19, n=30, p=0.5))
print(1 - binom.cdf(k=19, n=30, p=0.5))

# Квантиль
print(binom.ppf(0.9506314266473055, n=30, p=0.5))
print(binom.ppf(0.94, n=30, p=0.5))

# Верхник порог альфы
alpha_max = 0.05
x = binom.ppf(1 - alpha_max, n=30, p=0.5)
print(x)

critical_value = binom.ppf(1 - alpha_max, n=30, p=0.5) + 1
print(critical_value)

# Истинная альфа
print(1 - binom.cdf(critical_value - 1, n=30, p=0.5))

# Статистический критерий - строгое математическое правило,
# по которому статистическая гипотеза H0 принимается или отвергается с известным уровнем значимости a

print(binom.pmf(k=15, n=30, p=0.5))

# График
pyplot.style.use('dark_background')
N = 30
mu0 = 0.5
# x = numpy.arange(start=0, stop=N + 1)
# y = binom.pmf(x, N, mu0)
#
# pyplot.figure(figsize=(16, 8))
# pyplot.vlines(x, 0, y, colors='w', linestyles='-', linewidth=15.0, label='pmf, $\mu = 0.5$')
# pyplot.title('Binomial distribution', fontsize=20)
# pyplot.legend(loc='best', frameon=False, prop={'size': 15})
# pyplot.xticks(fontsize=15)
# pyplot.yticks(fontsize=15)
# pyplot.show()

# P-value - вероятность при H0 получить настолько же или более экстремальное значение статистики,
# чем то, что мы получили

k = 19
p_value = 1 - binom.cdf(k - 1, n=N, p=mu0)
print(p_value)

if p_value <= alpha_max:
    print('Reject H0')
else:
    print('Do not reject H0')

x = numpy.arange(start=0, stop=N + 1)
y = binom.pmf(x, N, mu0)

# График 2
pyplot.figure(figsize=(16, 8))
pyplot.vlines(x, 0, y, colors='w', linestyles='-', linewidth=15.0, label='pmf, $\mu = 0.5$')
y_critical = [0 if x_i < critical_value else binom.pmf(x_i, N, mu0) for x_i in x]
pyplot.vlines(x, 0, y_critical, colors='y', linestyles='-', linewidth=12.0, label='alpha')
y_pval = [0 if x_i < k else binom.pmf(x_i, N, mu0) for x_i in x]
pyplot.vlines(x, 0, y_pval, colors='r', linestyles='-', linewidth=4.0, label='p-value')
pyplot.title('Binomial distribution', fontsize=20)
pyplot.legend(loc='best', frameon=False, prop={'size': 15})
pyplot.xticks(fontsize=15)
pyplot.yticks(fontsize=15)
pyplot.show()

# Двусторонний критерий
alpha_max = 0.05
N = 30
mu0 = 0.5

critical_value_right = binom.ppf(q=1 - alpha_max / 2, n=N, p=mu0) + 1
critical_value_left = binom.ppf(q=alpha_max / 2, n=N, p=mu0) - 1
print(f'if k <= {critical_value_left:.0f} or k >= {critical_value_right:.0f} then reject H0')

alpha = (
    1 - binom.cdf(critical_value_right - 1, n=N, p=0.5)
    + binom.cdf(critical_value_left - 1, n=N, p=0.5)
)
print(alpha)

# P-value в двустороннем случе
k = 22
p_value_onesided = 1 - binom.cdf(k-1, n=N, p=0.5)
p_value_2sided = p_value_onesided * 2
print(p_value_2sided)

k = 8
p_value_onesided = 1 - binom.cdf(k-1, n=N, p=0.5)

if p_value_onesided > 0.5:
    p_value_onesided = binom.cdf(k, n=N, p=0.5)

p_value_2sided = p_value_onesided * 2

if p_value_2sided > 1:
    p_value_2sided = 1

print(p_value_2sided)

#
print(binom_test(x=28, n=35, p=0.907, alternative='two-sided'))
print(binom_test(x=35, n=35, p=0.907, alternative='two-sided'))
