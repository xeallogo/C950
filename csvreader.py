import csv
from packages import Package
from hashtable import HashTable

hash_table = HashTable()  # creates new HashTable object

# O(n) Complexity
# package data is imported from packages.csv file, package objects are created and added to a hash table.
with open('CSVs/packages.csv') as packages_file:
    readCSV = csv.reader(packages_file, delimiter=',')
    for row in readCSV:
        id = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        delivery_deadline = row[5]
        weight = row[6]
        note = row[7]

        #  package #9 is changed to corrected address
        if id == '9':
            address = '410 S State St'
            zip = '84111'

        #  package object created for each package
        p1 = Package(id, address, city, state, zip, delivery_deadline, weight, note, 'at the hub', '')

        #  each package is placed into the hashtable with their key being the package ID
        hash_table.insert(id, p1)

# O(n) Complexity
# distance data imported from distances.csv file.
with open('CSVs/distances.csv') as distances_file:
    distance_data = []
    readCSV = csv.reader(distances_file, delimiter=',')
    for row in readCSV:
        distance_data.append(row)

# O(n) Complexity
# address data imported from addresses.csv file.
with open('CSVs/addresses.csv') as addresses_file:
    address_data = []
    readCSV = csv.reader(addresses_file, delimiter=',')
    for row in readCSV:
        address_data.append(row)


# O(n) Complexity
# returns a number representing the address's locaiton
def address_lookup(address):
    i = 0
    while i < len(address_data):
        if address == address_data[i][1]:
            return i
        else:
            i = i + 1