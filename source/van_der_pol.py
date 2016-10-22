"""Van der Pol Oscillator

This script solves Van der Pol Oscillator equations for specified
values and generates two graphs for th same.

How to Use?
-----------
python3 van_der_pol.py

Specifiy Parameters
-------------------
Parameters can be specified in Parameters section of this files

eg. mu = 1.0
    X0 = [1.0, 2.0]

Output
------
Two files as following will be created in the same directory as script:

vanderpol-1.png --> x vs. t, y vs. t
vanderpol-2.png --> y vs.x
"""


# Include Required Libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# Parameters
mu = 1.0
X0 = [1.0, 2.0]


# Function for set of Van der Pol Equations
def vanderpol(X, t, mu=mu):
    """This is the the function for Van der Pol Differential Equations

    Args
    ----
    mu : float
        Value of mu in Van der Pol Equations

    Returns
    -------
    array([dxdt, dydt]): numpy array
        Rate of Change of x and y wrt time as array of floats
    """
    x = X[0]
    y = X[1]
    dxdt = y
    dydt = mu * (1.0 - x**2) * y - x
    return np.array([dxdt, dydt])


# Function to solve Van der Pol Equations
def solve(X0, tstart=0, tend=20, tnum=500):
    """Solves Van der Pol Differential Equations

    Args
    ----
    X0 : list, float
        Value of initial condition for each equation as list of floats
    tstart : int, optional
        Start time of solution as int
        Default is 0
    tend : int, optional
        Stop time for solution as int
        Default is 20
    tnum : int, optional
        Total number of points to consider in between tstart and tend
        while solving
        Default is 500

    Returns
    -------
    [x, y, t] : list, float
        x, y, and t as lists of float
    """
    t = np.linspace(tstart, tend, tnum)
    sol = odeint(vanderpol, X0, t)
    x = sol[:, 0]
    y = sol[:, 1]
    return [x, y, t]


# Function to plot Solution
def SolutionPlot(x, y, t):
    """Plots the solution and saves it to vanderpol-1.png

    Args
    ----
    x : list, float
        List of floating point values of x from the solution of
        Van der Pol Equations
    y : list, float
        List of floating point values of y from the solution of
        Van der Pol Equations
    t : list, float
        List of time values used in the solution of Van der Pol
        Equations

    Returns
    -------
    fig : figure object
        Figure object used when plotting
    """
    fig = plt.figure(1)
    plt.clf()
    line1, = plt.plot(t[::5], x[::5], '+-', label='x', linewidth=1,
                      markersize=4, markeredgewidth=2)
    line2, = plt.plot(t[::5], y[::5], 'D-', label='y', linewidth=2,
                      markersize=3, markeredgewidth=1)
    plt.title('States vs. Time', fontname='serif', fontsize=14)
    plt.xlabel('Time', fontname='serif', fontsize=12)
    plt.xticks(range(0, 21)[::2], family='serif', fontsize=12)
    plt.ylabel('States', fontname='serif', fontsize=12)
    plt.yticks(family='serif', fontsize=12)
    plt.legend(prop={'family': 'serif', 'size': 12})
    plt.savefig('vanderpol-1.png')
    return fig


# Function to plot Phase Portrait
def PhasePlot(x, y):
    """Plots the phase plot of solution and saves it to vanderpol-2.png

    Args
    ----
    x : list, float
        List of floating point values of x from the solution of
        Van der Pol Equations
    y : list, float
        List of floating point values of y from the solution of
        Van der Pol Equations

    Returns
    -------
    fig : figure object
        Figure object used when plotting
    """
    fig = plt.figure(2)
    plt.clf()
    plt.grid(True)
    plt.plot(x, y, linewidth=2, label='Phase Portrait')
    plt.title('Phase Portrait', fontname='serif', fontsize=14)
    plt.xlabel('x', fontname='serif', fontsize=12)
    plt.ylabel('y', fontname='serif', fontsize=12)
    plt.savefig('vanderpol-2.png')
    return fig

if __name__ == '__main__':
    # Export Parameters to a txt file
    with open('getparams.txt', 'w') as getparams:
        getparams.write('\\newcommand{\getmu}{' + str(mu) + '}\n')
        getparams.write('\\newcommand{\getinitial}{' + str(X0) + '}\n')

    # Main Processing
    [x, y, t] = solve(X0)
    SolutionPlot(x, y, t)
    PhasePlot(x, y)
