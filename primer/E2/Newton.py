def Newton(f, x, dfdx, epsilon=1.0E-7, N=100, store=False):
    """Newton's method:
        x(n) = x(n-1) - f(x(n-1))/f'(x(n-1))
    
    epsilon: error
    N: max. iteration
    Caution: only works for scalar equations only
    """
    f_value = f(x)
    n = 0
    if store: info = [(x, f_value)]             # Storing soln into info
    while abs(f_value) > epsilon and n <= N:
        dfdx_value = float(dfdx(x))
        if abs(dfdx_value) < 1E-14:
            raise ValueError("Newton: f'(%g)% = %g" % (x, dfdx_value))
        
        # Newton's method
        x = x - f_value/dfdx_value
        
        n += 1
        f_value = f(x)                          # Update
        if store: info.append((x, f_value))     # Storing soln into info
    if store:
        return x, info
    else:
        return x, n, f_value
    