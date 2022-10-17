import numpy
from matplotlib import pyplot
from scipy.stats import binom
from statsmodels.stats.proportion import proportion_confint

# 2.1 Статистическая мощность

# Статистический критерий - строго математическое правило, по которому статистическая гипотеза H0 принимается или
# отвергается с известным уровнем значимости a

# H0: сейчас лето
# H1: сейчас не лето
# Критерий Тимура: если за окном идет снег, то мы отвергаем H0. Иначе не отвергать H0.
# Вероятность увидеть снег летом равно 0.001
# a = 0.001

# Критерий Сноу
# H0: любая
# H1: H0 неверна
# Критерий Сноу: с вероятностью a отклонить H0, с вероятностью 1-a - не отклонять
# Заметим, что если H0 верна, то вероятность false rejection равна a

# Мощность статистического критерия
# Вернемся к задаче про лето
# Вероятность принять H0, если она неверна
# Пусть 90% дней с сентября по май снег не шел
# b = 0.9

# a
# статистическая значимость
# вероятность отвергнуть H0, если она верна
# вероятность false rejection
# вероятность ошибки первого рода
# вероятность false positive (в статистике отвержение H0 в пользу H1 - это вердикт positive)
# False Positive Rate

# b
# вероятность принять H0, если она неверна
# вероятность пропустить открытие
# вероятность ошибки второго рода
# вероятность false negative
# False Negative Rate

# Статистическая мощность = 1-b
# вероятность принять H1, если она неверна
# True Positive Rate

# Критерий Тимура: если за окном идет снег, то мы отвергаем H0. Иначе не отвергать H0.
# statistical significance = a = 0.001
# statistical power = 1-b = 1-0.90 = 0.10

# Критерий Сноу: с вероятностью a отвергнуть H0. С вероятностью 1-a не отвергать H0.
# statistical significance = a = 0.001
# statistical power = вероятность принять H1, если она верна = 0.001

# 2.2 Мощность для задачи с конверсией
mu0 = blue_button_average_conversion = 0.5
N = 30
alpha_max = 0.05

critical_value = binom.ppf(q=1 - alpha_max, n=N, p=mu0) + 1
print(f'if k >= {critical_value:.0f} then reject HO')

mu = 0.6
power = 1 - binom.cdf(critical_value - 1, n=N, p=mu)
print(power)


def get_stat_power(N, mu0, true_mu, alpha_max):
    # значение, начиная с которого, мы отвергаем H0
    critical_value = binom.ppf(1 - alpha_max, N, mu0) + 1
    # вероятность получить critical_value из n или больше
    # = 1 - (вероятность получить critical_value-1 из n или меньше)
    return 1 - binom.cdf(critical_value - 1, N, true_mu)


print(get_stat_power(N=30, mu0=0.5, true_mu=0.6, alpha_max=0.05))
print(get_stat_power(N=300, mu0=0.5, true_mu=0.6, alpha_max=0.05))
print(get_stat_power(N=300, mu0=0.5, true_mu=0.51, alpha_max=0.05))
print(get_stat_power(N=15000, mu0=0.5, true_mu=0.51, alpha_max=0.05))

# Значение мощности в 80% считают приемлемым

N_vector = numpy.arange(start=1, stop=500 + 1, step=20)
power_vector = [get_stat_power(N, mu0=0.5, true_mu=0.6, alpha_max=0.05) for N in N_vector]

# Какая скорость роста мащности с ростом N
pyplot.figure(figsize=(16, 8))

# биноминальное респределение, параметр = mu0 = 0.5
pyplot.plot(N_vector, power_vector, 'black', linewidth=2.0)

pyplot.title('Power as a function of N', fontsize=20)

pyplot.xticks(fontsize=15)
pyplot.xlabel('N', fontsize=15)

pyplot.yticks(fontsize=15)
pyplot.ylabel('Statistical power', fontsize=15)

# pyplot.show()


# Как мощность зависит от истинного mu

mu_vector = numpy.arange(start=0.501, stop=1 + 0.01, step=0.01)
power_vector = [get_stat_power(N, mu0=0.5, true_mu=mu, alpha_max=0.05) for mu in mu_vector]

pyplot.figure(figsize=(16, 8))

# биноминальное респределение, параметр = mu0 = 0.5
pyplot.plot(mu_vector, power_vector, 'black', linewidth=2.0)

pyplot.title('Power as a function of $\mu$', fontsize=20)

pyplot.xticks(fontsize=15)
pyplot.xlabel('$\mu$', fontsize=15)

pyplot.yticks(fontsize=15)
pyplot.ylabel('Statistical power', fontsize=15)
pyplot.ylim(0, 1.1)


# pyplot.show()

# Мощность зависит от неизвестного нам истинного mu, следовательно
# Мощность нам в точности неизвестна

