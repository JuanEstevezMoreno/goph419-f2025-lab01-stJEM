import numpy as np

def sqrt(x):
    if x < 0 or x > 2.5:
        raise ValueError("Input must be between 0 and 2.5")
    # TO DO implement series expansion around chosen base point
    return np.sqrt(x) #placeholder for testing

def arcsin(x):
    if x < 0 or x > 1:
        raise ValueError("Input must be between 0 and 1")
    # TODO: implement series expansion
    return np.arcsin(x) #placeholder for testing 

def launch_angle(ve_v0, alpha):
    """Single launch angle from Eq.(17)"""
    #compute RHS of eq(17) then use arcsin()
    return None #placeholder

def launch_angle_range (ve_v0, alpha, tol_alpha):
    """Min and max allowable launch angles."""
    return np.array([None, None])