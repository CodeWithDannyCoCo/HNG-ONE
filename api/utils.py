import requests
import math

def is_armstrong(number):
    # Convert number to string to count digits
    num_str = str(number)
    num_digits = len(num_str)
    
    # Calculate sum of each digit raised to power of number of digits
    digit_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    return digit_sum == number

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def is_perfect(number):
    if number <= 1:
        return False
    
    # Find sum of proper divisors
    divisor_sum = sum(i for i in range(1, number) if number % i == 0)
    return divisor_sum == number

def get_digit_sum(number):
    return sum(int(digit) for digit in str(number))

def get_properties(number):
    properties = []
    
    # Check if number is Armstrong
    if is_armstrong(number):
        properties.append("armstrong")
    
    # Check if odd or even
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    
    return properties

def get_fun_fact(number):
    try:
        response = requests.get(f"http://numbersapi.com/{number}/math")
        if response.status_code == 200:
            return response.text
        return f"{number} is a number"
    except:
        return f"{number} is a number" 