# Именно поэтому мы избегаем формулировки 'Принимаем H0', так как мы не знаем,
# с какой вероятностью это происходит ошибочно.
# Вместо этого мы осторожно говорим 'Не отвергаем H0'


# 2.3 Доверительный интервал

def conversion_criterion_2sided(N, mu0, alpha_max, k):
    critical_value_left = binom.ppf(alpha_max / 2, N, mu0) - 1
    critical_value_right = binom.ppf(1 - alpha_max / 2, N, mu0) + 1
    if k <= critical_value_left or k >= critical_value_right:
        # Reject HO
        return 1
    else:
        # Do not reject HO
        return 0


confidence_interval = []

for m in numpy.arange(start=0, stop=1.001, step=0.001):
    if conversion_criterion_2sided(N=30, mu0=m, alpha_max=0.05, k=19):
        pass
    else:
        confidence_interval.append(m)

print(f'95%-confidence interval: ' f'{min(confidence_interval):.3f} -- {max(confidence_interval):.3f}')
# print(binom.ppf(0.025, 30, 1))

# 2.4. Односторонний доверительный интервал
print(1 - binom(30, 0.439).cdf(18))


def conversion_criterion_rightsided(N, mu0, alpha_max, k):
    critical_value = binom.ppf(1 - alpha_max, N, mu0) + 1
    if k >= critical_value:
        # Reject HO
        return 1
    else:
        # Do not reject HO
        return 0


confidence_interval = []

for m in numpy.arange(start=0, stop=1.001, step=0.001):
    if conversion_criterion_rightsided(N=30, mu0=m, alpha_max=0.05, k=22):
        pass
    else:
        confidence_interval.append(m)

print(f'95%-confidence interval: ' f'{min(confidence_interval):.3f} -- {max(confidence_interval):.3f}')

confidence_interval = []

for m in numpy.arange(start=0, stop=1.001, step=0.001):
    if conversion_criterion_2sided(N=30, mu0=m, alpha_max=0.05 * 2, k=22):
        pass
    else:
        confidence_interval.append(m)

print(f'95%-confidence interval: ' f'{min(confidence_interval):.3f} -- {max(confidence_interval):.3f}')


# 2.5. Свойства доверительного интервала

# Пусть есть реализация некой статистики k и критерий для проверки H0: u = m
# Доверительный интервал для u, построенный на основании k - множество таких m,
# что критерий не отвергает для них H0: u = m
# 1 - a max называется уровнем доверия доверительного интервала

# Свойство доверительного интервала:
# Если для известного истинного u повторить эксперимент бесконечное количество раз:
# Насемплировать выборку
# Для выборки получить статистику k
# По статистике k построить с помощью критерия доверительный интервал
# То в >= 1 - a max случаев доверительный интервал будет содержать истинное u

def my_binominal_conf_int(N, alpha_max, k):
    confidence_interval = []
    for m in numpy.arange(start=0, stop=1.001, step=0.001):
        if conversion_criterion_2sided(N, m, alpha_max, k) == 0:
            # H0 is not rejected, therefore m is likely to be mu
            confidence_interval.append(m)
    return min(confidence_interval), max(confidence_interval)


print(my_binominal_conf_int(30, 0.10, 19))

# N = 20
# alpha_max = 0.10
# latent_mu = 0.5
#
# numpy.random.seed(1337)
#
# n_samples = 10000
# oops = 0
#
# for i in range(n_samples):
#     t = binom.rvs(n=N, p=latent_mu)
#
#     L, R = my_binominal_conf_int(N, alpha_max, t)
#
#     if latent_mu < L or latent_mu > R:
#         oops += 1
#
# print(f'latent mu is not contained in CI in {oops / n_samples:.2f} of all tests')

print(proportion_confint(count=19, nobs=30, alpha=0.10, method='wilson'))

print(my_binominal_conf_int(3000, 0.05, 1045))
print(proportion_confint(count=1045, nobs=3000, alpha=0.05, method='wilson'))

# 2.6. Minimum detectable effect (MDE)

N = 30
mu0 = 0.5
alpha_max = 0.05

critical_value = binom.ppf(q=1-alpha_max, n=N, p=mu0) + 1
print(f'If k >= {critical_value:.0f} then reject H0, otherwise not reject H0')


# Пусть mu -- такое значение параметра, что H0 отвергается с вероятностью 80%
# prediction_segment(mu) = [20, 30]
# binom(n=30, p=mu).ppf(q=0.20) = 20

power = 0.80
powerful_mu = None

for potential_mu in numpy.arange(start=0, stop=1.001, step=0.001):
    if binom(n=30, p=potential_mu).ppf(q=1-power) == critical_value:
        powerful_mu = potential_mu
        break

print(f'Minimum Detectable Effect is +{powerful_mu - mu0:.3f}')

print(1 - binom(n=30, p=0.719).cdf(19))
print(1 - binom(n=30, p=0.5 + 0.219).cdf(20-1))