"""
This file could contain the necessary calls to make plots etc for 
case 2

"""
from cases.context import lorenz

def run_case2():
    sigma = 10
    beta = 8 / 3
    rho = 16
    initial_array = [0.1, 0.1, 1]
    print("Now run the lorenz solver by giving an initial array {}".format(initial_array))
    t_file = lorenz.run.run_save_plot(sigma, beta, rho, initial_arrays=initial_array)
    print("Now run the lorenz plot by give the data file.")
    lorenz.run_load_plot(target_file=t_file, sigma=sigma, beta=beta, rho=rho)


if __name__ == '__main__':
    run_case2()