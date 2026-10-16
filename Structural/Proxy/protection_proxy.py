class Car:
    def __init__(self, driver):
        self.driver = driver


    def drive(self):
        print(f'Car is being driven by {self.driver.name}')


class CarProxy:
    def __init__(self, driver):
        self.driver = driver
        self.car = Car(driver)

    def drive(self):
        if self.driver.age >=16:
            self.car.drive()
        else:
            print('Driver is too young')

class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == "__main__":
    driver = Driver('John', 12)
    car = CarProxy(driver)
    car.drive()



