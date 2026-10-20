"""Calculate and visualise the ideal braking curve using vehicle parameters."""

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

# Example deceleration value for testing (m/s²)
test_deceleration_ms2 = 5.0  
test_tyre_friction_coefficient = 0.8

weight_transfer_N = calculate_weight_transfer_N(test_deceleration_ms2)

front_braking_force_N = calculate_front_braking_force_N(test_tyre_friction_coefficient, weight_transfer_N)

rear_braking_force_N = calculate_rear_braking_force_N(test_tyre_friction_coefficient, weight_transfer_N)

# Display results
print(f"Static front load: {static_front_load_N:.2f} N")
print(f"Static rear load: {static_rear_load_N:.2f} N")
print(f"Weight transfer at {test_deceleration_ms2:.2f} m/s² deceleration: {weight_transfer_N:.2f} N")
print(f"Front braking force: {front_braking_force_N:.2f} N")
print(f"Rear braking force: {rear_braking_force_N:.2f} N")