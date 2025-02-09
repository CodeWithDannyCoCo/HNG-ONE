from rest_framework import serializers
import math
import requests
from django.core.cache import cache
from functools import lru_cache

@lru_cache(maxsize=1000)  # Cache up to 1000 number calculations
def calculate_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    return sum(int(digit) ** num_digits for digit in num_str) == number

@lru_cache(maxsize=1000)
def calculate_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    # Only check odd numbers up to square root
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

@lru_cache(maxsize=1000)
def calculate_perfect(number):
    if number < 2:
        return False
    divisor_sum = 1
    # Optimize by checking up to square root
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            divisor_sum += i
            if i != number // i:  # Avoid counting square root twice
                divisor_sum += number // i
    return divisor_sum == number

class NumberClassificationSerializer(serializers.Serializer):
    number = serializers.IntegerField(required=True)
    is_prime = serializers.BooleanField(read_only=True)
    is_perfect = serializers.BooleanField(read_only=True)
    properties = serializers.ListField(child=serializers.CharField(), read_only=True)
    digit_sum = serializers.IntegerField(read_only=True)
    fun_fact = serializers.CharField(read_only=True)

    def validate_number(self, value):
        try:
            # Ensure it's a positive integer
            if value < 0:
                raise serializers.ValidationError("Number must be a positive integer")
            if value > 1000000:  # Limit size for performance
                raise serializers.ValidationError("Number must be less than or equal to 1,000,000")
            return value
        except TypeError:
            raise serializers.ValidationError("Invalid number format")

    def get_fun_fact(self, number):
        # Try to get from cache first
        cache_key = f'fun_fact_{number}'
        fun_fact = cache.get(cache_key)
        if fun_fact:
            return fun_fact
        
        try:
            response = requests.get(
                f"http://numbersapi.com/{number}/math",
                timeout=0.5  # Reduced timeout to 500ms
            )
            fun_fact = response.text if response.status_code == 200 else f"{number} is a number"
            # Cache for 24 hours
            cache.set(cache_key, fun_fact, 60 * 60 * 24)
            return fun_fact
        except:
            return f"{number} is a number"

    def to_representation(self, instance):
        try:
            number = int(instance)
            
            # Basic properties (very fast)
            properties = ['odd' if number % 2 else 'even']
            digit_sum = sum(int(digit) for digit in str(number))
            
            # Cached/optimized calculations
            if calculate_armstrong(number):
                properties.append('armstrong')
            
            is_prime = calculate_prime(number)
            is_perfect = calculate_perfect(number)
            
            # Get cached fun fact
            fun_fact = self.get_fun_fact(number)
            
            return {
                'number': number,
                'is_prime': is_prime,
                'is_perfect': is_perfect,
                'properties': properties,
                'digit_sum': digit_sum,
                'fun_fact': fun_fact
            }
        except Exception as e:
            # Minimal response for errors
            return {
                'number': int(instance),
                'is_prime': False,
                'is_perfect': False,
                'properties': ['even'] if int(instance) % 2 == 0 else ['odd'],
                'digit_sum': 0,
                'fun_fact': f"{instance} is a number"
            }