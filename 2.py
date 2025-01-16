import numpy as np
import sympy

def coupon_collector_average(n, k):
    sum = 0
    for _ in range(k):
        sum += monte_carlo(n)
    return sum / k


def monte_carlo(n):
    num_coupons = 0
    collected = set()
    while len(collected) != n:
        collected.add(np.random.randint(0, n))
        num_coupons += 1
    return num_coupons


N = 10
print(f'n = {N}, k = 10   :' ,coupon_collector_average(N, 10))
print(f'n = {N}, k = 100  :' ,coupon_collector_average(N, 100))
print(f'n = {N}, k = 1000 :' ,coupon_collector_average(N, 1000))


s, i= sympy.symbols('s i')
p_Xi = (N - (i - 1))/N

# def pmf_Xi(x):
#     return p_Xi*(1 - p_Xi)**(x - 1)

# x = sympy.symbols('x')
# mgf_Xi = sympy.Sum(sympy.exp(s*x)*pmf_Xi(x), (x, 1, sympy.oo))

mgf_Xi = p_Xi*sympy.exp(s)/(1-(1-p_Xi)*sympy.exp(s))

mgf_X = 1
for ii in range(1, N + 1):
    mgf_X *= mgf_Xi.subs(i, ii)

average_X = sympy.diff(mgf_X, s).subs(s, 0)

print(f'n = {N}: E[X] =', average_X, '≃', average_X.evalf())


