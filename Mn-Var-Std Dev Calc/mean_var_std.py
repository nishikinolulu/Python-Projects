import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        flat_mn = np.mean(list)
        flat_var = np.var(list)
        flat_std = np.std(list)
        flat_max = max(list)
        flat_min = min(list)
        flat_sum = sum(list)
        
        matrix = np.array([list[:3], list[3:6], list[6:]])

        ax1_mn = np.mean(matrix, axis=0)
        ax2_mn = np.mean(matrix, axis=1)
        ax1_var = np.var(matrix, axis=0)
        ax2_var = np.var(matrix, axis=1)
        ax1_std = np.std(matrix, axis=0)
        ax2_std = np.std(matrix, axis=1)
        ax1_max = np.max(matrix, axis=0)
        ax2_max = np.max(matrix, axis=1)
        ax1_min = np.min(matrix, axis=0)
        ax2_min = np.min(matrix, axis=1)
        ax1_sum = np.sum(matrix, axis=0)
        ax2_sum = np.sum(matrix, axis=1)

        calc_dict = {   "mean" : [ax1_mn.tolist(), ax2_mn.tolist(), flat_mn],
                        "variance" : [ax1_var.tolist(), ax2_var.tolist(), flat_var],
                        "standard deviation" : [ax1_std.tolist(), ax2_std.tolist(), flat_std],
                        "max" : [ax1_max.tolist(), ax2_max.tolist(), flat_max],
                        "min" : [ax1_min.tolist(), ax2_min.tolist(), flat_min],
                        "sum" : [ax1_sum.tolist(), ax2_sum.tolist(), flat_sum]
                    }

    return calc_dict