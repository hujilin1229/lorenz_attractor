# PhD-Python-1
A repository containing a mini project template for the 
course "Scientific Computing using Python, part 1", held 
at Aalborg University, May 2016

#  
Here you can put a bit of information/documentation of the program 
you develop, including:

- Author: Jilin Hu

- What does the program?
  This program is used to solve ODE, file writting and reading, and
  trajectory plotting. 
  
- Files and dir structure
    ./
    doc
    results
    test
    LICENSE
    README.md
    setup.py
    ./cases/
            __init__.py
            context.py
            case1.py
            case2.py
            case3.py
            case4.py
            case5.py
    ./lorenz/
            __init__.py
            filehandling.py
            plot.py
            run.py
            solver.py
            util.py
    ./test/
            __init__.py
            context.py
            test_basic.py
- How to run the program
    $cd cases
    $python
    >>import sys
    >>sys.path.append('../')
    >>exec(open("case1.py").read())
    
    or 
    $cd cases
    $ipython
    []:import sys
    []:sys.path.append('../')
    []:%run case1.py
# 
you might need to put something like


in e.g. cases/case1.py or test/test.py to be access the functions etc.
you make in lorenz/solver.py, lorenz/run.py etc.# lorenz_attractor
