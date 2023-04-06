PI = 3.1415926535

def number_input():
    return float(input('숫자 입력> '))

def get_circumference(radius):
    return 2 * PI * radius

def get_area(radius):
    return PI * radius * radius

def print_name():
    print(__name__)

