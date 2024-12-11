def quadratic_weather_model(a, b, c, x):
    y = a * x**2 + b * x + c
    return y
with open('coeff.txt', 'r') as file:
    for line in file:
        a, b, c, x = map(float, line.split())
        result = quadratic_weather_model(a, b, c, x)
        print(f"For x={x}, the result is: {result}")


Output:-
For x=4.0, the result is: 75.0
For x=3.0, the result is: 115.0
For x=2.0, the result is: -20.0
