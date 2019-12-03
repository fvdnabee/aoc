
with open('input', 'r') as f:
    contents = f.readlines()

def calc_fuel_requirement(mass):
    fuel_requirement = mass//3 - 2
    if fuel_requirement > 6:
        print(mass, fuel_requirement)
        fuel_requirement += calc_fuel_requirement(fuel_requirement)

    return fuel_requirement

total_fuel = 0
for line in contents:
    mass = int(line)
    fuel_requirement = calc_fuel_requirement(mass)
    print("module with mass {} requires {} fuel".format(mass, fuel_requirement))
    # if fuel < 0: fuel = 0
    total_fuel += fuel_requirement

print("Fuel required for all modules and fuel {}".format(total_fuel))
