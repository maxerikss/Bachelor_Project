import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np


# Use LaTeX and serif font
plt.rc('font', **{'family': 'serif', 'serif': ['Computer Modern'], 'size': 12})
plt.rc('text.latex', preamble=r'\usepackage{amssymb,amsmath,amsfonts,amsthm}')
plt.rcParams['text.usetex'] = True

# Defining functions

def x2(n, L, Q, reG, imG):
    term1 = -16*L**2 * Q**3
    term2 = 4*L*(1 + 2*n)*(-1 + Q*(imG +2*Q*(-2 + reG)))
    term3 = Q**2 * reG * (reG + 2*Q*reG*(-1 + Q - Q*reG) - imG*(2 + Q*reG))
    nominator = term1 + term2 + term3
    denominator = 8*L*(-1 + Q*(-4*Q + imG*(-1 + 2*Q*(imG + 2*Q*(-1 + reG)))))
    return nominator/denominator

def p2(n, L, Q, reG, imG):
    term1 = 8*L**2 *Q *(-1 + Q*(-imG + 2*imG**2 * Q -2*Q*(1+reG)))
    term2 = 4*L*(1 + 2*n)*(-1 + Q*(-imG + 2*imG**2 *Q +2*Q*(-2+reG)*(1+reG)))
    term3 = -Q*reG*(reG + Q*(2*imG**2 * Q*(-2 + reG) + imG*(-2 + 3*reG) + 2*Q*reG*(1 + reG + Q*(-1 + reG**2))))
    nominator = term1 + term2 + term3
    denominator = 8*L*(-1 + Q*(-4*Q + imG*(-1 + 2*Q*(imG + 2*Q*(-1 + reG)))))
    return nominator/denominator

def E(n, L, Q, reG, imG):
    return 0.5 * (x2(n, L, Q, reG, imG) + p2(n, L, Q, reG, imG))

## defiining constants
kbT = 10
n = 1 / (np.exp(1 / kbT) - 1)
L = 2
Q = 10

### Defining colormap
colors = ['red', 'blue']
cmap = mcolors.ListedColormap(colors)
bounds = [-np.inf, 0, np.inf]
norm = mcolors.BoundaryNorm(bounds, cmap.N)


## Unzoomed numbers
resolution = 500
reG = np.linspace(-1, 3, resolution)
imG = np.linspace(-2, 2, resolution)
X, Y = np.meshgrid(reG, imG)
Z = E(n, L, Q, X, Y)

XOld, YOld = np.meshgrid(np.linspace(0, 0, resolution), np.linspace(0, 0, resolution))
ZOld = E(n, L, Q, XOld, YOld)

ZRatio = Z/ZOld

## Zoomed numbers
reGZoom = np.linspace(-1, 1, resolution)
imGZoom = np.linspace(0, 1.5, resolution)
XZoom, YZoom = np.meshgrid(reGZoom, imGZoom)
ZZoom = E(n, L, Q, XZoom, YZoom)
ZRatioZoom = ZZoom/ZOld


## Near zero values
reGZero = np.linspace(-0.1, 0.1, resolution)
imGZero = np.linspace(-0.1, 0.2, resolution)
XZero, YZero = np.meshgrid(reGZero, imGZero)
ZZero = E(n, L, Q, XZero, YZero)

ZZeroDiff = ZZero - ZOld

## Plotting
fig, axes = plt.subplots(1, 2, layout='compressed')
fig.set_size_inches(7.27, 4.5)

N = 1
levels = np.linspace(-N, N, 301)
contourPlotRatio = axes[0].contourf(X, Y, ZRatio, levels=levels, cmap='seismic', extend='both')
contourPlotRatioZoom = axes[1].contourf(XZoom, YZoom, ZRatioZoom, levels=levels, cmap='seismic', extend='both')

cBar = fig.colorbar(contourPlotRatio, ax=axes, orientation='horizontal')


## Setting labels
axes[0].set_xlabel(r"$\mathfrak{R} \{ \tilde{f} \}$")
axes[0].set_ylabel(r"$\mathfrak{I} \{ \tilde{f} \}$")
axes[1].set_xlabel(r"$\mathfrak{R} \{ \tilde{f} \}$")
axes[1].set_ylabel(r"$\mathfrak{I} \{ \tilde{f} \}$")

cBar.set_label(r"$\langle \tilde{E} \rangle_\text{feedback} / \langle \tilde{E} \rangle$")
cBar.set_ticks(np.linspace(-N, N, 9))

axes[0].text(-0.6, 1.3, r"\textbf{a}", fontsize=20)
axes[1].text(-0.75, 1.2, r"\textbf{b}", fontsize=20)

## Showing / Saving
#plt.show()
contourPlotRatio.set_edgecolor('face')
contourPlotRatioZoom.set_edgecolor('face')
#plt.savefig("../Bachelor_Thesis/figures/energyFeedbackRatio.pdf", dpi=300)
plt.close(fig)


## Plotting the difference near zero

fig, axes = plt.subplots(1, 1, layout='compressed')
fig.set_size_inches(7.27, 4.5)

N = 30
levels = np.linspace(-N, N, 301)
contourPlotZeroDiff = axes.contourf(XZero, YZero, ZZeroDiff, levels=levels, cmap='seismic', extend='both')

cBar = fig.colorbar(contourPlotZeroDiff, ax=axes, orientation='horizontal')

## Setting labels
axes.set_xlabel(r"$\mathfrak{R} \{ \tilde{f} \}$")
axes.set_ylabel(r"$\mathfrak{I} \{ \tilde{f} \}$")

cBar.set_label(r"$\langle \tilde{E} \rangle_\text{feedback} - \langle \tilde{E} \rangle$")
cBar.set_ticks(np.linspace(-N, N, 9))

## Showing / Saving
#plt.show()
contourPlotZeroDiff.set_edgecolor('face')
plt.savefig("../Bachelor_Thesis/figures/energyFeedbackDifference.pdf", dpi=300)
plt.close(fig)

## Comparing with the old Equation
def x2old(omega, lamda, gamma, kbT):
    nbar = 1 / (np.exp(omega / kbT) - 1)
    Q = omega / gamma
    temp_term = nbar + 1/2
    measurement_term = lamda * 2  * Q**3 /( omega**2 * (4 * Q**2 + 1))
    return temp_term + measurement_term

def p2old(omega, lamda, gamma, kbT):
    nbar = 1 / (np.exp(omega / kbT) - 1)
    Q = omega / gamma
    temp_term = nbar + 1/2
    measurement_term = lamda /(omega**2) * (Q - 2 * Q**3 / (4 * Q**2 + 1))
    return temp_term + measurement_term

def Eold(omega, lamda, gamma, kbT):
    return omega/2 * (p2old(omega, lamda, gamma, kbT) + x2old(omega, lamda, gamma, kbT))

#print(Eold(1, 2, 0.1, 10))
#print(E(n, L, Q, 0, 0))
