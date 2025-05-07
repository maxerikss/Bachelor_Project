import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

# Use LaTeX and serif font
plt.rc('font', **{'family': 'serif', 'serif': ['Computer Modern'], 'size': 12})
plt.rc('text.latex', preamble=r'\usepackage{amssymb}')
plt.rcParams['text.usetex'] = True

## defining functions
def eigenvaluePos(ref, imf, gamma):
    root = np.emath.sqrt(imf**2 - 2*np.sqrt(2) * ref - 2)
    return (1 / np.sqrt(2)) * (root - imf - gamma/np.sqrt(2))

def eigenvalueNeg(ref, imf, gamma):
    root = np.emath.sqrt(imf**2 - 2*np.sqrt(2) * ref - 2)
    return (1 / np.sqrt(2)) * (-root - imf - gamma/np.sqrt(2))

def parabolaRef(imf):
    quadratic = imf**2 /(2 * np.sqrt(2))
    return quadratic - 1 / np.sqrt(2)

## defiining constants
gamma = 0.2

### Defining colormap
colors = ['red', 'blue']
cmap = mcolors.ListedColormap(colors)
bounds = [-np.inf, 0, np.inf]
norm = mcolors.BoundaryNorm(bounds, cmap.N)

## Plotting

fig, axes = plt.subplots(1, 2, layout='compressed')
fig.set_size_inches(7.27, 4)

ref = np.linspace(-2, 2, 300)
imf = np.linspace(-2, 2, 300)
X, Y = np.meshgrid(ref, imf)
ZNeg = np.real(eigenvalueNeg(X, Y, gamma))
ZPos = np.real(eigenvaluePos(X, Y, gamma))
parabola = parabolaRef(imf)

N = 3
levels = np.linspace(-N, N, 301)

cNeg = axes[0].contourf(X, Y, ZNeg, levels=levels, cmap='seismic')
#cNeg = axes[0].contourf(X, Y, ZNeg, levels=3, cmap=cmap, norm=norm)
axes[0].plot(parabola, ref, color='black')
axes[1].plot(parabola, ref, color='black')
#axes[0].scatter(-1/np.sqrt(2), -gamma/(np.sqrt(8)), color='black', marker='o' )

cPos = axes[1].contourf(X, Y, ZPos, levels=levels, cmap='seismic')

cBar = fig.colorbar(cNeg, ax=axes, orientation='horizontal')

## setting labels
axes[0].set_xlabel(r"$\mathfrak{R} \{ f \}$")
axes[0].set_ylabel(r"$\mathfrak{I} \{ f \}$")

axes[1].set_xlabel(r"$\mathfrak{R} \{ f \}$")
axes[1].set_ylabel(r"$\mathfrak{I} \{ f \}$")

cBar.set_label(r"$\mathfrak{R} \{\lambda_\pm \}$")
cBar.set_ticks(np.linspace(-N, N, 9))

axes[0].text(1.5, -1.5, r"\textbf{a}", fontsize=20)
axes[1].text(1.5, -1.5, r"\textbf{b}", fontsize=20)


plt.savefig("../Bachelor_Thesis/figures/eigenvalueFirstMomenta.pdf")