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

