import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

# Use LaTeX and serif font
plt.rc('font', **{'family': 'serif', 'serif': ['Computer Modern'], 'size': 20})
plt.rc('text.latex', preamble=r'\usepackage{amssymb}')
plt.rcParams['text.usetex'] = True

## defining functions
def eigenvaluePos(ref, imf, Q):
    root = np.emath.sqrt(imf**2 - 2*np.sqrt(2) * ref - 2)
    return (1 / np.sqrt(2)) * (root - imf - 1/(Q*np.sqrt(2)))

def eigenvalueNeg(ref, imf, Q):
    root = np.emath.sqrt(imf**2 - 2*np.sqrt(2) * ref - 2)
    return (1 / np.sqrt(2)) * (-root - imf - 1/(Q*np.sqrt(2)))

def parabolaRef(imf):
    quadratic = imf**2 /(2 * np.sqrt(2))
    return quadratic - 1 / np.sqrt(2)

## defiining constants
Q = 10

## Plotting

fig, axes = plt.subplots(1, 2, layout='compressed')
fig.set_size_inches(7.27, 4)

ref = np.linspace(-2, 2, 300)
imf = np.linspace(-2, 2, 300)
X, Y = np.meshgrid(ref, imf)
ZNeg = np.real(eigenvalueNeg(X, Y, Q))
ZPos = np.real(eigenvaluePos(X, Y, Q))
parabola = parabolaRef(imf)


N = 3
levels = np.linspace(-N, N, 301)

cNeg = axes[0].contourf(X, Y, ZNeg, levels=levels, cmap='seismic', extend='both')

axes[0].plot(parabola, ref, color='black')
axes[1].plot(parabola, ref, color='black')
#axes[1].plot(slope, imf, color='black')
#axes[0].scatter(-1/np.sqrt(2), -gamma/(np.sqrt(8)), color='black', marker='o' )

cPos = axes[1].contourf(X, Y, ZPos, levels=levels, cmap='seismic', extend='both')

cBar = fig.colorbar(cNeg, ax=axes, orientation='horizontal')

## setting labels
axes[0].set_xlabel(r"$\mathfrak{R} \{ \tilde{f} \}$")
axes[0].set_ylabel(r"$\mathfrak{I} \{ \tilde{f} \}$")

axes[1].set_xlabel(r"$\mathfrak{R} \{ \tilde{f} \}$")
axes[1].set_ylabel(r"$\mathfrak{I} \{ \tilde{f} \}$")

cBar.set_label(r"$\mathfrak{R} \{\varepsilon_\pm / \omega \}$")
cBar.set_ticks(np.linspace(-N, N, 9))

axes[0].text(1.5, -1.5, r"\textbf{a}", fontsize=20)
axes[1].text(1.5, -1.5, r"\textbf{b}", fontsize=20)


## Showing / Saving
#plt.show()
#cNeg.set_edgecolor('face')
#cPos.set_edgecolor('face')
cNeg.set_rasterized(True)
cPos.set_rasterized(True)
plt.savefig("../Presentation/Stability.pdf", dpi=300)