Problem Statement
============

This mini-project relates to the Lorenz attractor. In this process, we need to solve the Ordinary Differential Equations
(ODEs), write and read the data, and plot the data. By looking this problem, we can divide this problem into following steps.

ODE Solver
-----------

In this part, we construct a class named "ODE_solvers". In this class, there's a initial function which is used to
specify sigma, beta, rho of the ODE and these three parameters are the attributes of this class. Moreover, we also
define a function named "Euler_solve" which adopts Euler approach to solve this ODE by giving the initial conditions
corresponding to values for (x[0], y[0], z[0]), time interval and number of steps. Of course, you can added some more
advanced and accurate solve methods into this class, but here we just implement the Euler one to show how it works.

Filehandling
---------------------------

In this part, we implement a module named "filehandling" to take over the task of writing(reading)the trajectory from
"Euler_solve" into(out) file.

Plotting
---------------------------

In this part, we implement a module named "plot" which can plot a 3D and 2D of the trajectory

Running
---------------------------

This is a integrated module, which integrate the solver, file writing and reading, and plotting. There are two methods
in this module, "run_save_plot" and "run_load_plot". When you call "run_save_plot", it will automatically solving the
ODE, saving the data into file and plot the trajectory. Otherwise, you can call "run_load_plot", it will load the data
from the file you specified and plot the trajectory.

Testing
---------------------------

Here we conduct unit test for the functions mentioned above. All of these functions passed the unit test.