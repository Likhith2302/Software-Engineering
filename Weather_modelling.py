def quadratic_weather_model(a, b, c, x):
    y = a * x**2 + b * x + c
    return y
with open('input.txt', 'r') as file:
    for line in file:
        a, b, c, x = map(float, line.split())
        result = quadratic_weather_model(a, b, c, x)
        print(f"For x={x}, the result is: {result}")


Output:-
For x=5.0, the result is: 87.5
