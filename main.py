import os
from config import dev_config
from dotenv import load_dotenv

db = dev_config.get('db')
table = dev_config.get('table')
user = dev_config.get('user')

def test_function(x, y):
    add = x + y
    subtract = x - y
    multiply = x * y
    exponant = x ** y

    return add, subtract



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(test_function(6, 4))

