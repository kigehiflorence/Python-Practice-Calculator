import math

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Division by zero not allowed")
        return a / b

    @staticmethod
    def power(a, b):
        return a ** b

    @staticmethod
    def sqrt(a):
        if a < 0:
            raise ValueError("Square root of negative number not allowed")
        return math.sqrt(a)
