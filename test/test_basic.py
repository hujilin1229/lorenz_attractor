"""
In this file you may have your tests


"""
from test.context import lorenz

import unittest
import numpy as np

class TestSuite(unittest.TestCase):
    """
    This is a unit test for the module lorenz
    """
    def test_solver(self):
        sigma = 1
        beta = 1
        rho = 1
        test_solver = lorenz.ODE_solvers(sigma=sigma, beta= beta, rho=rho)
        out_array = np.array([[1, 2, 3], [2, -2, 2], [-2, -2, -4]]).transpose()
        self.assertEqual(test_solver.Euler_solve(initial_arrays=[1, 2, 3], N=3, t_sigma=1).tolist(),
                         out_array.tolist())
        self.assertEqual(test_solver.Euler_solve(initial_arrays=[1,1]), False)
        self.assertEqual(test_solver.Euler_solve(initial_arrays=[1,1,1], N = 0), False)
        self.assertEqual(test_solver.Euler_solve(initial_arrays=[1,1,1], N = -1), False)
        self.assertEqual(test_solver.Euler_solve(initial_arrays=[1,1,1], t_sigma=-1), False)
        self.assertEqual(test_solver.Euler_solve(initial_arrays=[1,1,1],t_sigma=0), False)

    def test_filehandling(self):
        #Check the file intend to be opened not exist
        self.assertEqual(lorenz.filehandling.read_x_y_z_fromfile(filename=""), False)

    def test_plot(self):
        #Check the input for plot is None
        self.assertEqual(lorenz.plot.plot2Dpdf(y=[1,2], z=[2,3]), False)
        self.assertEqual(lorenz.plot.plot2Dpdf(x=[1,2], z=[2,3]), False)
        self.assertEqual(lorenz.plot.plot2Dpdf(y=[1,2], x=[2,3]), False)
        self.assertEqual(lorenz.plot.plot2Dpdf(x=[1,2,3], y=[1,2,3], z=[1,2]), False)
        self.assertEqual(lorenz.plot.plot2Dpdf(z=[1,2,3], y=[1,2,3], x=[1,2]), False)
        self.assertEqual(lorenz.plot.plot2Dpdf(x=[1,2,3], z=[1,2,3], y=[1,2]), False)
        self.assertEqual(lorenz.plot.plot3Dpdf(y=[1,2], z=[2,3]), False)
        self.assertEqual(lorenz.plot.plot3Dpdf(x=[1,2], z=[2,3]), False)
        self.assertEqual(lorenz.plot.plot3Dpdf(y=[1,2], x=[2,3]), False)
        self.assertEqual(lorenz.plot.plot3Dpdf(x=[1,2,3], y=[1,2,3], z=[1,2]), False)
        self.assertEqual(lorenz.plot.plot3Dpdf(z=[1,2,3], y=[1,2,3], x=[1,2]), False)
        self.assertEqual(lorenz.plot.plot3Dpdf(x=[1,2,3], z=[1,2,3], y=[1,2]), False)


if __name__ == '__main__':
    unittest.main()
