import random
import string


def get_unique_batch_number():
    chars = string.ascii_uppercase

    while True:
        letters = "".join(random.choices(chars, k=3))

        numbers = "".join(random.choices(string.digits, k=3))

        batch_number = f"{letters}{numbers}"

        return batch_number
