"""
This file may contain a convenient interface/function for 

1: computing a trajectory using an ODE solver from solver.py
2: save data to file
3: plot data

and possible another function that

2: load data from file
3: plot data

"""
from . import plot
from . import solver
from . import filehandling


def run_save_plot(sigma, beta, rho, initial_arrays):
    """
    Run Euler_solve, save and plot trajectory

    :param sigma: sigma
    :param beta: beta
    :param rho: rho
    :param initial_arrays: [x[0], y[0], z[0]]
    :returns: the name of saved file.
    :rtype: String
    """

    solver1 = solver.ODE_solvers(sigma=sigma, beta=beta, rho=rho)
    traj_array = solver1.Euler_solve(initial_arrays)
    target_file = "../results/traj_s{0}_b{1}_r{2}.pkl".format(sigma, round(beta, 2), rho)
    filehandling.write_x_y_z_tofile(traj_array, target_file)
    plot.plot3Dpdf(traj_array[0, :], traj_array[1, :], traj_array[
                   2, :], sigma=sigma, beta=beta, rho=rho)
    plot.plot2Dpdf(x=traj_array[0, :], y=traj_array[
                   1, :], z=traj_array[2, :], sigma=sigma, beta=beta, rho=rho)

    return target_file


def run_load_plot(target_file, sigma, beta, rho):
    """
    Read and plot trajectory

    :param target_file: The pickle file contain the traj of x, y, z
    :param sigma: the sigma used for this trajectory
    :param beta: the beta used for this trajectory
    :param rho: the rho used for this trajectory
    :returns: None
    :rtype: None

    """
    traj_array = filehandling.read_x_y_z_fromfile(target_file)
    plot.plot3Dpdf(traj_array[0, :], traj_array[1, :], traj_array[
                   2, :], sigma=sigma, beta=beta, rho=rho)
    plot.plot2Dpdf(x=traj_array[0, :], y=traj_array[
                   1, :], z=traj_array[2, :], sigma=sigma, beta=beta, rho=rho)
