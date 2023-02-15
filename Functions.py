import math

# Basic arithmetic operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Trigonometric functions
def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def arcsin(x):
    return math.asin(x)

def arccos(x):
    return math.acos(x)

def arctan(x):
    return math.atan(x)

# Exponential and logarithmic functions
def exp(x):
    return math.exp(x)

def log(x, base=10):
    return math.log(x, base)

def ln(x):
    return math.log(x)

def sqrt(x):
    return math.sqrt(x)

# Statistical functions
def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        return (sorted_numbers[n//2] + sorted_numbers[n//2-1]) / 2
    else:
        return sorted_numbers[n//2]

def mode(numbers):
    mode_dict = {}
    for number in numbers:
        if number in mode_dict:
            mode_dict[number] += 1
        else:
            mode_dict[number] = 1
    mode_list = [k for k, v in mode_dict.items() if v == max(mode_dict.values())]
    return mode_list

def standard_deviation(numbers):
    n = len(numbers)
    mean_value = mean(numbers)
    variance = sum([(x-mean_value)**2 for x in numbers]) / n
    return math.sqrt(variance)

# String manipulation functions
def reverse_string(string):
    return string[::-1]

def count_occurrences(string, substring):
    return string.count(substring)

def replace_substring(string, old_substring, new_substring):
    return string.replace(old_substring, new_substring)

def capitalize_first_letter(string):
    return string.capitalize()

# File I/O functions
def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

def write_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data)

# List manipulation functions
def concatenate_lists(list1, list2):
    return list1 + list2

def sort_list(numbers):
    return sorted(numbers)

def filter_list(numbers, condition):
    return list(filter(condition, numbers))

def map_list(numbers, function):
    return list(map(function, numbers))

# Data structure functions
def add_to_set(my_set, item):
    my_set.add(item)

def add_to_dict(my_dict, key, value):
    my_dict[key] = value

def add_to_list_of_lists(my_list, item, sublist):
    my_list[sublist].append(item)


def ping(host):
    import subprocess
    process = subprocess.Popen(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return 'bytes from ' + host in stdout.decode()

# Decorator functions
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

