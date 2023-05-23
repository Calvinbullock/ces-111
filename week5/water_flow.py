import pytest

# Global constant
# ρ is the density of water (998.2 kilogram / meter3)
DENSITY_OF_WATER = 998.2


def water_column_height(tower_height, tank_height):
    """
    calculates and returns the height of a column of water from a
    towers height and a tank wall's height.

    Paramiters:
    (int|float) tower_height
    (int|float) tank_height

    returns:
    (flaot) hight of water column
    """

    water_height = tower_height + (3 * tank_height) / 4
    return water_height


def pressure_gain_from_water_height(height):
    """
    calculates and returns height of the water column in meters.

    Paramiters:
    (int|float) height

    returns:
    (flaot) pressure gain
    """

    # g is the acceleration from Earths gravity
    # (9.80665 meter / second2)
    gravity = 9.80665

    # Compute and return pressure
    pressure = (DENSITY_OF_WATER * gravity * height) / 1000

    return round(pressure, 3)


def pressure_loss_from_pipe(
    pipe_diameter, pipe_length, friction_factor, fluid_velocity
):
    """
    calculates and returns the pressure lose from a pipe in kilopascals,

    Paramiters:
    (int|float) pipe_diameter
    (int|float) pipe_length
    (int|float) friction_factor
    (int|float) fluid_velocity

    returns:
    (flaot) of the pressure lose
    """

    # P is the lost pressure in kilopascals
    pressure = (
        -friction_factor * pipe_length * DENSITY_OF_WATER * fluid_velocity**2
    ) / (2000 * pipe_diameter)

    return round(pressure, 3)


def pressure_loss_from_fittings(fluid_velocity, fitting_num):
    """
    calculates and returns the pressure lose from a fittings on a pipe
    in kilopascals,

    Paramiters:
    (int|float) fluid_velocity: is the velocity of the water
    (int|float) fitting_num: is the quantity of fittings
                        flowing through the pipe in meters / second

    returns:
    (flaot) the lost pressure in kilopascals
    """

    # P is the lost pressure in kilopascals
    lost_pressure = (
        (-0.04) * DENSITY_OF_WATER * fluid_velocity**2 * fitting_num
    ) / 2000

    return round(lost_pressure, 3)


def reynolds_number(hydraulic_diameter, fluid_velocity):
    """
    calculates and returns the pressure lose from a fittings on a pipe
    in kilopascals,

    Paramiters:
    (int|float) hydraulic diameter of a pipe in meters. For a round
                        pipe, the hydraulic diameter is the same
                        as the pipe's inner diameter.
    (int|float) velocity of the water flowing through the pipe in
                        meters / second

    returns:
    (flaot) the Reynolds number
    """
    # μ is the dynamic viscosity of water (0.0010016 Pascal seconds)
    water_dynamic_viscosity = 0.0010016

    reynolds_number = (
        DENSITY_OF_WATER * hydraulic_diameter * fluid_velocity
    ) / water_dynamic_viscosity

    return round(reynolds_number)


def pressure_loss_from_pipe_reduction(
    larger_diameter, fluid_velocity, reynolds_number, smaller_diameter
):
    """
    calculates and returns the pressure lose from a fittings on a pipe
    in kilopascals,

    Paramiters:
    (int|float) Reynolds number that corresponds to the pipe with
                        the larger diameter
    (int|float) diameter of the larger pipe in meters
    (int|float) diameter of the smaller pipe in meters
    (int|float) velocity of the water flowing through the larger
                        diameter pipe in meters / second

    returns:
    (flaot) the lost pressure kilopascals
    """

    # k is a constant computed by the first formula and used in the second formula
    constant = (0.1 + (50 / reynolds_number)) * (
        (larger_diameter / smaller_diameter) ** 4 - 1
    )

    # round to the ones 1
    constant = round(constant, 3)

    # the lost pressure kilopascals
    lost_pressure = ((-constant) * DENSITY_OF_WATER * fluid_velocity**2) / 2000

    return round(lost_pressure, 3)


PVC_SCHED80_INNER_DIAMETER = 0.28687  # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65  # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692  # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018  # (unitless)
HOUSEHOLD_VELOCITY = 1.75  # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(
        diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER
    )
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")

    # testing for local main run
    # Height of water tower (meters): 36.6
    # Height of water tank walls (meters): 9.1
    # Length of supply pipe from tank to lot (meters): 1524.0
    # Number of 90° angles in supply pipe: 3
    # Length of pipe from supply to house (meters): 15.2
    # Pressure at house: 158.7 kilopascals

if __name__ == "__main__":
    main()
