"""
This file can contain functionalities for saving/loading data

"""
import pickle

def write_x_y_z_tofile(var, filename):
    """Write the arrays of x, y, z to a file

    :param var: x, y, z 
    :param filename: the target filename
    :returns: None
    :rtype: None

    """
    write_file = open(filename, 'wb')
    pickle.dump(var, write_file)
    write_file.flush()
    write_file.close()


def read_x_y_z_fromfile(filename):
    """read x y z from file: filename

    :param filename: The file which we want to read from
    :returns: three arrays: x, y, z
    :rtype: numpy.arrays

    """
    try:
        read_file = open(filename, 'rb')
    except IOError:
        print("cannot open this file")
        return False
    else:
        var = pickle.load(read_file)
        read_file.close()
        return var
