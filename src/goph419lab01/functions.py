import math
import numpy as np

def sqrt(x, rtol=1e^-9, atol=0.0, max_terms=200):
    """
    Positive square root using a binomial/Taylor series about a chosen base 'a'.
    Valid for 0.0 <= x <= 2.5
    """
    if not (0.0 <= x <= 2.5):
        raise ValueError("sqrt(x): x must be in [0.0, 2.5.]")
    if x == 0.0:
        return 0.0
    if x == 1.0:
        return 1.0
    
    #Choose base a to keep |(x-a)/a| <= ~0.5 for fast convergence
    candidates = np.array([0.5, 1.0, 1.5, 2.0])
    a = float(candidates[np.argmin(np.abs(candidates - x))])

    t = (x-a)/a     # expansion variable
    root_a = math.sqrt(a)   
    c = 1.0
    term = root_a * c
    s = term

    for n in range (1, max_terms + 1):
        c *= (0.5 - (n-1)) / n
        term = root_a * c * (t ** n)
        s_new = s + term
        if abs (s_new - s) <= max(atol, rtol * abs(s_new)):
            return s_new
        s = s_new

    # Should converge by here
    raise RuntimeError("sqrt series did not converge within max_terms.")

def arcsin(x, rtol=1e-9, atol=0.0, max_terms=10000):
    """
    arcsin(x) using power series on [0,1]
    Raises ValueError is x not in [0,1]
    """
    if not (0.0 <= x <= 1.0):
        raise ValueError("arcsin(x) must be in [0.0, 1.0].")
    
    if x == 0.0:
        return 0.0
    if x == 1.0:
        return math.pi/2.0
    
    x2 = x * x
    # k=0
    a_k = 1.0 #a0 = 1
    term = a_k * x
    s = term

    for k in range(0, max_terms):
        # Update coefficient a_{k+1} from a_k:
        num = (2*k +1)
        a_k *= (num / (2**(k+1)))**2 * (num / (2*k + 3))

        # Next term uses x^{2(k+1)+1} = x^{2k+3} + (x^{2k+1})*x^2
        term *= x2
        next_term = a_k * term # now equals a_{k+1} * x^2{(k+1)+1}
        s_new = s + next_term
        if abs(s_new -s) <= max(atol, rtol * abs(s_new)):
            return s_new
        s = s_new

    raise RuntimeError("arcsin series did not converge within max_terms")

def launch_angle(ve_v0, alpha):
    """Single launch angle from Eq.(17)."""
    #compute RHS of eq(17) then use arcsin()
    return None #placeholder

def launch_angle_range (ve_v0, alpha, tol_alpha):
    """Min and max allowable launch angles."""
    return np.array([None, None])