import numpy as np

def compute_iteration(x_min, x_max, y_min, y_max, max_iter):
    """
    This function computes the iteration requested in question 1 of assignment 3
    
    Parameters:
    x_min -- float or integer value defining the minimum x value of the 
    complex plane c
    x_max -- float or integer value defining the maximum x value of the 
    complex plane c
    y_min -- float or integer value defining the minimum y value of the 
    complex plane c
    y_max -- float or integer value defining the maximum y value of the 
    complex plane c
    max_iter -- integer value that represents that maximum iterations to run
    
    Returns:
    diverg_steps -- 2D array showing the iteration count when a point diverged
    bdd_mask -- 2D boolean array which shows True if the point stays bounded
    """
    # Set up the complex plane 
    x = np.linspace(x_min, x_max, 500) # Increase 500 for higher quality resolution
    y = np.linspace(y_min, y_max, 500)
    X, Y = np.meshgrid(x, y)
    c = X + 1j * Y
    
    z = np.zeros_like(c)
    diverg_steps = np.zeros(z.shape, dtype=int)
    bdd_mask = np.full(z.shape, True, dtype=bool) 
    
    # Iteration
    for i in range(max_iter):
        z[bdd_mask] = z[bdd_mask] ** 2 + c[bdd_mask]
        div = np.abs(z) > 2
        esc = div & bdd_mask
        diverg_steps[esc] = i
        bdd_mask[div] = False 
    
    return diverg_steps, bdd_mask