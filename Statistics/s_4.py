from scipy.stats import (
    norm, binom, expon, t, chi2, pareto, ttest_1samp, ttest_ind, sem
)
from statsmodels.stats.api import CompareMeans, DescrStatsW
from statsmodels.stats.proportion import proportion_confint
import numpy as numpy
from seaborn import distplot
from matplotlib import pyplot
import seaborn

import sys

sys.path.append('.')

import warnings

warnings.filterwarnings("ignore")

# 4.1 Критерии сравнения средних. Т-критерий Стьюдента

X = numpy.array([6.9, 6.45, 6.32, 6.88, 6.09, 7.13, 6.76])
print(f"Среднее время загрузки в СУБД: {round(numpy.mean(X), 2)}")

# ddof = 1 -- Это значит, что делим не на n, а на n-1 в формуле выше
print(f"Оценка sigma^2: {numpy.var(X, ddof=1)}")


def sample_statistics(number_of_experiments, statistic_function, sample_size, sample_distr):
    """
        Функция для генерации выборки некой статистики statistic_function, построенной по выборке из распределения sample_distr.
        Возвращает выборку размера number_of_experiments для statistic_function.

        Праметры:
            - number_of_experiments: число экспериментов, в каждом из которых мы посчитаем statistic_function
            - statistic_function: статистика, которая принимает на вход выборку из распределения sample_distr
            - sample_size: размер выборки, которая подается на вход statistic_function
            - sample_distr: распределение изначальной выборки, по которой считается статистика
    """

    statistic_sample = []
    for _ in range(number_of_experiments):
        # генерируем number_of_experiments раз выборку
        sample = sample_distr.rvs(sample_size)

        # считаем статистику
        statistic = statistic_function(sample)

        # сохраняем
        statistic_sample.append(statistic)
    return statistic_sample


numpy.random.seed(8)

sample_size = 7
M = 100000
sample_distr = norm(loc=5, scale=3)  # Пусть выборка из этого распределения

T_X = lambda sample: numpy.sqrt(sample_size) * (numpy.mean(sample) - sample_distr.mean()) / numpy.sqrt(
    numpy.var(sample, ddof=1))  # или numpy.std
Z_X = lambda sample: numpy.sqrt(sample_size) * (numpy.mean(sample) - sample_distr.mean()) / sample_distr.std()
samples = {
    "T(X)": sample_statistics(
        number_of_experiments=M, statistic_function=T_X,
        sample_size=sample_size, sample_distr=sample_distr),

    "Z(X)": sample_statistics(
        number_of_experiments=M, statistic_function=Z_X,
        sample_size=sample_size, sample_distr=sample_distr)
}

# pyplot.figure(figsize=(22, 5))
#
# for i, name in enumerate(["T(X)", "Z(X)"]):
#     pyplot.subplot(1, 2, i + 1)
#     current_sample = samples[name]
#     l_bound, r_bound = numpy.quantile(current_sample, [0.001, 0.999])
#
#     x = numpy.linspace(l_bound, r_bound, 1000)
#     pyplot.title(f'Распределение статистики {name}, sample size={sample_size}', fontsize=12)
#     distplot(current_sample, label='Эмпирическое распределение')
#     pyplot.plot(x, norm(0, 1).pdf(x), label='$\mathcal{N}(0, 1)$')
#     pyplot.legend(fontsize=12)
#     pyplot.xlabel(f'{name}', fontsize=12)
#     pyplot.xlim((l_bound, r_bound))
#     pyplot.ylabel('Плотность', fontsize=12)
#     pyplot.grid(linewidth=0.2)
# pyplot.show()

numpy.random.seed(42)

S2 = lambda sample: numpy.std(sample, ddof=1)
S2_sample = sample_statistics(
    number_of_experiments=M, statistic_function=S2,
    sample_size=sample_size, sample_distr=sample_distr
)

# pyplot.figure(figsize=(10, 5))
# pyplot.title('Распределение $\sqrt{S^2}$', fontsize=12)
# distplot(S2_sample, label='Эмпирическое распределение')
# pyplot.legend(fontsize=12)
# pyplot.xlabel('$\sqrt{S^2}$', fontsize=12)
# pyplot.ylabel('Плотность распределения', fontsize=12)
# pyplot.grid(linewidth=0.2)
# pyplot.show()

# T-test

numpy.random.seed(42)

eta_statistic = lambda sample: numpy.var(sample, ddof=1) * (sample_size - 1) / sample_distr.var()
eta_sample = sample_statistics(
    number_of_experiments=M, statistic_function=eta_statistic,
    sample_size=sample_size, sample_distr=sample_distr
)

chi2_dist = chi2(df=sample_size - 1)  # Распределение chi2

l_bound, r_bound = numpy.quantile(S2_sample, [0.001, 0.999])
x = numpy.linspace(l_bound, r_bound, 1000)

# pyplot.figure(figsize=(10, 5))
# pyplot.title('Распределение $\eta$', fontsize=12)
# distplot(eta_sample, label='Эмпирическое распределение')
# pyplot.plot(x, chi2_dist.pdf(x), label='Chi2(n-1)')
# pyplot.legend(fontsize=12)
# pyplot.xlabel('$\eta$', fontsize=12)
# pyplot.ylabel('Плотность распределения', fontsize=12)
# pyplot.grid(linewidth=0.2)
# pyplot.show()

numpy.random.seed(42)

T_X = lambda sample: numpy.sqrt(sample_size) * (numpy.mean(sample) - sample_distr.mean()) / numpy.std(sample, ddof=1)
T_sample = sample_statistics(
    number_of_experiments=M, statistic_function=T_X,
    sample_size=sample_size, sample_distr=sample_distr
)

T_dist = t(df=sample_size - 1)  # Распределение T Стьюдента

l_bound, r_bound = numpy.quantile(T_sample, [0.001, 0.999])
x = numpy.linspace(l_bound, r_bound, 1000)

# pyplot.figure(figsize=(10, 5))
# pyplot.title('Распределение $T(X)$', fontsize=12)
# distplot(T_sample, color='royalblue', label='Эмпирическое распределение')
# pyplot.plot(x, T_dist.pdf(x), c='green', label='T(n-1)')
# pyplot.plot(x, norm(0, 1).pdf(x), c='yellow', label='$\mathcal{N}(0, 1)$')
# pyplot.legend(fontsize=12)
# pyplot.xlabel('$T(X)$', fontsize=12)
# pyplot.ylabel('Плотность распределения', fontsize=12)
# pyplot.xlim((l_bound, r_bound))
# pyplot.grid(linewidth=0.2)
# pyplot.show()

# Как вызывать критерий
# print(ttest_1samp(norm(loc=0, scale=1).rvs(100), popmean=-1, alternative='greater'))

# X = numpy.array([6.9, 6.45, 6.32, 6.88, 6.09, 7.13, 6.76])
# t_stat = (numpy.mean(X) - 7) / (numpy.var(X, ddof=1) / 7) ** 0.5
# print(t_stat)
#
# p_value = t(7 - 1).cdf(-2.69024)
# print(p_value)

# 4.3. Доверительный интервал

sample = norm(loc=10, scale=2).rvs(100)

# sem -- standart error of the mean, sem = sqrt(S^2)/sqrt(n)
left_bound, right_bound = t.interval(alpha=0.95, loc=numpy.mean(sample), df=len(sample)-1, scale=sem(sample))
print(f"CI = [{round(left_bound, 2)}, {round(right_bound, 2)}]")