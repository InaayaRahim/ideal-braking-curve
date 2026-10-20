"""Calculate and visualise the ideal braking curve using vehicle parameters."""

import numpy as np
import matplotlib.pyplot as plt

# Car parameters (SI units)
GRAVITY_MS2 = 9.81
MASS_KG = 280.0
CG_HEIGHT_M = 0.25
WHEELBASE_M = 1.590
FRONT_WEIGHT_DISTRIBUTION = 0.5

# Static axle loads (N)
static_front_load_N = MASS_KG * GRAVITY_MS2 * FRONT_WEIGHT_DISTRIBUTION
static_rear_load_N = MASS_KG * GRAVITY_MS2 * (1 - FRONT_WEIGHT_DISTRIBUTION)

def calculate_weight_transfer_N(deceleration_ms2: float) -> float:
    """Calculate longitudinal weight transfer during braking (N)."""
    # Use positive braking deceleration value so that weight transfer is positive
    return (MASS_KG * deceleration_ms2 * CG_HEIGHT_M) / WHEELBASE_M

def calculate_front_braking_force_N(tyre_friction_coefficient: float, weight_transfer_N: float) -> float:
    """Calculate the front braking force (N)."""
    front_load_during_braking_N = static_front_load_N + weight_transfer_N
    return tyre_friction_coefficient * front_load_during_braking_N

def calculate_rear_braking_force_N(tyre_friction_coefficient: float, weight_transfer_N: float) -> float:
    """Calculate the rear braking force (N)."""
    rear_load_during_braking_N = static_rear_load_N - weight_transfer_N
    return tyre_friction_coefficient * rear_load_during_braking_N

def calculate_braking_curve(tyre_friction_coefficients: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Calculate the braking curve for a range of tyre friction coefficients."""

    # Assume braking deceleration is tyre friction coefficient * gravity
    decelerations_ms2 = tyre_friction_coefficients * GRAVITY_MS2

    # Calculate weight transfer for each friction coefficient
    weight_transfers_N = (MASS_KG * decelerations_ms2 * CG_HEIGHT_M) / WHEELBASE_M

    # Calculate front and rear braking forces for each friction coefficient
    front_forces_N = tyre_friction_coefficients * (static_front_load_N + weight_transfers_N)

    rear_forces_N = tyre_friction_coefficients * (static_rear_load_N - weight_transfers_N)

    return front_forces_N, rear_forces_N

# Generate a range of tyre friction coefficients for the braking curve
tyre_friction_coefficients = np.linspace(0.1, 1.0, 10)

# Calculate the front and rear braking forces
front_forces_N, rear_forces_N = calculate_braking_curve(tyre_friction_coefficients)

# Plot the braking forces
plt.plot(front_forces_N, rear_forces_N, marker="o", label="Ideal Braking Curve")

# Label each point with the corresponding tyre friction coefficient
for i, mu in enumerate(tyre_friction_coefficients):
    plt.annotate(f"{mu:.1f}", (front_forces_N[i], rear_forces_N[i]), xytext=(5,5), textcoords='offset points', fontsize=8)

plt.xlabel("Front Braking Force (N)")
plt.ylabel("Rear Braking Force (N)")
plt.title("Ideal Braking Curve")
plt.grid(True)
plt.legend()
plt.tight_layout()

# Show the plot
plt.savefig("plots/ideal_braking_curve.png", dpi=300)  # Save the plot as a PNG file
plt.show()