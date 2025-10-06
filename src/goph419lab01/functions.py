import math
import numpy as np

def sqrt(x, rtol=1e-9, atol=0.0, max_terms=200):
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

def arcsin(x, rtol=1e-12, atol=0.0, max_terms=10000):
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
    
    s = 0.0
    term = x    #x^(2k+1)
    a_k = 1.0   #coefficient a_0
    s += a_k * term

    for k in range(0, max_terms):
        # recurrence for a_{k+1}/a_k
        ratio = ((2*k + 1)**2 / (2.0 * (k + 1) * (2*k +3)))
        a_k *= ratio
        term *= x*x 
        s_new = s + a_k * term
        if abs(s_new - s) <= rtol * abs(s_new):
            return s_new
        s = s_new

    raise RuntimeError("arcsin series did not converge within max_terms")

def _rhs_sin_phi0(ve_v0: float, alpha: float) -> float:
    """
    Cumpute RHS of Eq. 17: sin(phi0) = (1+alpha) * sqrt(1 - (ve/v0)^2 * alpha/(1+alpha))
    """
    if ve_v0 <= 0:
        raise ValueError("ve_v0 must be positive.")
    if alpha < 0:
        raise ValueError ("alpha must be non-negative.")
    
    one_pa = 1.0 + alpha
    inner = 1.0 - (ve_v0 *ve_v0) * (alpha / one_pa)

    if inner < 0.0:
        # No real solution, target altitude too large for given ve/v0
        raise ValueError ("No real launch angle: Expression under sqrt is negative")
    s = one_pa * sqrt(inner) 
    if s < 0.0 or s > 1.0:
        # Physically invalid
        raise ValueError ("No real launch angle: sin(phi0) outside [0,1].")
    return s

def launch_angle(ve_v0: float, alpha: float) -> float:
    """
    Single launch angle from Eq.(17).
    """
    s = _rhs_sin_phi0(ve_v0, alpha)
    return arcsin(s)

def launch_angle_range (ve_v0: float, alpha: float, tol_alpha: float) -> np.ndarray:
    """
    Returns [phi_min, phi_max] in radians. 
    Per lab spec:
    - phi_min corresponds to max altitude (1 + tol_alpha)*alpha
    - phi_max corresponds to min altitude (1 - tol_alpha)*alpha
    """
    if tol_alpha < 0:
        raise ValueError("tol_alpha must be non-negative")
    
    alpha_hi = alpha * (1.0 + tol_alpha) #higher target
    alpha_lo = alpha * (1.0 - tol_alpha) #lower target
    if alpha_lo < 0.0:
        raise ValueError("alpha*(1- tol_alpha) became negative; check inputs.")
    
    # Compute sin(phi) at bounds, then arcsin
    s_hi = _rhs_sin_phi0(ve_v0, alpha_hi)
    s_lo = _rhs_sin_phi0(ve_v0, alpha_lo)

    phi_min = arcsin(s_hi) #min angle at higher alt
    phi_max = arcsin(s_lo) #max anlge at lower alt

    return np.array([phi_min, phi_max], dtype=float)