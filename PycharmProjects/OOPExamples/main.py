class car:

    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        return self.odometer / self.time

if __name__ == '__main__':

    my_car = car()
    print("I'm a car!")
    while True:
        action = input("What should I do? [A]ccelerate , show [O]dometer, or show average [S]peed?").upper()
        if action not in "ABOS" or len(action) != 1:
            print("I don't know how to do that")
            continue
        if action == 'A':
            my_car.accelerate()
            print("Accelerating...")
        if action == 'B':
            my_car.brake()
            print("Braking...")
        elif action == 'O':
            print("The car has driven {} Kilometers", format(my_car.odometer))
        elif action == 'S':
            print("The car's average speed was {} Kph", format(my_car.average_speed()))
        my_car.step()
        


