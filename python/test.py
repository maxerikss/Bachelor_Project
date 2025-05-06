import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

plt.rc('font',**{'family':'serif','serif':['Computer Modern'], 'size':'12'})
plt.rcParams['text.usetex'] = True

def compute_D(f_tilde, omega, gamma, m, lambda_, hbar):
    im_f = np.imag(f_tilde)
    re_f = np.real(f_tilde)
    
    term1 = -gamma * (-2 * im_f + gamma) * (4 * im_f + gamma)
    term2 = 8 * im_f*re_f * omega
    term3 = -4 * (2 * im_f + gamma) * omega**2
    
    D = 8 * m * lambda_ * (term1 + term2 + term3) * hbar
    return D

def expval_x2(f_tilde, omega, gamma, m, nbar, lambda_, hbar):
    re_f = np.real(f_tilde)
    im_f = np.imag(f_tilde)
    
    D = compute_D(f_tilde, omega, gamma, m, lambda_, hbar)

    term1 = re_f * omega * (
        -2 * im_f * gamma * (re_f - 2 * m * omega)
        + re_f * (gamma**2 - 2 * re_f * omega)
    )
    
    term2 = -8 * m * (nbar + 0.5) * gamma * omega * (
        -2 * im_f * gamma + gamma**2  -2 * (re_f - 2 * omega) * omega
    )

    
    result = (1 / D) * (term1 + term2) * hbar
    return result

def expval_p2(f_tilde, omega, gamma, m, nbar, lambda_, hbar):
    re_f = np.real(f_tilde)
    im_f = np.imag(f_tilde)
    
    D = compute_D(f_tilde, omega, gamma, m, lambda_, hbar)

    term1 = re_f * omega * (
        -2 * re_f**3
        + re_f * (im_f * (2 + 4 * m) - gamma) * (4 * im_f + gamma)
        - 2 * (re_f**2 + 2 * im_f * m * (4 * im_f + gamma)) * omega
    )
    
    term2 = -8 * m * (nbar + 0.5) * gamma * lambda_ * (
        -8 * im_f**2 + 2 * im_f * gamma + gamma**2
        - 2 * (re_f - 2 * omega) * (re_f + omega)
    )
    
    result = (1 / D) * (term1 + term2) * hbar
    return result

def expval_E(f_tilde, omega, gamma, m, nbar, lambda_, hbar):
    x2 = expval_x2(f_tilde, omega, gamma, m, nbar, lambda_, hbar)
    p2 = expval_p2(f_tilde, omega, gamma, m, nbar, lambda_, hbar)
    E = 0.5 * omega * (x2 + p2)
    return E


import numpy as np
import matplotlib.pyplot as plt

# Constants (example values; adjust as needed)
omega = 1.0
gamma = 0.2
m = 1.0
nbar = 9.5
lambda_ = 0.8
hbar = 1.0

# Import the previously defined functions here
# compute_D, expval_x2, expval_p2, expval_E

# Grid of Re(f̃) and Im(f̃)
re_f_vals = np.linspace(-0, 0, 100)
im_f_vals = np.linspace(-0, 0, 100)
Re, Im = np.meshgrid(re_f_vals, im_f_vals)

# Allocate energy grid
E_vals = np.zeros_like(Re)
x2_vals = np.zeros_like(Re)
p2_vals = np.zeros_like(Re)

# Compute E at each grid point
for i in range(Re.shape[0]):
    for j in range(Re.shape[1]):
        f_tilde = Re[i, j] + 1j * Im[i, j]
        try:
            E_vals[i, j] = expval_E(f_tilde, omega, gamma, m, nbar, lambda_, hbar)
            x2_vals[i, j] = expval_x2(f_tilde, omega, gamma, m, nbar, lambda_, hbar)
            p2_vals[i, j] = expval_p2(f_tilde, omega, gamma, m, nbar, lambda_, hbar)
        except ZeroDivisionError:
            E_vals[i, j] = np.nan  # Handle division by zero in D
            x2_vals[i, j] = np.nan
            p2_vals[i, j] = np.nan

# Plotting

colors = ['red', 'blue']
cmap = mcolors.ListedColormap(colors)
bounds = [-np.inf, 0, np.inf]
norm = mcolors.BoundaryNorm(bounds, cmap.N)

plt.figure(figsize=(8, 6))
#contour = plt.contourf(Re, Im, E_vals, levels=100, cmap='jet')
contour = plt.contourf(Re, Im, x2_vals, levels=3, cmap=cmap, norm=norm)
plt.colorbar(contour, label='E')
plt.xlabel('Re(f)')
plt.ylabel('Im(f)')
plt.title('Contour Plot of E(f)')
plt.grid(True)
plt.tight_layout()
plt.show()

