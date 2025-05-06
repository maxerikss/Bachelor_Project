import matplotlib.pyplot as plt
import numpy as np

# Use LaTeX and serif font
plt.rc('font', **{'family': 'serif', 'serif': ['Computer Modern'], 'size': 12})
plt.rcParams['text.usetex'] = True

# Vectorized x2
def x2(omega, lamda, gamma, kbT, imf, ref):
    nbar = 1 / (np.exp(omega / kbT) - 1)
    D = 8 * lamda * (
        -gamma * (-2 * imf + gamma) * (4 * imf + gamma)
        + 8 * imf * ref * omega
        - 4 * (2 * imf + gamma) * omega**2
    )
    top = ref * omega * (
        -2 * imf * gamma * (ref - 2 * omega)
        + ref * (gamma**2 - 2 * ref * omega)
    )
    bottom = -8 * (nbar + 0.5) * gamma * omega * (-2 * imf * gamma + gamma**2)
    correction = -2 * (ref - 2 * omega) * omega
    return (top + bottom + correction) / D

# Vectorized p2
def p2(omega, lamda, gamma, kbT, imf, ref):
    nbar = 1 / (np.exp(omega / kbT) - 1)
    D = 8 * lamda * (
        -gamma * (-2 * imf + gamma) * (4 * imf + gamma)
        + 8 * imf * ref * omega
        - 4 * (2 * imf + gamma) * omega**2
    )
    top = ref * omega * (
        -2 * ref**3
        + ref * (imf * (2 + 4) - gamma) * (4 * imf + gamma)
        - 2 * (ref**2 + 2 * imf * (4 * imf + gamma)) * omega
    )
    bottom = -8 * (nbar + 0.5) * gamma * lamda * (
        -8 * imf**2 + 2 * imf * gamma + gamma**2
        - 2 * (ref - 2 * omega) * (ref + omega)
    )
    return (top + bottom) / D

# Energy
def E(omega, lamda, gamma, kbT, imf, ref):
    return 0.5 * omega * (x2(omega, lamda, gamma, kbT, imf, ref) + p2(omega, lamda, gamma, kbT, imf, ref))

# Constants
omega = 1
kbT = 10
gamma = 0.1
lamda = 1

# Grid of values
imf = np.linspace(-0.1, 0.1, 250)
ref = np.linspace(-0.5, 0.5, 250)
X, Y = np.meshgrid(ref, imf)

# Compute energy on grid
Z = E(omega, lamda, gamma, kbT, Y, X)

# Plotting
fig, ax = plt.subplots()
plot = ax.contourf(X, Y, Z, levels=50, cmap='viridis')
cbar = fig.colorbar(plot, ax=ax)
cbar.set_label(r'$E(\tilde{f})$')
ax.set_xlabel(r'$\mathrm{Re}(\tilde{f})$')
ax.set_ylabel(r'$\mathrm{Im}(\tilde{f})$')
ax.set_title(r'Contour Plot of Energy $E$')
plt.tight_layout()
plt.show()
