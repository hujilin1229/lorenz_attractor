"""
This file may contain functionalities for plotting

"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from . import util

def plot3Dpdf(x=None, y=None, z=None, sigma=10, beta=2.67, rho=6):
    """
    Plot the 3D scatter of lorenz

    :param x: x-axis data
    :param y: y-axis data
    :param z: z-axis data
    :param sigma: param sigma for lorenz
    :param beta: param beta for lorenz
    :param rho: param rho for lorenz
    :return: bool

    """
    if x is None or y is None or z is None:
        print("In plot.plot3Dpdf none of these should be None ")
        return False
    if len(x) != len(y) or len(y) != len(z) or len(x) !=len(z):
        print("The length for x, y, z should be the same!")
        return False
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    # Calculate the Euclidian distance from one time step n to the next n+1
    t = np.zeros(len(x))
    t[1:] = np.sqrt((x[1:] - x[:-1])**2 + (y[1:] - y[:-1])**2 + (z[1:] - z[:-1])**2)
    ax.scatter3D(x, y, z, c=t)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("3D plot of Lorenz")
    plt.savefig(
        "../results/3D_plot_s{0}_b{1}_r{2}.jpg".format(sigma, round(beta,2), rho))
    plt.show()
    return True


def plot2Dpdf(x=None, y=None, z=None, sigma=10, beta=2.67, rho=6):
    """
    Plot 3*1 subplots of 2D plot for lorenz

    :param x: x-axis data
    :param y: y-axis data
    :param z: z-axis data
    :param sigma: param sigma for lorenz
    :param beta: param beta for lorenz
    :param rho: param rho for lorenz
    :return: bool

    """
    if x is None or y is None or z is None:
        print("In plot.plot2Dpdf none of these should be None ")
        return False
    if len(x) != len(y) or len(y) != len(z) or len(x) !=len(z):
        print("The length for x, y, z should be the same!")
        return False
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    t = np.zeros(len(y))
    t[1:] = np.sqrt(((y[1:] - y[:-1])**2 + (z[1:] - z[:-1])**2))
    ax1.scatter(y, z, c=t)
    ax1.set_xlabel("Y")
    ax1.set_ylabel("Z")
    ax1.set_title("2D Y-Z plot of Lorenz")


    t = np.zeros(len(x))
    t[1:] = np.sqrt(((x[1:] - x[:-1])**2 + (z[1:] - z[:-1])**2))
    ax2.scatter(x, z, c=t)
    ax2.set_xlabel("X")
    ax2.set_ylabel("Z")
    ax2.set_title("2D X-Z plot of Lorenz")


    t = np.zeros(len(x))
    t[1:] = np.sqrt(((x[1:] - x[:-1])**2 + (y[1:] - y[:-1])**2))
    ax3.scatter(x, z, c=t)
    ax3.set_xlabel("X")
    ax3.set_ylabel("Y")
    ax3.set_title("2D X-Y plot of Lorenz")
    plt.savefig(
        "../results/2D_plots_s{0}_b{1}_r{2}.jpg".format(sigma, round(beta,2), rho))

    plt.show()
    return True
