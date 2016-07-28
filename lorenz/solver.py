"""
This file may contain the ODE solver

"""
import numpy as np


class ODE_solvers(object):
    """
    An integrated ODE solvers
    By giving the initial parameters, we can construct the ODE solver

    Example:
        solver = ODE_solver(sigma, beta, rho)
    """

    def __init__(self, sigma, beta, rho):
        """return a ODE_solvers object whose three parameters are given 

        :param sigma: sigma param in ODE function
        :param beta: beta param in ODE function
        :param rho: rho param in ODE function
        :returns: None
        :rtype: None
        """
        self.sigma = sigma
        self.beta = beta
        self.rho = rho

    def Euler_solve(self, initial_arrays, N=50000, t_sigma=0.01):
        """Solve the equation with Euler approach

        :param initial_arrays: list of initial values for x[0], y[0], z[0] 
        :param N: the total steps to calculate the equation
        :param t_sigma: the minimal step
        :returns: arrays of [x, y, z], size(3*n)
        :rtype: numpy.arrays

        """
        if len(initial_arrays) < 3:
            print("The length of initial array should be 3!")
            return False
        if t_sigma <= 0:
            print("The time step t_sigma cannot be smaller than zero!")
            return False
        if N <= 0:
            print("The total steps cannot be smaller than zero!")
            return False
        r_arrays = np.zeros((3, N))
        # initialize with the given results
        r_arrays[:, 0] = initial_arrays
        num_ind = 1
        while num_ind < N:
            r_arrays[0, num_ind] = self.sigma * (r_arrays[1, num_ind - 1] - r_arrays[
                                                 0, num_ind - 1]) * t_sigma + r_arrays[0, num_ind - 1]
            r_arrays[1, num_ind] = t_sigma * (r_arrays[0, num_ind - 1] * (self.rho - r_arrays[
                                              2, num_ind - 1]) - r_arrays[1, num_ind - 1]) + r_arrays[1, num_ind - 1]
            r_arrays[2, num_ind] = t_sigma * (r_arrays[0, num_ind - 1] * r_arrays[
                                              1, num_ind - 1] - self.beta * r_arrays[2, num_ind - 1]) \
                                   + r_arrays[2, num_ind - 1]
            num_ind += 1

        return r_arrays
