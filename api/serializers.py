from rest_framework import serializers
import math
import requests

class NumberClassificationSerializer(serializers.Serializer):
    number = serializers.IntegerField(required=True)
    is_prime = serializers.BooleanField(read_only=True)
    is_perfect = serializers.BooleanField(read_only=True)
    properties = serializers.ListField(child=serializers.CharField(), read_only=True)
    digit_sum = serializers.IntegerField(read_only=True)
    fun_fact = serializers.CharField(read_only=True)

    def validate_number(self, value):
        if not isinstance(value, int):
            raise serializers.ValidationError("Number must be an integer")
        return value

    def to_representation(self, instance):
        number = instance
        
        # Calculate properties
        properties = []
        
        # Check if Armstrong number
        num_str = str(number)
        num_digits = len(num_str)
        digit_sum_powered = sum(int(digit) ** num_digits for digit in num_str)
        if digit_sum_powered == number:
            properties.append("armstrong")
        
        # Check if odd/even
        properties.append("odd" if number % 2 else "even")
        
        # Calculate digit sum
        digit_sum = sum(int(digit) for digit in num_str)
        
        # Check if prime
        is_prime = True
        if number < 2:
            is_prime = False
        else:
            for i in range(2, int(math.sqrt(number)) + 1):
                if number % i == 0:
                    is_prime = False
                    break
        
        # Check if perfect
        is_perfect = False
        if number > 1:
            divisor_sum = sum(i for i in range(1, number) if number % i == 0)
            is_perfect = divisor_sum == number
        
        # Get fun fact
        try:
            response = requests.get(f"http://numbersapi.com/{number}/math")
            fun_fact = response.text if response.status_code == 200 else f"{number} is a number"
        except:
            fun_fact = f"{number} is a number"
        
        return {
            'number': number,
            'is_prime': is_prime,
            'is_perfect': is_perfect,
            'properties': properties,
            'digit_sum': digit_sum,
            'fun_fact': fun_fact
        }