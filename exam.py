# void function
# it does not return any value and has no effect on the flow of the code
def said(person, speech):
    print(f"{person} said {speech}")


# value returning function
# has 'return' keyword. Returns value in the script and directly affects the performance of the program
def squared(number):
    return number*number


said("Cato", "Carthago delenda est")

Answer = 56 + squared(32) - (17 + squared(12))
print(Answer)


# object-oriented approach is more concise and allows to reuse the same code multiple times
# class that creates an instance of a client with one's name and work duration. Has a function to calculate fee
class Client:
    def __init__(self, name, days):
        self.name = name
        self.duration = days

    def fee(self, type):
        if type == 1:
            return self.duration * 100
        elif type == 2:
            return self.duration * 200
        elif type == 3:
            return self.duration * 300
        else:
            return print("Invalid input")


cl1 = Client("Cato", 30)
print(cl1.fee(2))

# functional approach requires writing separate functions for different portions of the program
# function to calculate client's fee, taking information from the client object
def fee_counter(client):
    if client["type"] == 1:
        return client["duration"] * 100
    elif client["type"] == 2:
        return client["duration"] * 200
    elif client["type"] == 3:
        return client["duration"] * 300


# client object
cl2 = {
    "name": "Scipio",
    "duration": 45,
    "type": 3
}

print(fee_counter(cl2))
