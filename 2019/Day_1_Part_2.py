# ################################################################################
# NAME : Day_1_Part_2.py
# DATE STARTED : Feb 19, 2020
# AUTHORS : Dale Mercado
# PURPOSE : Advent of code 2019 Day 1 "Tyranny of the Rocket Equation"
#   Take the sum of several masses in order to determine the amount of
#   rocket fuel required
#
# EXPLANATION :
# CALLING SEQUENCE :
# INPUTS :
#           nsims (number of simulations/files to read in)
#
# OUTPUTS :
# REVISION HISTORY :
################################################################################

import numpy as np

mass = [130541,69856,104618,149406,64500,128553,94958,104788,87642,60597,142981,132940,64860,122199,131528,84879,144729,139907,147856,66258,95890,115399,106239,126841,59689,146878,105262,137079,145130,114767,94900,64349,105456,59491,79265,89321,62254,106996,107612,71451,138032,137610,52157,68712,134770,111493,50370,91088,149756,51638,110641,60113,54732,86907,73037,111831,116378,93493,55956,111018,99771,65224,149852,97464,148596,140102,81222,106843,61575,112180,124277,59315,101347,141260,90253,87946,55455,115978,51255,149617,77484,133499,128627,75777,135748,87630,86834,145664,86360,139511,60064,106100,123539,115732,107666,89177,82419,98712,148947,50931]



def fuel_calc(mass,fuel_flag = 1):
    fuel = []
    for i in mass:
        x = i
        while fuel_flag == 1:
            if x > 0:
                needed_fuel = np.floor(x/3) - 2
                print('Fuel for mass ',x, 'is ', needed_fuel)
                if needed_fuel <= 0:
                    needed_fuel = 0
                    fuel_flag = 0
                fuel = np.append(fuel, needed_fuel)
                x = needed_fuel
        needed_fuel = 1
        fuel_flag = 1
    # print(fuel)
    # needed = np.sum(fuel)
    # return(needed)
    return(fuel)

fuel_mass = fuel_calc(mass)
total_fuel = np.sum(fuel_mass)
# extra_fuel = fuel_calc(total_fuel)
# extra_fuel2 = fuel_calc(extra_fuel)
# extra_fuel3 = fuel_calc(extra_fuel2)



print('The total amount of fuel needed it ', total_fuel)
# print('The total amount of fuel needed it ', extra_fuel)
# print('The total amount of fuel needed it ', extra_fuel2)
# print('The total amount of fuel needed it ', extra_fuel3)
