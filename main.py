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

    # Initialise lists to store front and rear braking forces
    front_forces_N = []
    rear_forces_N = []

    # Iterate over the range of tyre friction coefficients to calculate braking forces
    for mu in tyre_friction_coefficients:
        # Assume braking deceleration is tyre friction coefficient * gravity
        deceleration_ms2 = mu * GRAVITY_MS2

        # Calculate weight transfer
        weight_transfer_N = calculate_weight_transfer_N(deceleration_ms2)

        # Calculate front and rear braking forces
        front_force_N = calculate_front_braking_force_N(mu, weight_transfer_N)
        rear_force_N = calculate_rear_braking_force_N(mu, weight_transfer_N)

        # Append the calculated forces to the lists
        front_forces_N.append(front_force_N)
        rear_forces_N.append(rear_force_N)
    
    return np.array(front_forces_N), np.array(rear_forces_N)

# Generate a range of tyre friction coefficients for the braking curve
tyre_friction_coefficients = np.linspace(0.1, 1.0, 10)

# Calculate the front and rear braking forces
front_forces_N, rear_forces_N = calculate_braking_curve(tyre_friction_coefficients)

# Check both axle forces sum to the total braking force
total_braking_force_N = front_forces_N + rear_forces_N
expected_total_braking_force_N = tyre_friction_coefficients * MASS_KG * GRAVITY_MS2

assert np.allclose(total_braking_force_N, expected_total_braking_force_N), ("Total braking force does not match expected value.")

# Plot the braking forces
plt.plot(front_forces_N, rear_forces_N, marker="o", label="Ideal Braking Curve", zorder=3)

# Add diagonal lines for tyre friction coefficients
front_force_line_N = np.linspace(0, MASS_KG * GRAVITY_MS2, 400)

for mu in np.arange(0.1, 1.01, 0.1):
    total_braking_force_N = mu * MASS_KG * GRAVITY_MS2
    rear_force_line_N = total_braking_force_N - front_force_line_N

    # Only plot the line where the rear braking force is non-negative
    valid = rear_force_line_N >= 0

    plt.plot(
        front_force_line_N[valid],
        rear_force_line_N[valid],
        color = "lightgray",
        linestyle = "--", 
        linewidth = 0.9, 
        zorder = 1 # Draw behind the main braking curve
    )

    plt.annotate(
        f"{mu:.1f}",
        (total_braking_force_N, 0),
        xytext = (0, 5),
        textcoords = "offset points",
        fontsize = 8,
        rotation = 0,
        ha = "center",
        va = "bottom"
    )

# Set axis labels and title
plt.xlabel("Front Braking Force (N)")
plt.ylabel("Rear Braking Force (N)")
plt.title("Ideal Braking Curve")

# Start both axes at zero
plt.xlim(left=0)
plt.ylim(bottom=0)

# Add grid and legend
plt.grid(True)
plt.legend()
plt.tight_layout()

# Show the plot
plt.savefig("plots/ideal_braking_curve.png", dpi=300)  # Save the plot as a PNG file
plt.show()