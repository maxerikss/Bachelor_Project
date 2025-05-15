import matplotlib.pyplot as plt
import numpy as np

plt.rc('font',**{'family':'serif','serif':['Computer Modern'], 'size':'12'})
plt.rc('text.latex', preamble=r'\usepackage{amssymb,amsmath,amsfonts,amsthm}')
plt.rcParams['text.usetex'] = True

## defining funcitons
def x2(omega, lamda, gamma, kbT):
    nbar = 1 / (np.exp(omega / kbT) - 1)
    Q = omega / gamma
    temp_term = nbar + 1/2
    measurement_term = lamda * 2  * Q**3 /( omega**2 * (4 * Q**2 + 1))
    return temp_term + measurement_term

def p2(omega, lamda, gamma, kbT):
    nbar = 1 / (np.exp(omega / kbT) - 1)
    Q = omega / gamma
    temp_term = nbar + 1/2
    measurement_term = lamda /(omega**2) * (Q - 2 * Q**3 / (4 * Q**2 + 1))
    return temp_term + measurement_term

def E(omega, lamda, gamma, kbT):
    return omega/2 * (p2(omega, lamda, gamma, kbT) + x2(omega, lamda, gamma, kbT))

## defining constants
omega = 1
kbT = 10

## defining figure object
fig, axes = plt.subplots(3, 2)
fig.set_size_inches(7.27, 11)

## plotting against lambda
gamma = [0.5, 1, 1.5]
lamda = np.linspace(0, 2, 200)

for g in gamma:
    axes[0,0].plot(lamda/omega, E(omega, lamda, g, kbT), label = fr"$Q = {omega/g:.2f}$")
    axes[1,0].plot(lamda/omega, x2(omega, lamda, g, kbT), label = fr"$Q = {omega/g:.2f}$")
    axes[2,0].plot(lamda/omega, p2(omega, lamda, g, kbT), label = fr"$Q = {omega/g:.2f}$")

## plotting against Q
lamda = [0.5, 1, 1.5]
gamma = np.linspace(0.1, 20, 200)

for l in lamda:
    axes[0,1].plot(omega/gamma, E(omega, l, gamma, kbT), label = fr"$\lambda = {l:.2f}$")
    axes[1,1].plot(omega/gamma, x2(omega, l, gamma, kbT), label = fr"$\lambda = {l:.2f}$")
    axes[2,1].plot(omega/gamma, p2(omega, l, gamma, kbT), label = fr"$\lambda = {l:.2f}$")

## setting labels
axes[2,0].set_xlabel(r"$\lambda / \omega$")
axes[2,1].set_xlabel(r"Q")

axes[0,0].set_ylabel(r"$ \tilde{E}_\text{ss} $")
axes[1,0].set_ylabel(r"$\langle \tilde{x}^2 \rangle_\text{ss}$")
axes[2,0].set_ylabel(r"$\langle \tilde{p}^2 \rangle_\text{ss}$")

## legend
for ax in axes.flatten():
    ax.legend()

## adding text on panels
xTestPos = 0.05
yTextPos = 0.52
axes[0,0].text(xTestPos, yTextPos, r"\textbf{a}", transform=axes[0,0].transAxes, fontsize=20)
axes[0,1].text(xTestPos, yTextPos, r"\textbf{b}", transform=axes[0,1].transAxes, fontsize=20)

axes[1,0].text(xTestPos, yTextPos, r"\textbf{c}", transform=axes[1,0].transAxes, fontsize=20)
axes[1,1].text(xTestPos, yTextPos, r"\textbf{d}", transform=axes[1,1].transAxes, fontsize=20)

axes[2,0].text(xTestPos, yTextPos, r"\textbf{e}", transform=axes[2,0].transAxes, fontsize=20)
axes[2,1].text(xTestPos, yTextPos, r"\textbf{f}", transform=axes[2,1].transAxes, fontsize=20)


plt.savefig("../Bachelor_Thesis/figures/measurement_result.pdf", bbox_inches="tight")