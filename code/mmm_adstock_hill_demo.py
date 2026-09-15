import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def adstock(x, theta=0.5):
    """Geometric adstock transformation.

    x: marketing spend by period
    theta: retention rate;
           smaller theta -> faster decay, larger theta -> longer carryover
    """
    y = np.zeros(len(x), dtype=float)
    for t in range(len(x)):
        y[t] = x[t] + (theta * y[t - 1] if t > 0 else 0.0)
    return y


def hill(x, k=30, alpha=1.5):
    """Hill saturation function.

    x: spend or exposure
    k: half-saturation point
    alpha: shape parameter controlling the steepness of the curve
    """
    return (x ** alpha) / (k ** alpha + x ** alpha)


# --- Adstock example ---
weeks = np.arange(12)
spend = np.array([0, 2, 5, 4, 3, 2, 6, 7, 5, 4, 2, 1], dtype=float)

fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
for theta in [0.2, 0.5, 0.8]:
    effect = adstock(spend, theta=theta)
    axes[0].plot(weeks, effect, marker="o", linewidth=2, label=f"theta={theta}")

axes[0].plot(weeks, spend, linestyle="--", color="black", linewidth=1.5, label="original spend")
axes[0].set_title("Adstock: delayed carryover effect")
axes[0].set_xlabel("Week")
axes[0].set_ylabel("Effect")
axes[0].grid(alpha=0.3)
axes[0].legend(loc="upper left")

# --- Hill example ---
marketing_spend = np.linspace(0, 100, 400)
for k in [10, 30, 60]:
    axes[1].plot(marketing_spend, hill(marketing_spend, k=k, alpha=1.5), linewidth=2, label=f"k={k}")

axes[1].set_title("Hill function: nonlinear saturation")
axes[1].set_xlabel("Marketing spend")
axes[1].set_ylabel("Response")
axes[1].grid(alpha=0.3)
axes[1].legend(loc="lower right")

fig.tight_layout()
fig.savefig("code/adstock_hill_example.png", dpi=200)
print("Saved code/adstock_hill_example.png")
