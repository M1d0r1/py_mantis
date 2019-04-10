import random
import string


class RandomData:

    def __init__(self):
        pass

    @staticmethod
    def get_random_bool():
        i = random.randrange(2)
        if i == 0:
            return True
        else:
            return False


    @staticmethod
    def get_random_list_value(list):
        i = random.randrange(len(list))
        return list[i]

    # noinspection PyUnusedLocal
    @staticmethod
    def get_random_string():
        ind = random.randrange(20)
        s = ''.join([random.choice(string.ascii_letters + string.digits + " ") for i in range(ind)])
        return s

    @staticmethod
    def get_random_phone():
        return str(random.randrange(1000000, 9999999))

    @staticmethod
    def get_random_multistring():
        return "%s\n%s\n%s" % (
            RandomData.get_random_string(), RandomData.get_random_string(), RandomData.get_random_string())
