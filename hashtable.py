class HashTable(object):

    # O(1) Complexity
    def __init__(self, length=40):
        # Create an array of empty values
        self.array = [None] * length

    # O(1) Complexity
    def hash(self, key):
        # Determine the array's index for a specific string key.
        length = len(self.array)
        return hash(key) % length

    # O(1) or O(n) Complexity
    # This function satisfies part E of the project requirements
    def insert(self, key, value):
        # Values is added to array by key
        index = self.hash(key)
        if self.array[index] is not None:
            # Checks if the key already exists.
            for kvp in self.array[index]:
                # If key exists, then update its current value to the new value.
                if kvp[0] == key:
                    kvp[1] = value
                    break
            else:
                # Key was not found - Append to the end of array
                self.array[index].append([key, value])
        else:
            # Index is empty - Create a list and append the K/V pair
            self.array[index] = []
            self.array[index].append([key, value])

    # O(1) Complexity
    # This function satisfies part F of the project requirements
    def lookup(self, key):
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            # returns the key's value if it exists.
            for kvp in self.array[index]:
                if kvp[0] == key:
                    return kvp[1]
            # key did not exist if nothing was returned during the loop
            raise KeyError()
