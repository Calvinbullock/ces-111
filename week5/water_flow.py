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
    print(f"l.17- {water_height}")
    return water_height


def pressure_gain_from_water_height(height):
    """
    calculates and returns height of the water column in meters.

    Paramiters:
    (int|float) height

    returns:
    (flaot) pressure gain
    """

    # ρ is the density of water (998.2 kilogram / meter3)
    density_of_water = 998.2

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

    # ρ is the density of water (998.2 kilogram / meter3)
    density_of_water = 998.2

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

    # ρ is the density of water (998.2 kilogram / meter3)
    water_density = 998.2

    # P is the lost pressure in kilopascals
    lost_pressure = ((-0.04) * water_density * fluid_velocity**2 * fitting_num) / 2000
    return round(lost_pressure, 3)


def main():
    print(f"f21- {water_column_height(0, 0)}")


if __name__ == "__main__":
    main()
