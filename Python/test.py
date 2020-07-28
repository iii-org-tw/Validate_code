from numpy import quantile
# from weighted_quantile import quantile
import numpy as np

from  itertools import permutations
import pickle
import numpy as np

from  itertools import permutations
import pickle

def add_sample(a, out=None,overwrite_input=False,keepdims=False):
    interpolation_list = ['lower','higher','midpoint','nearest','linear']
    q = np.random.rand(1)[0]
    w = np.ones(len(a))
    for interpolation in interpolation_list:
        d ={'a':a,
            'q':q,
            'w':w,
            'out':out,
            'overwrite_input':overwrite_input,
            'interpolation':interpolation,
            'keepdims':keepdims}
    return d

def check_equal(param_list,error_samples):
    f = True
    for param_dict in param_list:
        a = param_dict['a']
        q = param_dict['q']
        w = param_dict['w']
        out = param_dict['out']
        overwrite_input = param_dict['overwrite_input']
        interpolation = param_dict['interpolation']
        keepdims = param_dict['keepdims']
        
        result_a = quantile(a, q, w=w, out=out, overwrite_input=overwrite_input, interpolation=interpolation, keepdims=keepdims)
        result_b = quantile(a, q, out=out, overwrite_input=overwrite_input, interpolation=interpolation, keepdims=keepdims)
        if not np.allclose(result_a,result_b,equal_nan=True):
            error_samples.append(param_dict)
            print("Error occurs!")
            print("result_a",result_a)
            print("result_b",result_b)
            f = False
    if f:
        print("Pass!")


if __name__=="__main__":
    f = open('../data/HIGGS.csv', 'r')
    a = 0
    test_samples = []
    for line in f:
        line = np.array([float(dx) for dx in line.split(',')])
        test_samples.append(line)
        a += 1
        if a > 100000:
        # print(line)
            processed_samples = []
            for test_sample in test_samples:
                processed_samples.append(add_sample(test_sample))
            error_samples = []
            check_equal(processed_samples,error_samples)
            a = 0
            test_samples = []