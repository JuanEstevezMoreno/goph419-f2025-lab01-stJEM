import numpy as np
import matplotlib.pyplot as plt
from goph419lab01.functions import launch_angle_range

def main():
    alphas = np.linspace(0.01, 1.0, 50)
    min_angles = []
    max_angles = []

    for a in alphas:
        phi_range = launch_angle_range(2.0, a, 0.04)
        min_angles.append(phi_range[0])
        max_angles.append(phi_range[1])

    plt.plot(alphas, min_angles, label="Min launch angle")
    plt.plot(alphas, max_angles, label="Max lanuch angle")
    plt.xlabel("⍺ (altitude ratio)")
    plt.ylabel("Launch angle (rad)")
    plt.legend()
    plt.savefig("../figures/launch_angle_vs_alpha.png")

if __name__ == "__main__":
    main()
    