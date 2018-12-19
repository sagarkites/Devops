class Family:
    def sagar(self):
        print("sagar")


class Home(Family):
    def chanti(self):
        print("vidyasagar")

    def sagar(self):  # overwrite method
        print("scott")


number = Home()
print(number.chanti())
print(number.sagar())