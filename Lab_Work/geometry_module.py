# geometry_module.py
# Module to calculate Curved Surface Area, Total Surface Area and Volume
# of Cube, Cuboid, Cylinder, Cone, Sphere and Hemisphere

import math

# ---------------- Cube ----------------

def cube_total_surface_area(side):
    return 6 * side * side

def cube_volume(side):
    return side ** 3


# ---------------- Cuboid ----------------

def cuboid_total_surface_area(length, breadth, height):
    return 2 * (length * breadth + breadth * height + length * height)

def cuboid_volume(length, breadth, height):
    return length * breadth * height


# ---------------- Cylinder ----------------

def cylinder_curved_surface_area(radius, height):
    return 2 * math.pi * radius * height

def cylinder_total_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

def cylinder_volume(radius, height):
    return math.pi * radius * radius * height


# ---------------- Cone ----------------

def cone_curved_surface_area(radius, slant_height):
    return math.pi * radius * slant_height

def cone_total_surface_area(radius, slant_height):
    return math.pi * radius * (radius + slant_height)

def cone_volume(radius, height):
    return (1 / 3) * math.pi * radius * radius * height


# ---------------- Sphere ----------------

def sphere_curved_surface_area(radius):
    return 4 * math.pi * radius * radius

def sphere_total_surface_area(radius):
    return 4 * math.pi * radius * radius

def sphere_volume(radius):
    return (4 / 3) * math.pi * radius ** 3


# ---------------- Hemisphere ----------------

def hemisphere_curved_surface_area(radius):
    return 2 * math.pi * radius * radius

def hemisphere_total_surface_area(radius):
    return 3 * math.pi * radius * radius

def hemisphere_volume(radius):
    return (2 / 3) * math.pi * radius ** 3
