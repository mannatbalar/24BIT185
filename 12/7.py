class Weather:
    def __init__(self, data):
        self.data = data

    def __contains__(self, item):
        return item in self.data

w = Weather(['rainy', 'sunny', 'cloudy','hot'])

print('sunny' in w)   
print('snowy' in w)   