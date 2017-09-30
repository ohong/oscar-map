
"""
@author: Oscar Hong (@ohong)
@date: 09-30-2017
"""

import sys
import pprint


def main():

    oscar = OscarMap(10)
    oscar.set("alice", 10101)
    oscar.set("brian", 2299)
    oscar.set("chris", 7689)
    oscar.set("dan", 45666)
    oscar.set("eve", 6758)
    oscar.set("francesca", 867430)
    oscar.set("gal", 12345)
    oscar.set("lauren", 8008)

    oscar.display()


"""
My General Strategy
 - initialize an list of the given size
 - for a given key, get it's index in the array
 - perform set(), get(), and delete() using the index
 - resolve collisions (i.e. two different keys assigned to the same index) by chaining (i.e. list of lists)
"""


class OscarMap():

    # Returns an instance of the class with pre-allocated space for the given number of objects.
    def __init__(self, size=1729):
        # constructor
        # if no size specified, use the taxi cab number (b/c I like it)
        self.size = size
        # initialize with 2D list (for chaining later)
        self.list = [[[None]] for x in xrange(self.size)]
        # count tracks how many key-value pairs are in the OscarMap
        self.count = 0

    # Stores the given key/value pair in the hash map. Returns a boolean value indicating success / failure of the operation.
    def set(self, key, value):
        """
        Possible situations:
        #0: This OscarMap is at max capacity (i.e. count == size) - return False.
        #1: The element at its index is None - set it to this key-value pair.
        #2: The key-value pair is already in this OscarMap - do nothing.
        #3: The key is already in this OscarMap but the value is different - update the value.
        #4: The key isn't in this OscarMap & there is already at least one other key-value pair at this index - append this key-value pair to the exisiting one(s) (i.e. chaining using a "list of lists")
        """

        target_pair = [key, value]
        key_index = self.get_index(key)

        # Situation #0
        if self.count == self.size:
            print "Your OscarMap has reached its max capacity of {0}, no more items can be added.".format(self.size)
            return False

        # Situation #1
        if self.list[key_index][0] == [None]:
            self.list[key_index][0] = target_pair
            print "{0} is the first key-value pair you've added to index {1} of your OscarMap!".format(target_pair, key_index)
            self.count += 1
            return True

        # Situation #2
        if target_pair in self.list[key_index]:
            print "The key-value pair {0} is already in your OscarMap!".format(target_pair)
            return True

        # Situation #3
        for current_pair in self.list[key_index]:
            if current_pair[0] == key:
                current_pair[1] = value
                print "The key '{0}' was already in your OscarMap, but the value has been updated to '{1}'!".format(key, value)
                return True

        # Situation #4
        self.list[key_index].append(target_pair)
        print "Collision! The key-value pair {0} has been added. There are now {1} key-value pairs chained at index {2}.".format(target_pair, len(self.list[key_index]), key_index)
        self.count += 1
        return True

        print "Nothing worked. Sorry, mate."
        return False

    # Returns the value associated with the given key, or None if no value is set.
    def get(self, key):

        key_index = self.get_index(key)

        # No key-value pairs are at this index
        if self.list[key_index][0] == [None]:
            print "The key '{0}' is not in your OscarMap.".format(key)
            return None
        else:
            for current_pair in self.list[key_index]:
                if current_pair[0] == key:
                    return current_pair[1]
            print "The key '{0}' is not in your OscarMap.".format(key)
            return None

    # Deletes the value associated with the given key, returning the value on success or None if the key has no value.
    def delete(self, key):

        key_index = self.get_index(key)

        # No key-value pairs are at this index
        if self.list[key_index][0] == [None]:
            print "The key '{0}' is not in your OscarMap.".format(key)
            return None
        else:
            for current_pair in self.list[key_index]:
                if current_pair[0] == key:
                    value = current_pair[1]
                    current_pair[1] = None
                    self.count -= 1
                    return value

            print "The key '{0}' is not in your OscarMap.".format(key)
            return None

    # Returns a float value representing the load factor (`(items in hash map)/(size of hash map)`) of the data structure. Since the size of the dat structure is fixed, this should never be greater than 1.
    def load(self):
        load_factor = float(self.count) / float(self.size)
        return load_factor

    def get_index(self, key):
        return hash(key) % self.size

    def display(self):
        pprint.pprint(self.list)


if __name__ == '__main__':
    main()
