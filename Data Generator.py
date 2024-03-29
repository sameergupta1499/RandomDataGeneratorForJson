import random
import string

class DocumentData:
    key = ""
    value = ""


class FieldValueSpecs:
    space = False
    nospace = True
    valueLength=0
    number = False
    fieldType = "noSpacedCharacterString"
    wildString = ""
    isWildString = False


def divide_number(number, parts_number, allow_zero = False):
    if(number == parts_number):                     #if number number of parts is equal to the length
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
    random.shuffle(parts)
    return parts



def countAsterisk(s):
    totalAsterisk = s.count("*") - s.count("\*")
    return totalAsterisk                            #\* is a special character.

def countQuestionMark(s):
    totalQM = s.count("?")-s.count("\?")            #\? is a special character.
    return totalQM

def generateNoSpacedWildString(length , wildString):
    totalAsterisk = countAsterisk(wildString)
    totalQuestionMark = countQuestionMark(wildString)
    #print(length,totalAsterisk)
    parts = divide_number(length-totalQuestionMark,totalAsterisk)   #number of character per *
    #print(parts)
    value = ""
    currentAstrickIndex = 0                                   #parts index basically
    for s in wildString:
        if(s == "*"):
            value += generateNoSpacedCharacterString(parts[currentAstrickIndex])
            currentAstrickIndex += 1
        elif(s == "?"):
            value += generateNoSpacedCharacterString(1)
        else:
            value += s
    return value

def generateSpacedWildString(length , wildString):
    totalAsterisk = countAsterisk(wildString)
    totalQuestionMark = countQuestionMark(wildString)
    parts = divide_number(length-totalQuestionMark,totalAsterisk)   #number of character per *
    value = ""
    currentAstrickIndex = 0
    for s in wildString:
        if(s == "*"):
            value += generateSpacedCharacterString(parts[currentAstrickIndex])
            currentAstrickIndex += 1
        elif(s == "?"):
            value += generateSpacedCharacterString(1)
        else:
            value += s
    return value

def generateNumbers(length):
    rangeStart = 10**(length-1)
    rangeEnd = (10**length)-1
    return random.randrange(rangeStart, rangeEnd)

def generateNoSpacedCharacterString(length):
    str=""
    for currentIndex in range(length):
        str += random.choice(string.ascii_letters)
    return str

def generateSpacedCharacterString(length):
    str=""
    nextSpacedIndex = random.randrange(1,11)
    for currentIndex in range(length):
        if(currentIndex == nextSpacedIndex):
            str += " "
            nextSpacedIndex += random.randrange(2,11)
        else:
            str += random.choice(string.ascii_letters)
    return str

def parseDocumentTemplate(documentTemplate):       #document template is list type containing dictionaries. ex- [{"key1":"value"}, {"key2":[[2,6],"nospace"]}, {"key3":"value"}, {"key4":"value"}, {"key5":"value"}]
    document = {}
    for field in documentTemplate:                 #{"key" : value}   field is dictionary type.
        #print(field)
        key, value= parseField(field)
        document[key] = value
    return document                         #returns document of dictionary type

def parseField(field):
    key, value= parseKeyValue(field)        # string,list = parseKeyValue(dictionary type)
    value = parseFieldValue(value)       #value contains templates value data[[2,6],"nospace"].
    return key,value

def parseKeyValue(field):
    key = ""
    value = ""
    for item in field.items():
        key = item[0]
        value = item[1]
    return key, value                           # string,list = parseKeyValue(dictionary type)

def parseFieldValue(value):                 #value contains templates value data,value is of list type [[2,6],"nospace"].
    fieldValueSpecs = FieldValueSpecs()
    for attribute in value:
        fieldValueSpecs = setFieldValueSpecs(attribute,fieldValueSpecs)
    fieldValueSpecs.fieldType = getValueType(fieldValueSpecs)
    #print(fieldValueSpecs.fieldType)
    #print(fieldValueSpecs.space,fieldValueSpecs.nospace,fieldValueSpecs.number,fieldValueSpecs.valueLength)
    value = generateFieldValue(fieldValueSpecs)
    return value

def generateFieldValue(fieldValueSpecs):
    if(fieldValueSpecs.fieldType == "number"):
        return generateNumbers(fieldValueSpecs.valueLength)
    if(fieldValueSpecs.fieldType == "noSpacedCharacterString"):
        return generateNoSpacedCharacterString(fieldValueSpecs.valueLength)
    if(fieldValueSpecs.fieldType == "spacedCharacterString"):
        return generateSpacedCharacterString(fieldValueSpecs.valueLength)
    if(fieldValueSpecs.fieldType == "spacedWildString"):
        return generateSpacedWildString(fieldValueSpecs.valueLength , fieldValueSpecs.wildString)
    if(fieldValueSpecs.fieldType == "noSpacedWildString"):
        return generateNoSpacedWildString(fieldValueSpecs.valueLength , fieldValueSpecs.wildString)



#Get Value type
def getValueType(fieldValueSpecs):
    if(fieldValueSpecs.isWildString == True and fieldValueSpecs.space == True):
        return "spacedWildString"
    if(fieldValueSpecs.isWildString == True and fieldValueSpecs.nospace == True):
        return "noSpacedWildString"
    if(fieldValueSpecs.number == True):
        return "number"
    if(fieldValueSpecs.space == True):
        return "spacedCharacterString"
    if(fieldValueSpecs.nospace == True):
        return "noSpacedCharacterString"



"""def validateSpaceOccurrence(fieldValueSpecs):
    if(fieldValueSpecs.space == True and fieldValueSpecs.nospace==True):
        return True
    return False
"""

def setFieldValueSpecs(attribute,fieldValueSpecs):
    if(attribute == "nospace"):
        #if(validateSpaceOccurrence(fieldValueSpecs) == True):
        fieldValueSpecs.nospace = True
        fieldValueSpecs.space = False
    elif(attribute == "space"):
        #if(validateSpaceOccurrence(fieldValueSpecs) == True):
        fieldValueSpecs.nospace = False
        fieldValueSpecs.space = True
    elif(attribute == "number"):
        fieldValueSpecs.number = True
        fieldValueSpecs.space = False
    elif(type(attribute) == list):
        if(type(attribute[0]) == list):
            fieldValueSpecs.wildString = (attribute[0])[0]
            fieldValueSpecs.isWildString = True
        if(type(attribute[0]) == int):
            fieldValueSpecs.valueLength = getAttributeLength(attribute)
    else:
        return False
    return fieldValueSpecs

def getAttributeLength(attribute):
    if( attribute[0] == attribute[1] ):
        return attribute[0]
    return random.randrange(attribute[0],attribute[1])



# 10,[{"key",{value}},{},{}]

def jsonDataGenerator(totalDocuments = 1, documentTemplate = []):
    collection=[]
    for x in range(totalDocuments):
        document = parseDocumentTemplate(documentTemplate)      #parseDocumentTemplate should return a dictionary
        collection.append(document)
    return collection                                           #returns list of dictionaries

jsonData = jsonDataGenerator(1,[{"username":[ [2,20],"nospace" ]},
                     {"email":[ [4,90] , [["*@*.*.com?"]] , "space"]},
                     {"phoneNumber":[ [10,10],"number" ]},
                     {"title":[ [6,90],"space" ]},
                     {"content":[ [200,600],"space"] }] )

for dict in jsonData:
    print(dict)


