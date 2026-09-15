import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def adstock_effect(spend, theta=0.5, max_lag=12):
    """Simple geometric adstock transformation.

    Parameters
    ----------
    spend : np.ndarray
        Time series of marketing spend.
    theta : float
        Retention rate. Higher theta means the effect lasts longer.
    max_lag : int
        Maximum number of lags to consider.
    """
    transformed = np.zeros_like(spend, dtype=float)
    for t in range(len(spend)):
        total = 0.0
        for lag in range(max_lag):
            idx = t - lag
            if idx < 0:
                break
            total += spend[idx] * (theta ** lag)
        transformed[t] = total
    return transformed


def hill_function(x, k=30, alpha=1.5):
    """Hill saturation curve.

    x: marketing input
    k: half-saturation point
    alpha: shape parameter controlling steepness
    """
    return (x ** alpha) / (k ** alpha + x ** alpha)


# 1. Adstock example: effect lasts for several periods
weeks = np.arange(12)
original_spend = np.array([0, 1, 2, 3, 5, 4, 3, 2, 1, 0, 0, 0], dtype=float)

theta_values = [0.2, 0.5, 0.8]
fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

ax = axes[0]
for theta in theta_values:
    response = adstock_effect(original_spend, theta=theta, max_lag=12)
    ax.plot(weeks, response, marker="o", linewidth=2, label=f"theta={theta}")

ax.plot(weeks, original_spend, linestyle="--", color="black", linewidth=1.5, label="original spend")
ax.set_title("Adstock effect: delayed carryover")
ax.set_xlabel("Week")
ax.set_ylabel("Effect")
ax.grid(alpha=0.3)
ax.legend()

# 2. Hill function example: saturation effect
x = np.linspace(0, 100, 400)
for k in [10, 30, 60]:
    ax2 = axes[1]
    y = hill_function(x, k=k, alpha=1.5)
    ax2.plot(x, y, linewidth=2, label=f"k={k}")

ax2 = axes[1]
ax2.set_title("Hill function: nonlinear saturation")
ax2.set_xlabel("Marketing spend")
ax2.set_ylabel("Response")
ax2.grid(alpha=0.3)
ax2.legend()

fig.tight_layout()
fig.savefig("code/adstock_hill_example.png", dpi=200)
plt.close(fig)

print("Saved code/adstock_hill_example.png")
