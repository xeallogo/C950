#  Alex Gool #002762910

from trucks import *
from datetime import timedelta, datetime
from csvreader import hash_table

# _______________________________USER INTERFACE______________________________________#
# O(1)
print('__________WGUPS__________')
print('Please choose from the below options:')
user_entry = input("0: Exit the program\n"
                   "1: Lookup a truck's mileage\n"
                   "2: Lookup a package by its ID\n"
                   "3: Lookup a package info by its time\n"
                   )

# O(n) Complexity
# Quit the application if user enters 0
if user_entry == '0':
    exit()

#  prints each truck's mileage and the total mileages of all trucks
elif user_entry == '1':
    # calls the start_routes function to start the trucks on their route.
    start_routes(timedelta(hours=-0))
    print('Mileage:\nTruck 1: ' + str(round(truck1.miles, 2))
          + '\nTruck 2: ' + str(truck2.miles) + '\nTruck 3: ' + str(truck3.miles)
          + '\nTotal mileage: ' + str(round(truck1.miles + truck2.miles + truck3.miles, 2)))

#  prints package information by the user-entered package ID
elif user_entry == '2':
    # start_routes function is called so trucks begin their routes
    start_routes(timedelta(hours=-0))
    ID = input('Please enter package ID: ')
    print('Package ID: ' + (hash_table.lookup(ID)).id)
    print('Address: ' + (hash_table.lookup(ID)).address)
    print('Delivery Deadline: ' + (hash_table.lookup(ID)).delivery_deadline)
    print('City: ' + (hash_table.lookup(ID)).city)
    print('Zip Code: ' + (hash_table.lookup(ID)).zip)
    print('Weight: ' + (hash_table.lookup(ID)).weight)
    print('Delivery Status: ' + hash_table.lookup(ID).status + ' : ' + str(
        (hash_table.lookup(ID)).delivery_time))

# this option 3 satisfies part G of the project requirements
elif user_entry == '3':
    try:
        time = input("Please enter a specific time (with 24hr format: HH:MM): ")
        t = datetime.strptime(time, '%H:%M')
        delta = timedelta(hours=t.hour, minutes=t.minute)
        # start_routes function is called so trucks begin their routes
        # using the time-entered by user (later used to set the package statuses).
        start_routes(delta)
        print("\n_______________________ALL PACKAGES AS OF " + str(delta) + '__________________________')
        i = 1
        while i <= 40:
            package = hash_table.lookup(str(i))
            if package.status == 'delivered':
                print(
                    package.id + ' | ' + package.address + ' | '
                    + package.city + ' | ' + package.zip + ' | '
                    + package.weight + ' | ' + package.delivery_deadline + ' | '
                    + package.status + ' @ ' + str(package.delivery_time)
                )
            elif package.status == 'en route':
                print(
                    package.id + ' | ' + package.address + ' | '
                    + package.city + ' | ' + package.zip + ' | '
                    + package.weight + ' | ' + package.delivery_deadline + ' | '
                    + package.status
                )
            else:
                print(
                    package.id + ' | ' + package.address + ' | '
                    + package.city + ' | ' + package.zip + ' | '
                    + package.weight + ' | ' + package.delivery_deadline + ' | '
                    + package.status
                )
            i = i + 1
    except (ValueError, NameError):
        print('That was not the correct format. Try again.')

else:
    print('It seems that entry was invalid. Try again.')
