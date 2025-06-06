import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from numpy import linalg as LA
import matplotlib.gridspec as gridspec

# Use LaTeX and serif font
plt.rc('font', **{'family': 'serif', 'serif': ['Computer Modern'], 'size': 12})
plt.rc('text.latex', preamble=r'\usepackage{amssymb}')
plt.rcParams['text.usetex'] = True


## Defining functions
def generateA(Q, reG, imG):
    row1 = np.array([ -1 - 2*Q*imG, np.zeros_like(imG), -Q*np.ones_like(imG) ])
    row2 = np.array([ np.zeros_like(imG), -np.ones_like(imG), Q*(1 + reG) ])
    row3 = np.array([ 2*Q*(1 + reG), 2*Q*np.ones_like(imG), -1 - Q*imG ])
    A = np.array([row1, row2, row3])
    return A

## Defining constants / parameters
resolution = 400
Q = 10
#reG = np.linspace(-0.25, 0.25, resolution)
#imG = np.linspace(-0.25, 0.25, resolution)
reG = np.linspace(-2, 2, resolution)
imG = np.linspace(-2, 2, resolution)
X, Y = np.meshgrid(reG, imG)

## Generating eigenvalues
AList = generateA(Q, X, Y)
eVals = np.zeros((AList.shape[2], AList.shape[3], 3), dtype=np.complex128)

for i in range(AList.shape[2]):
    for j in range(AList.shape[3]):
        A = AList[:,:, i, j]
        e, _ = LA.eig(A)
        eVals[i,j] = e

Z0 = np.real(eVals[:, :, 0])
Z1 = np.real(eVals[:, :, 1])
Z2 = np.real(eVals[:, :, 2])

## Plotting
fig = plt.figure(figsize=(7.27, 8), constrained_layout=True)
gs = gridspec.GridSpec(2, 3, width_ratios=[1, 1, 1], height_ratios=[1, 1])
axes = [
    fig.add_subplot(gs[0, 0]),
    fig.add_subplot(gs[0, 1]),
    fig.add_subplot(gs[0, 2]),
    fig.add_subplot(gs[1, :]),
]

N = 30
levels = np.linspace(-N, N, 301)

contourPlot0 = axes[0].contourf(X, Y, Z0, levels=levels, cmap='seismic', extend='both')
contourPlot1 = axes[1].contourf(X, Y, Z1, levels=levels, cmap='seismic', extend='both')
contourPlot2 = axes[2].contourf(X, Y, Z2, levels=levels, cmap='seismic', extend='both')


cBar = fig.colorbar(contourPlot0, ax=axes[:3], orientation='horizontal', pad=0.2)

## Setting labels
cBar.set_label(r"$\mathfrak{R} \{\varepsilon \}$")
cBar.set_ticks(np.linspace(-N, N, 9))

axes[0].set_xlabel(r"$\mathfrak{R} \{ \tilde{f} \}$")
axes[0].set_ylabel(r"$\mathfrak{I} \{ \tilde{f} \}$")

axes[1].set_xlabel(r"$\mathfrak{R} \{ \tilde{f} \}$")
axes[1].set_ylabel(r"$\mathfrak{I} \{ \tilde{f} \}$")

axes[2].set_xlabel(r"$\mathfrak{R} \{ \tilde{f} \}$")
axes[2].set_ylabel(r"$\mathfrak{I} \{ \tilde{f} \}$")

axes[0].text(0.15, 0.18, r"\textbf{a}", fontsize=20)
axes[1].text(0.15, 0.18, r"\textbf{b}", fontsize=20)
axes[2].text(0.15, 0.18, r"\textbf{c}", fontsize=20)


## Showing / saving the plot
#plt.show()
contourPlot0.set_edgecolors('face')
contourPlot1.set_edgecolors('face')
contourPlot2.set_edgecolors('face')
#plt.savefig("../Bachelor_Thesis/figures/eigenvaluesSecondMomenta.pdf", dpi=300)
#plt.close(fig)


## Checking how many are negative / positive
#fig, axes = plt.subplots(1,1, layout='compressed')
#fig.set_size_inches(7.27, 4)

#ZPos = (np.sign(Z0) +1)/2 + (np.sign(Z1) +1)/2  +(np.sign(Z2) +1)/2 
ZNeg = -(np.sign(Z0) -1)/2 - (np.sign(Z1) -1)/2  -(np.sign(Z2) -1)/2

#contourPlotPos = axes[0].contourf(X, Y, ZPos, levels=[-0.5, 0.5, 1.5, 2.5, 3.5], cmap='magma')
contourPlotNeg = axes[3].contourf(X, Y, ZNeg, levels=[-0.5, 0.5, 1.5, 2.5, 3.5], cmap='summer')
cBar = fig.colorbar(contourPlotNeg, ax=axes[3], orientation='vertical')

## Setting labels
cBar.set_label(r"Number of $\varepsilon_i < 0$")
cBar.set_ticks([0, 1, 2, 3])

axes[3].set_xlabel(r"$\mathfrak{R} \{ \tilde{f} \}$")
axes[3].set_ylabel(r"$\mathfrak{I} \{ \tilde{f} \}$")


plt.show()
