import random,string
mylist = [
  { "name": 12939, "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]
dict = {"sameer":0}

def divide_number(number, parts_number, allow_zero = False):
    if(number == parts_number):
        return [1]*number

    if (parts_number > number):
        raise ValueError("Number of parts can't be higher than the length")

    parts = []
    number_rest = number

    for i in range(1, parts_number + 1):
        if (i == parts_number):
            parts.append(number_rest)
            break
        else:
            new_number = random.randint(0, number_rest) if allow_zero else random.randint(1, (number_rest - (parts_number - i)) // 2)

        number_rest -= new_number
        parts.append(new_number)

    return parts
print(divide_number(4,2))

def getAttributeLength(attribute):
    if( attribute[0] == attribute[1] ):
        return attribute[0]
    return random.randrange(attribute[0],attribute[1],1)

def generateNumbers(length):
    rangeStart = 10**(length-1)
    rangeEnd = (10**length)-1
    return random.randrange(rangeStart, rangeEnd)

#print(random.randrange(1,10))
str = string.ascii_letters
#print(len(str))
#'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

a=11
divide = 4
#print(countAsterisk(s))
arr = [1]*10
print(type(arr))
arr2 = [1,3,4,5,66,7,8]
random.shuffle(arr2)
print(arr2)
