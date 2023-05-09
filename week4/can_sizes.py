import math

def Main():
    tag_list = [
        "#1 Picnic",
        "#1 Tall",
        "#2",
        "#2.5 1",
        "#3 Cylinder",
        "#5",
        "#6Z",
        "#8Z short",
        "#10",
        "#211",
        "#300",
        "#303",
    ]

    radius_list = [
        6.83,
        7.78,
        8.73,
        10.32,
        10.79,
        13.02,
        5.40,
        6.83,
        15.72,
        6.83,
        7.62,
        8.10,
    ]

    height_list = [
        10.16,
        11.91,
        11.59,
        11.91,
        17.78,
        14.29,
        8.89,
        7.62,
        17.78,
        12.38,
        11.27,
        11.11,
    ]

    for i in range(len(height_list)):
        print(f"{tag_list[i]}: {storage_efficiency(radius_list[i], height_list[i])}")


def compute_volume(radius, height):
    """
    Computes the volume of a cylinder

    paramiters:
    radius (int|float): radiues of a cylinder
    hight (int|float): hight of a cylinder

    returns:
    Float: the computed volume

    """
    return math.pi * radius**2 * height


def compute_surface_area(radius, height):
    """
    Computes the surface area of a cylinder

    paramiters:
    radius (int|float): surface area of a cylinder
    hight (int|float): surface area of a cylinder

    returns:
    Float: the computed surface area

    """
    return 2 * math.pi * radius * (radius + height)


def storage_efficiency(radius, height):
    """
    Computes the Storage efficeny of a cylinder

    paramiters:
    radius (int|float): surface area of a cylinder
    hight (int|float): surface area of a cylinder

    returns:
    Float: the computed efficency of the cylinder

    """
    surface_area = compute_surface_area(radius, height)
    volume = compute_volume(radius, height)

    return round(volume / surface_area, 2)


Main()