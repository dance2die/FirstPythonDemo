def minmax(items):
    return min(items), max(items)


print(minmax([1,2,3,4,5,22,-1]))
print(__name__)


try:
    value = int(input("Type 1 ~ 10:"))
except ValueError:
    print("1 ~ 10!")
else:
    if (value > 0) and (value <= 10):
        print("You typed: {}".format(value))
    else:
        print("Wrong, try again!")

