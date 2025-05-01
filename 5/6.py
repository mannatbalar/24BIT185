def q6():
    fahrenheit = [32, 65, 101, 22, 50]  
    celsius = []

    for f in fahrenheit:
        celsius.append((f - 32) * 5 / 9)

    print(celsius)
