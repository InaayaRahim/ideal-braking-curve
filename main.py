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

print(f"Static front load: {static_front_load_N:.2f} N")
print(f"Static rear load: {static_rear_load_N:.2f} N")