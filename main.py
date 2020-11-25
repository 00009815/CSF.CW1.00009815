# There are 2 classes. 3 students each. The program takes class b student names and IDs from user input and stores them
# in a dictionary. It further checks ID similarities between classes, separates names and ID for further usage,
# generates seat numbers and pairs for works between classes.


def data_addition(key, value):  # function gets parameters from user input and passes into dictionary
    class_b[key] = value


def similarity_check(first, second):  # function gets two ID lists as parameters
    for i in range(len(first)):
        for j in range(len(second)):
            if first[i] == second[j]:       # Both lists have 3 elements and are sorted, the identical elements will be
                return True
    return False


class_a = {             # the data about student names and IDs is separated in two classes
    "Mike": "153",      # and stored in dictionaries for better readability
    "John": "684",
    "Daniel": "185"
}
class_a_names = []      # lists for separate student names and IDs for future usage
class_a_ids = []        # initially, list is used for IDs, so the data from dictionaries can be pushed there

class_b = dict()        # a dictionary created for the class b
class_b_names = []
class_b_ids = []

print("Input three sets of student data")
for i in range(3):                             # there are 3 students per class, so the loop will ask for input 3 times
    data_addition(input("Name: "), input("ID: "))

for name, ids in class_a.items():          # item method is used to create a sequence of tuples containing names and IDs
    class_a_names.append(name)             # names and IDs are pushed to separate lists
    class_a_ids.append(ids)
class_a_ids.sort()                         # sort IDs in the ascending order for further usage
for name, ids in class_b.items():          # similar procedure is done with the class b, but the data is pushed to
    class_b_names.append(name)             # respective lists
    class_b_ids.append(ids)
class_b_ids.sort()

if similarity_check(class_a_ids, class_b_ids):      # check if there are identical IDs in different classes
    print("There are the same IDs in two classes")  # warning if there are identical IDs
else:
    class_a_ids = tuple(class_a_ids)  # if there are no identical IDs, the ID lists are turned into immutable tuples
    class_b_ids = tuple(class_b_ids)  # to prevent accidental changes

print("Class A: ")
print(class_a)
print("Class B: ")
print(class_b)
print("Seat numbers for class A: ")
print(class_a_seats)
print("Seat numbers for class B: ")
print(class_b_seats)
print("Pairs for a collaboration work: ")
print(collaboration_list)
