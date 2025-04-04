#%%
import matplotlib.pyplot as plt
import numpy as np

plt.rc('font',**{'family':'serif','serif':['Computer Modern'], 'size':'20'})
plt.rcParams['text.usetex'] = True
#plt.rcParams['font.size'] = 16

#%%

def x2(omega, lamda, gamma, kbT):
    nbar = 1 / (np.exp(omega / kbT) - 1)
    Q = omega / gamma
    temp_term = nbar + 1/2
    measurement_term = lamda * 2  * Q**3 /( omega**2 * (4 * Q**2 - 1))
    return temp_term + measurement_term

def p2(omega, lamda, gamma, kbT):
    nbar = 1 / (np.exp(omega / kbT) - 1)
    Q = omega / gamma
    temp_term = nbar + 1/2
    measurement_term = lamda /(omega**2) * (Q - 2 * Q**3 / (4 * Q**2 - 1))
    return temp_term + measurement_term

def E(omega, lamda, gamma, kbT):
    return omega/2 * (p2(omega, lamda, gamma, kbT) + x2(omega, lamda, gamma, kbT))


#%%
# Plotting x^2 vs lambda with varying Q factor

omega = 1
gamma = [0.5, 1, 1.5]
lamda = np.linspace(0, 2, 200)
kbT = 10

fig, ax = plt.subplots(1,1)

for g in gamma:
    ax.plot(lamda/omega, x2(omega, lamda, g, kbT), label = fr"$Q = {omega/g:.2f}$")

ax.set_xlabel(r"$\lambda / \omega$")
ax.set_ylabel(r"$\langle \tilde{x}^2 \rangle$")
ax.text(0, 11, r"\textbf{a}", fontsize=20)
ax.legend()
plt.savefig("../Bachelor_Thesis/figures/x2_vs_lambda.pdf", bbox_inches="tight")

#%%
# Plotting x^2 vs Q with varying lambda

omega = 1
lamda = [0.5, 1, 1.5]
gamma = np.linspace(0.2, 1.5, 200)
kbT = 10

fig, ax = plt.subplots(1,1)

for l in lamda:
    ax.plot(omega/gamma, x2(omega, l, gamma, kbT), label = fr"$\lambda = {l:.2f}$")

ax.set_xlabel(r"$Q$")
ax.set_ylabel(r"$\langle \tilde{x}^2 \rangle$")
ax.text(0.7, 12, r"\textbf{b}", fontsize=20)
ax.legend()
plt.savefig("../Bachelor_Thesis/figures/x2_vs_Q.pdf", bbox_inches="tight")
#%%
# Plotting p^2 against lambda with varying Q factor
omega = 1
gamma = [0.5, 1, 1.5]
lamda = np.linspace(0, 2, 200)
kbT = 10

fig, ax = plt.subplots(1,1)

for g in gamma:
    ax.plot(lamda/omega, p2(omega, lamda, g, kbT), label = fr"$Q = {omega/g:.2f}$")

ax.set_xlabel(r"$\lambda / \omega$")
ax.set_ylabel(r"$\langle \tilde{p}^2 \rangle$")
ax.text(0, 10.8, r"\textbf{a}", fontsize=20)
ax.legend()
plt.savefig("../Bachelor_Thesis/figures/p2_vs_lambda.pdf", bbox_inches="tight")
#%%
# Plotting p^2 against Q with varying lambda
omega = 1
lamda = [0.5, 1, 1.5]
gamma = np.linspace(0.1, 1.8, 200)
kbT = 10

fig, ax = plt.subplots(1,1)

for l in lamda:
    ax.plot(omega/gamma, p2(omega, l, gamma, kbT), label = fr"$\lambda = {l:.2f}$")

ax.set_xlabel(r"$Q$")
ax.set_ylabel(r"$\langle \tilde{p}^2 \rangle$")
ax.text(0.5, 13, r"\textbf{b}", fontsize=20)
ax.legend()
plt.savefig("../Bachelor_Thesis/figures/p2_vs_Q.pdf", bbox_inches="tight")
#%%
# Plotting E against lambda with varying Q factor
omega = 1
gamma = [0.5, 1, 1.5]
lamda = np.linspace(0, 2, 200)
kbT = 10

fig, ax = plt.subplots(1,1)
fig.set_size_inches(6,4)

for g in gamma:
    ax.plot(lamda/omega, E(omega, lamda, g, kbT), label = fr"$Q = {omega/g:.2f}$")

ax.set_xlabel(r"$\lambda / \omega$")
ax.set_ylabel(r"$\langle \tilde{E} \rangle / \hbar\omega$")
ax.text(0, 10.8, r"\textbf{a}", fontsize=20, fontfamily="serif")
ax.legend()
plt.savefig("../Bachelor_Thesis/figures/E_vs_lambda.pdf", bbox_inches="tight")
#%%
# Plotting E against Q with varying lambda
omega = 1
lamda = [0.5, 1, 1.5]
gamma = np.linspace(0.1, 1.8, 200)
kbT = 10

fig, ax = plt.subplots(1,1)
fig.set_size_inches(6,4)

for l in lamda:
    ax.plot(omega/gamma, E(omega, l, gamma, kbT), label = fr"$\lambda = {l:.2f}$")

ax.set_xlabel(r"$Q$")
ax.set_ylabel(r"$\langle \tilde{E} \rangle / \hbar\omega$")
ax.text(0.5, 13, r"\textbf{b}", fontsize=20)
ax.legend()
plt.savefig("../Bachelor_Thesis/figures/E_vs_Q.pdf", bbox_inches="tight")

# %%
