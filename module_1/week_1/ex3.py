import random
import math

def mae_loss_func(num_samples):
    n = num_samples
    sum = 0
    for n in range(1,n):
        y = random.uniform(0.0,10.0)
        y_hat = random.uniform(0.0,10.0)
        diff = abs(y - y_hat)
        sum += diff
    sum = sum / n
    return sum

def mse_loss_func(num_samples):
    n = num_samples
    sum = 0
    for n in range(1,n):
        y = random.uniform(0.0,10.0)
        y_hat = random.uniform(0.0,10.0)
        ms = (y - y_hat) ** 2
        sum += ms
    sum = sum / n
    return sum

def rmse_loss_func(num_samples):
    n = num_samples
    result = math.sqrt(mse_loss_func(n))
    return result

def regression_loss_func(num_samples, loss_name):
    n = num_samples
    if n.isnumeric() == False:
        print('Number of samples must be an integer number')
        return
    else:
        n = int(n)
        if loss_name == 'mae':
            return mae_loss_func(n)
        elif loss_name == 'mse':
            return mse_loss_func(n)
        elif loss_name == 'rmse':
            return rmse_loss_func(n)