import math

def calc_f1_score ( tp , fp , fn ):
    if isinstance(tp, int) == 0:
        print('tp must be int')
        return
    elif isinstance(fp, int) == 0:
        print('fp must be int')
        return
    elif isinstance(fn, int) == 0:
        print('fn must be int')
        return
    elif tp <= 0 or fp <= 0 or fn <=0:
        print('tp and fp and fn must be greater than zero')
        return
    else:
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
        f1 = 2 * (precision * recall) / (precision + recall)
        print('precision is ', precision)
        print('recall is ', recall)
        print('f1-score is ', f1)
 





