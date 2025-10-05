import numpy as np
from goph419lab01.functions import sqrt, arcsin, launch_angle_range

def test_sqrt():
    x = 2.0
    expected = np.sqrt(x)
    actual = sqrt (x)
    print ("sqrt test:", np.isclose(expected, actual, atol=1e-8))

def test_arcsin():
    x = 0.5
    expected = np.arcsin(x)
    actual = arcsin(x)
    print ("arcsin test:", np.isclose(expected, actual, atol=1e-8))

def test_launch_angle_range():
    phi = launch_angle_range(2.0, 0.25, 0.02)
    print ("launch_angle_range:", phi)

if __name__ == "__main__":
    test_sqrt()
    test_arcsin()
    test_launch_angle_range()

