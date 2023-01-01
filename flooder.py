import os
import random
import string



def generate_random_filename(length):
    """Generates a random file name with the specified length.
    The file name will consist of lowercase letters and digits.
    """
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def create_random_file():
    """Creates a new file with a random file name and fills it with random data.
    The file name will be of the form 'random_XXXXXX', where XXXXXX is a random string.
    """
    # Generate a random file name
    filename = f'random_{generate_random_filename(6)}'

    # Open the file in write mode
    with open(filename, 'w') as f:
        # Write a random string to the file
        f.write(generate_random_filename(10))

while True:
    create_random_file()
