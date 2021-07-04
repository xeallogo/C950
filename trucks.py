from datetime import timedelta
from csvreader import *

# O(1) Complexity
class Truck:
    def __init__(self, location, hub_departure, miles, assoc_packages=[]):
        self.location = location
        self.hub_departure = hub_departure
        self.miles = miles
        self.assoc_packages = assoc_packages


#  creates a list of package IDs for each truck
truck_1_packages = ['29', '30', '31', '34', '37', '40', '1', '14', '16', '20', '13', '15', '19', '7', '21', '39']
truck_2_packages = ['3', '18', '36', '38', '6', '25', '32', '28', '4', '12', '17', '24', '26']
truck_3_packages = ['9', '2', '5', '8', '10', '11', '22', '23', '27', '33', '35']

#  creates truck objects for truck1, truck2, and truck3
truck1 = Truck('4001 South 700 East', timedelta(hours=8), 0, truck_1_packages)
truck2 = Truck('4001 South 700 East', timedelta(hours=9, minutes=10), 0, truck_2_packages)
truck3 = Truck('4001 South 700 East', timedelta(hours=10, minutes=30), 0, truck_3_packages)

# O(1) Complexity
# calculates the time it takes to reach an address by the miles travelled
def time_calculator(miles):
    time = miles / 18
    return timedelta(hours=time)

#  starts the truck routes
def start_routes(time):
    run_route(truck1, time)
    run_route(truck2, time)
    run_route(truck3, time)


#  O(n^2) Complexity
# This function iterates over all pkgs, and finds the nearest neighbor (address).
# It then delivers the nearest neighbor's package, and reiterates from the new location.
# This process keeps occurring until the truck is empty.
def run_route(truck, time):
    i = 0
    # current_truck_miles initialized to current miles of truck,
    # current_time initialized to truck's departure time
    # current_distance set to 100. This represents the nearest deliverable location (in miles)
    current_truck_miles = 0
    current_time = truck.hub_departure
    current_distance = float(100)

    #  outer loop iterates after the truck moves location. It saves the results of the inner while loop each time.
    #  inner loop iterates after finding the distance b/w current location and another location
    #  The inner loop keeps the shortest one.
    while len(truck.assoc_packages) != 0:
        while i < len(truck.assoc_packages):
            # Current address set as the truck's location, pkg is selected, selected pkg's address is set,
            # and finally the get_delivery function is called.
            current_truck_location = truck.location
            current_package = hash_table.lookup(truck.assoc_packages[i])
            address = current_package.address
            new_distance = get_distance(current_truck_location, address)

            # variables are set to new values if current distance is larger than the new distance.
            if float(current_distance) > float(new_distance):
                current_distance = float(new_distance)
                location = address
                package = current_package
                value = truck.assoc_packages[i]
            i = i + 1
        i = 0

        # Truck's location set to last package delivered, the delivered package is removed from the truck's
        # package list (assoc_packages), distance is added to the mileage count, delivery time is recorded,
        # and finally the distance is set back to 100 (the initial value)
        truck.location = location
        truck.assoc_packages.remove(value)
        current_truck_miles = current_truck_miles + float(current_distance)
        current_time = package.delivery_time = current_time + time_calculator(current_distance)
        current_distance = float(100)

        # If time != 0, set_package_statuses function is called.
        if time != timedelta(hours=0):
            set_package_status(package, truck, time)
        # package marked as delivered otherwise
        else:
            package.status = 'delivered'

    # returns (truck to hub and mileage to the truck) if truck is empty
    # distance back to hub is calculated, then is added to the mileage count, then sets truck miles
    # equal to the total miles travelled
    if len(truck.assoc_packages) == 0:
        return_to_hub = get_distance(current_truck_location, '4001 South 700 East')
        current_truck_miles = current_truck_miles + float(return_to_hub)
        truck.miles = current_truck_miles

# O(n) Complexity
# returns the distance from current address to the next address
def get_distance(current_address, address):
    if address_lookup(address) > address_lookup(current_address):
        current_distance = distance_data[address_lookup(address)][
            address_lookup(current_address)]
    else:
        current_distance = distance_data[address_lookup(current_address)][
            address_lookup(address)]
    return current_distance


#  O(1) Complexity
#  package statuses can be changed to 'delivered' or 'en route'.  Default is 'at the hub'
def set_package_status(package, truck, time):
    if package.delivery_time <= time:
        package.status = 'delivered'
    elif package.delivery_time > time < truck.hub_departure:
        var = None
    else:
        package.status = 'en route'