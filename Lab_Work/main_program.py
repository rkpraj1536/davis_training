# main_program.py
# Program to use geometry_module and display menu

import geometry_module

while True:
    print("\n------ Figure Menu ------")
    print("1. Cube")
    print("2. Cuboid")
    print("3. Cylinder")
    print("4. Cone")
    print("5. Sphere")
    print("6. Exit")

    figure_choice = int(input("Enter your choice: "))

    if figure_choice == 6:
        print("Program Ended")
        break

    print("\n------ Operation Menu ------")
    print("1. Curved Surface Area")
    print("2. Total Surface Area")
    print("3. Volume")

    operation_choice = int(input("Enter operation choice: "))

    if figure_choice == 1:
        side = float(input("Enter side of cube: "))

        if side <= 0:
            print("Invalid Input")
        elif operation_choice == 1:
            print("Cube does not have Curved Surface Area")
        elif operation_choice == 2:
            print("Total Surface Area =", geometry_module.cube_total_surface_area(side))
        elif operation_choice == 3:
            print("Volume =", geometry_module.cube_volume(side))
        else:
            print("Invalid Operation")

    elif figure_choice == 2:
        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))
        height = float(input("Enter height: "))

        if length <= 0 or breadth <= 0 or height <= 0:
            print("Invalid Input")
        elif operation_choice == 1:
            print("Cuboid does not have Curved Surface Area")
        elif operation_choice == 2:
            print("Total Surface Area =", geometry_module.cuboid_total_surface_area(length, breadth, height))
        elif operation_choice == 3:
            print("Volume =", geometry_module.cuboid_volume(length, breadth, height))
        else:
            print("Invalid Operation")

    elif figure_choice == 3:
        radius = float(input("Enter radius: "))
        height = float(input("Enter height: "))

        if radius <= 0 or height <= 0:
            print("Invalid Input")
        elif operation_choice == 1:
            print("Curved Surface Area =", geometry_module.cylinder_curved_surface_area(radius, height))
        elif operation_choice == 2:
            print("Total Surface Area =", geometry_module.cylinder_total_surface_area(radius, height))
        elif operation_choice == 3:
            print("Volume =", geometry_module.cylinder_volume(radius, height))
        else:
            print("Invalid Operation")

    elif figure_choice == 4:
        radius = float(input("Enter radius: "))

        if operation_choice == 3:
            height = float(input("Enter height: "))

            if radius <= 0 or height <= 0:
                print("Invalid Input")
            else:
                print("Volume =", geometry_module.cone_volume(radius, height))

        elif operation_choice == 1 or operation_choice == 2:
            slant_height = float(input("Enter slant height: "))

            if radius <= 0 or slant_height <= 0:
                print("Invalid Input")
            elif operation_choice == 1:
                print("Curved Surface Area =", geometry_module.cone_curved_surface_area(radius, slant_height))
            else:
                print("Total Surface Area =", geometry_module.cone_total_surface_area(radius, slant_height))
        else:
            print("Invalid Operation")

    elif figure_choice == 5:
        radius = float(input("Enter radius: "))

        if radius <= 0:
            print("Invalid Input")
        elif operation_choice == 1:
            print("Curved Surface Area =", geometry_module.sphere_curved_surface_area(radius))
        elif operation_choice == 2:
            print("Total Surface Area =", geometry_module.sphere_total_surface_area(radius))
        elif operation_choice == 3:
            print("Volume =", geometry_module.sphere_volume(radius))
        else:
            print("Invalid Operation")

    else:
        print("Invalid Figure Choice")
