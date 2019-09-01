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

def getAttributeLength(attribute):
    if( attribute[0] == attribute[1] ):
        return attribute[0]
    return random.randrange(attribute[0],attribute[1],1)

def generateNumbers(length):
    rangeStart = 10**(length-1)
    rangeEnd = (10**length)-1
    return random.randrange(rangeStart, rangeEnd)

print(random.randrange(1,10))
str = string.ascii_letters
print(len(str))
#'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
