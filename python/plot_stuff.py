#%%
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['text.usetex'] = True

#%%

def x2(omega, lamda, gamma, kbT):
    nbar = 1 / (np.exp(omega / kbT) - 1)
    Q = omega / gamma
    temp_term = nbar + 1/2
    measurement_term = lamda * 2  * Q**3 /( omega**2 * (4 * Q**2 - 1))
    return temp_term + measurement_term


#%%

omega = 1
gamma = [0.5, 1, 1.5]
lamda = np.linspace(0, 2, 200)
kbT = 10

#%%

fig, ax = plt.subplots(1,1)

for g in gamma:
    ax.plot(lamda/omega, x2(omega, lamda, g, kbT), label = fr"$Q = {omega/g:.2f}$")

ax.set_xlabel(r"$\lambda / \omega$")
ax.set_ylabel(r"$\langle \tilde{x}^2 \rangle$")
ax.legend()
plt.savefig("../Bachelor_Thesis/figures/x2_vs_lambda.pdf")

#%%

omega = 1
lamda = [0.5, 1, 1.5]
gamma = np.linspace(0.1, 1.8, 200)
kbT = 10

#%%
fig, ax = plt.subplots(1,1)

for l in lamda:
    ax.plot(omega/gamma, x2(omega, l, gamma, kbT), label = fr"$\lambda = {l:.2f}$")

ax.set_xlabel(r"$Q$")
ax.set_ylabel(r"$\langle \tilde{x}^2 \rangle$")
ax.legend()
plt.savefig("../Bachelor_Thesis/figures/x2_vs_Q.pdf")