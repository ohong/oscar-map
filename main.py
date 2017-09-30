
"""
@author: Oscar Hong (@ohong)
@date: 09-30-2017
"""

import sys
import pprint


def main():
    # print hash("lauren") % 10
    oscar = OscarMap(10)
    oscar.set("alice", 10101)
    oscar.set("brian", 2299)
    oscar.set("chris", 7689)
    oscar.set("dan", 45666)
    oscar.set("eve", 6758)
    oscar.set("francesca", 867430)
    oscar.set("gal", 12345)
    oscar.set("gal", 123456)
    oscar.set("lauren", 8008)
    pprint.pprint(oscar.display())


"""
My General Strategy
 - initialize an list of the given size
 - for a given key, get it's index in the array
 - perform set(), get(), and delete() using the index
 - resolve collisions (i.e. two different keys assigned to the same index) by chaining (i.e. list of lists)
"""


class OscarMap():

    def __init__(self, size=1729):
        # constructor
        # if no size specified, use the taxi cab number (b/c I like it)
        self.size = size
        # initialize with 2D list (for chaining later)
        self.list = [[[None]] for x in xrange(self.size)]

    def set(self, key, value):
        """
        Possible situations:
        #1: The element at its index is None - set it to this key-value pair.
        #2: The key-value pair is already in this OscarMap - do nothing.
        #3: The key is already in this OscarMap but the value is different - update the value.
        #4: The key isn't in this OscarMap & there is already at least one other key-value pair at this index - append this key-value pair to the exisiting one(s) (i.e. chaining using a "list of lists")
        """

        target_pair = [key, value]
        key_index = self.get_index(key)

        # Situation #1
        if self.list[key_index][0] == [None]:
            self.list[key_index][0] = target_pair
            print "{0} is the first key-value pair you've added to index {1} of your OscarMap!".format(target_pair, key_index)
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
        return True

        print "Nothing worked. Sorry, mate."
        return False

    def get(self, key):
        # TODO
        return

    def delete(self, key):
        # TODO
        return

    def load(self):
        # TODO
        # returns a float
        return

    def get_index(self, key):
        return hash(key) % self.size

    def display(self):
        return self.list


if __name__ == '__main__':
    main()
