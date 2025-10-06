import os
import numpy as np
import matplotlib.pyplot as plt
from goph419lab01.functions import launch_angle_range

def plot_vs_alpha():
    """Hold ve_v0=2.0; vary alpha; tol_alpha=0.04."""
    ve_v0 = 2.0
    tol_alpha = 0.04
    alphas = np.linspace(0.001, 1.0, 200)

    phi_min_deg, phi_max_deg = [], []

    for a in alphas:
        try:
            phi_min, phi_max = launch_angle_range(ve_v0, a, tol_alpha)
            phi_min_deg.append(np.degrees(phi_min))
            phi_max_deg.append(np.degrees(phi_max))
        except ValueError:
            # No real solution at this alpha
            phi_min_deg.append(np.nan)
            phi_max_deg.append(np.nan)

    plt.figure()
    plt.plot(alphas, phi_min_deg, label="Min launch angle")
    plt.plot(alphas, phi_max_deg, label="Max launch angle")
    plt.xlabel(r"$\alpha$  (altitude ratio)")
    plt.ylabel("Launch angle (degrees)")
    plt.title(rf"Launch angle range vs $\alpha$  (ve/v0={ve_v0}, tol={tol_alpha})")
    plt.legend()
    plt.grid(True, alpha=0.3)
    os.makedirs("figures", exist_ok=True)
    plt.savefig("figures/launch_angle_vs_alpha.png", dpi=200, bbox_inches="tight")
    plt.close()

def plot_vs_vev0():
    """Hold alpha=0.25; vary ve_v0; tol_alpha=0.04."""
    alpha = 0.25
    tol_alpha = 0.04
    ve_v0_vals = np.linspace(1.05, 3.0, 200)

    phi_min_deg, phi_max_deg = [], []

    for r in ve_v0_vals:
        try:
            phi_min, phi_max = launch_angle_range(r, alpha, tol_alpha)
            phi_min_deg.append(np.degrees(phi_min))
            phi_max_deg.append(np.degrees(phi_max))
        except ValueError:
            phi_min_deg.append(np.nan)
            phi_max_deg.append(np.nan)

    plt.figure()
    plt.plot(ve_v0_vals, phi_min_deg, label="Min launch angle")
    plt.plot(ve_v0_vals, phi_max_deg, label="Max launch angle")
    plt.xlabel(r"$v_e/v_0$")
    plt.ylabel("Launch angle (degrees)")
    plt.title(rf"Launch angle range vs $v_e/v_0$  (alpha={alpha}, tol={tol_alpha})")
    plt.legend()
    plt.grid(True, alpha=0.3)
    os.makedirs("figures", exist_ok=True)
    plt.savefig("figures/launch_angle_vs_vev0.png", dpi=200, bbox_inches="tight")
    plt.close()

def main():
    plot_vs_alpha()
    plot_vs_vev0()

if __name__ == "__main__":
    main()