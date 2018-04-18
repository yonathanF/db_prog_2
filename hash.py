'''
Programming Task 2: Hashing
@authors: Yonathan (yf2ey)

This is our implementation of a hash data structure.
It uses a file as input with the following specs:
    # of search keys > 0
    search keys (comma separated)
    # of buckets
    # of records/bucket
'''


class HashTable:
    ''' A class to hold together all the functions nicely '''

    def __init__(self, num_buckets, rec_buckets):

        # save these incase we need them later
        self.num_buckets = num_buckets
        self.rec_buckets = rec_buckets

        # create the table
        self.table = [[[] for _ in range(rec_buckets)]
                      for _ in range(num_buckets)]

    def create_overflow_bucket(self, bucket):
        ''' when there are more records in a bucket than
            expected, this method will create an extra
            bucket to handle the overflow '''

        self.table[bucket].append([])

    def hash_function(self, key):
        ''' hashes a given key using our function '''

        ascii_sum = 0
        # get sum of ascii values
        for index, char in enumerate(key):
            ascii_sum += ord(char) * 131**index

        return ascii_sum % self.num_buckets

    def insert(self, key):
        ''' inserts a key into the hash table '''

        # hash the key
        key_hash = self.hash_function(key)

        # get the bucket
        bucket = self.table[key_hash]

        # try to find a record
        for record in bucket:

            # found empty record, put it in and exit
            if not record:
                record.append(key)
                return True

        # couldn't find any empty record if we reach this
        self.create_overflow_bucket(key_hash)

        # try again
        self.insert(key)

    def print_table(self):
        ''' prints the table in a nice format '''

        print("-" * 20 * self.rec_buckets)
        for index, row in enumerate(self.table):
            print("#" + str(index), end=" ")
            for record in row:
                print(record, end="\t")
            print("\n")
            print("-" * 20 * self.rec_buckets)


def check_errors(num_keys, keys, num_buckets, rec_buckets):
    ''' checks for errors in value '''

    # check specified vs provided
    if len(keys) != num_keys:
        return False

    # check num_keys
    if num_keys < 10:
        return False

    # buckets * records vs keys
    if num_buckets * rec_buckets > num_buckets:
        return False

    return True


def get_input(filename="input.txt"):
    ''' gets input from file and returns it in vars '''

    # read it line by line
    data = open(filename, "r")
    num_keys = int(data.readline().strip("\n").strip(" "))
    keys = data.readline().strip("\n").strip(" ").split(",")
    num_buckets = int(data.readline().strip("\n").strip(" "))
    rec_buckets = int(data.readline().strip("\n").strip(" "))

    data.close()

    # error check it and return
    if not check_errors(num_keys, keys, num_buckets, rec_buckets):
        return keys, num_buckets, rec_buckets

    # if not raise an error
    raise Exception("Bad Input!")


def main():
    ''' main entry point of the program '''

    # get input from file
    keys, num_buckets, rec_buckets = get_input()

    hash_table = HashTable(num_buckets, rec_buckets)

    for key in keys:
        hash_table.insert(key)

    hash_table.print_table()


if __name__ == "__main__":
    main()
