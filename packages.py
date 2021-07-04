# Constructor for Package class objects
# O(1)
class Package:
    def __init__(self, package_id, package_address, package_city, package_state, package_zip,
                 package_delivery_deadline, package_weight, package_note, package_status, delivery_time):
        self.id = package_id
        self.address = package_address
        self.city = package_city
        self.state = package_state
        self.zip = package_zip
        self.delivery_deadline = package_delivery_deadline
        self.weight = package_weight
        self.note = package_note
        self.status = package_status
        self.delivery_time = delivery_time
