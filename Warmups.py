# 12.4.17
def reverse_order(first_name, last_name):
    print("%s, %s" % (last_name, first_name))
    print(last_name + "" + first_name)  # Concatenation


def reverse_order():
    first_name = input("First name")
    last_name = input("Last name")
    print("%s, %s" % (last_name, first_name))


def add_py(name):
    print("%s.py" % name)  # Solution 1
    print(name + ".py")  # Solution 2


def add(int1, int2, int3):
    print(int1 + int2 + int3)


add(90, 900, 9000)


def repeat(string):
    print(string)
    print(string)
    print(string)

    for x in range(3):
        print(string)


print(repeat("Bonjour!"))


def date(month, day, year):
    print(month + "/" + day + "/" + year)
    print("%s/%s/%s" % (month, day, year))  # Pair with date(12, 8, 17)


date("12", "8", "17")
