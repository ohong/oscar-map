
"""
@author: Oscar Hong (@ohong)
@date: 09-30-2017
"""

import sys
import logging
import pprint


def main():
    # logs are written to 'log_file.txt'
    # highest to lowest urgency: CRITICAL > ERROR > WARNING > INFO > DEBUG
    logging.basicConfig(filename='log_file.txt', level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    # Used for debug testing
    # test set()
    oscar = OscarMap(10)
    oscar.set("alice", 0)  # Situation #1
    oscar.set("alice", 0)  # Situation #2
    oscar.set("alice", 9000)  # Situation #3
    oscar.set("brian", 1)  # Situation #4
    oscar.set("christie", 2)
    oscar.set("dan", 3)
    oscar.set("eve", 4)
    oscar.set("franco", 5)
    oscar.set("gabby", 6)
    oscar.set("hank", 7)
    oscar.set("isabella", 8)
    oscar.set("jimmy", 9)
    oscar.set("oscar", 10)  # Situation #0

    # test get()
    oscar.get("brian")  # It's in there
    oscar.get("alexa")  # It's not in there

    # test delete()
    oscar.delete("isabella")  # It's in there
    oscar.delete("jacob")  # It's not in there

    # test load()
    oscar.load()

    # test display()
    oscar.display()


class OscarMap():

    """
    My General Strategy
     - initialize an list of the given size
     - for a given key, get its index in the list
     - perform set(), get(), and delete() using the index
     - resolve collisions (i.e. two different keys assigned to the same index) by chaining (i.e. list of lists)
    """

    # Constructor
    # Returns an instance of the class with pre-allocated space for the given number of objects.
    def __init__(self, size=1729):
        # if no size specified, use the taxi cab number (b/c I like it)
        self.size = size
        # initialize with 2D list (for chaining later)
        self.list = [[[None]] for x in xrange(self.size)]
        # count tracks how many key-value pairs are in the OscarMap
        self.count = 0
        logging.info(
            "An OscarMap of size {0} has been instantiated.".format(self.size))

    # Stores the given key/value pair in the hash map. Returns a boolean value indicating success / failure of the operation.
    def set(self, key, value):
        """
        Possible situations:
        #0: This OscarMap is at  its max capacity - set() fails.
        #1: The element at the key's index is None - set it to this key-value pair.
        #2: The key-value pair is already in this OscarMap - do nothing.
        #3: The key is already in this OscarMap but the value is different - update the value.
        #4: The key isn't in this OscarMap & there is already at least one other key-value pair at this index - append this key-value pair to the exisiting one(s) (i.e. chaining using a "list of lists")
        """

        target_pair = [key, value]
        key_index = self.get_index(key)

        # Situation #0
        if self.count == self.size:
            logging.error(
                "Your OscarMap has reached its max capacity of {0}, no more items can be added.".format(self.size))
            return False

        # Situation #1
        if self.list[key_index][0] == [None]:
            self.list[key_index][0] = target_pair
            logging.info(
                "{0} is the first key-value pair you've added to index {1} of your OscarMap!".format(target_pair, key_index))
            self.count += 1
            return True

        # Situation #2
        if target_pair in self.list[key_index]:
            logging.info(
                "The key-value pair {0} is already in your OscarMap!".format(target_pair))
            return True

        # Situation #3
        for current_pair in self.list[key_index]:
            if current_pair[0] == key:
                current_pair[1] = value
                logging.info(
                    "The key '{0}' was already in your OscarMap, but the value has been updated to '{1}'!".format(key, value))
                return True

        # Situation #4
        self.list[key_index].append(target_pair)
        logging.warning("Collision! The key-value pair {0} has been added. There are now {1} key-value pairs chained at index {2}.".format(
            target_pair, len(self.list[key_index]), key_index))
        self.count += 1
        return True

        logging.error("Nothing worked. Sorry, mate.")
        return False

    # Returns the value associated with the given key, or None if no value is set.
    def get(self, key):

        key_index = self.get_index(key)

        for current_pair in self.list[key_index]:
            if current_pair[0] == key:
                # found the key-value pair for the given key
                value = current_pair[1]
                logging.info(
                    "The value for key '{0}' is '{1}'.".format(key, value))
                return value

        # no key-value pairs at this index match the given key
        logging.warning(
            "Can't get the value for key '{0}'; it's not in your OscarMap.".format(key))
        return None

    # Deletes the value associated with the given key, returning the value on success or None if the key has no value.
    def delete(self, key):

        key_index = self.get_index(key)

        for current_pair in self.list[key_index]:
            if current_pair[0] == key:
                # found the key-value pair for the given key
                value = current_pair[1]
                current_pair[1] = None
                self.count -= 1
                logging.info(
                    "Deleted the value for key '{0}'; it was {1}.".format(key, value))
                return value

        logging.warning(
            "Can't delete the value for key '{0}'; it's not in your OscarMap.".format(key))
        return None

    # Returns a float value representing the load factor (`(items in hash map)/(size of hash map)`) of the data structure. Since the size of the dat structure is fixed, this should never be greater than 1.
    def load(self):
        load_factor = float(self.count) / float(self.size)
        logging.info(
            "The load factor for your OscarMap is '{0}'.".format(load_factor))
        return load_factor

    def get_index(self, key):
        return hash(key) % self.size

    def display(self):
        logging.info("\n" + pprint.pformat(self.list))


if __name__ == '__main__':
    main()
