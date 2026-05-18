class Solution:
    def convertTemperature(self, celsius):
        
        # Công thức chuyển đổi:
        # Kelvin = Celsius + 273.15
        # Fahrenheit = Celsius * 1.8 + 32
        
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.8 + 32
        
        return [kelvin, fahrenheit]