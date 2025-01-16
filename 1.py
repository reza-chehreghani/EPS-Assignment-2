import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import poisson, binom

tarbiat = pd.read_csv('Tarbiat.csv')
metro = tarbiat['metro']
brt = tarbiat['BRT']

fig, axs = plt.subplots(2, 2)

metro_and_brt_range = np.arange(np.minimum(np.min(metro), np.min(brt)) - 0.5, np.maximum(np.max(metro), np.max(brt)) + 1.5)
axs[0][0].hist([metro, brt], metro_and_brt_range, label=['metro', 'BRT'])
axs[0][0].legend()
axs[0][0].set_title('part 1')


X_randvar = np.array(metro)
Y_randvar = np.array(brt)

X_lambda = np.mean(X_randvar)
Y_lambda = np.mean(Y_randvar)

metro_range = np.arange(np.min(metro) - 0.5, np.max(metro) + 1.5)
axs[0][1].hist(metro, metro_range, density=True, label='metro')

X_range = np.arange(min(X_randvar), max(X_randvar) + 1)
axs[0][1].plot(X_range, poisson.pmf(X_range, X_lambda), label=f'X~Poi({X_lambda:.1f})')
axs[0][1].legend()
axs[0][1].set_title('part 4')


Z_randvar = X_randvar + Y_randvar
Z_lambda = X_lambda + Y_lambda

Z_range = np.arange(np.min(Z_randvar), np.max(Z_randvar) + 1)
axs[1][0].plot(Z_range, poisson.pmf(Z_range, Z_lambda), label=f'Z~Poi({Z_lambda:.1f})')

sum_metro_and_brt = metro + brt
sum_metro_and_brt_range = np.arange(min(sum_metro_and_brt) - 0.5, max(sum_metro_and_brt) + 1.5)
axs[1][0].hist(sum_metro_and_brt, sum_metro_and_brt_range, density=True, label='sum of metro and BRT')
axs[1][0].legend()
axs[1][0].set_title('part 5')


W_prob = X_lambda / Z_lambda
N = 8
W_range = np.arange(0, N + 1)

axs[1][1].plot(W_range, binom.pmf(W_range, N, W_prob), label=f'W~Bin({N}, {W_prob:.1f})')

conditional_metro = tarbiat[tarbiat['metro'] + tarbiat['BRT'] == N]['metro']
conditional_metro_range = np.arange(np.min(conditional_metro) - 0.5, np.max(conditional_metro) + 1.5)
axs[1][1].hist(conditional_metro, conditional_metro_range, density=True, label='conditional metro')
axs[1][1].legend()
axs[1][1].set_title('part 8')

plt.show()