import math

def is_number (n):
    try:
        float (n)
    except ValueError:
        return False
    return True

def calc_sig ( x ) :
 sig = 1 / (1 + math.exp(-x))
 return sig

def calc_relu(x):
  return max(x,0.0)

def calc_elu ( x ) :
  if x <= 0:
    return 0.01 * (math.e ** x - 1)
  else:
    return x

def calc_activation_func(x , act_name):
  if is_number(x) == False:
    print('x must be a number')
    return
  else:
    if act_name == 'sigmoid':
        return calc_sig (x)
    elif act_name == 'relu':
        return calc_relu(x)
    elif act_name == 'elu':
        return calc_elu(x)
    else:
        print(act_name, 'is not supported')
        return