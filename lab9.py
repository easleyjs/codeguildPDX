#lab9.py
#Unit Converter
"""
This lab will involve writing a program that allows the user to convert a number between units.

Version 1

Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.

> what is the distance in feet? 12
> 12 ft is 3.6576 m
Version 2

Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.

1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m
Below is some sample input/output:

> what is the distance? 100
> what are the units? mi
> 100 mi is 160934 m
Version 3

Add support for yards, and inches.

1 yard is 0.9144 m
1 inch is 0.0254 m
Version 4

Now we'll ask the user for the distance, the starting units, and the units to convert to.

"""
#Base Unit is Meters.
unit_dict = {   'ft':0.3048,
                'yd':0.9144,
                'm':1,
                'km':.001,
                'mi':0.00062137119
}
distance = float(input("What is the distance?: "))
startUnit = input("What is the unit? [ft/m/km/mi]: ")
endUnit = input("What unit would you like to convert to? [m/km/mi]: ")

print("%s %s equals %s %s." % (distance,startUnit,round(distance*unit_dict[startUnit]*unit_dict[endUnit],4),endUnit))
