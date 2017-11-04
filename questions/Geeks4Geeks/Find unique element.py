#code

class arrayElement:
    
    def __init__(self,number):
        self.name = number
        self.occurance = 1

def findUniqueElement(n,k,array):

    elements = []
    elements.append(arrayElement(array[0]))
    
    for i in range(1,len(array)):
        skipFlag = False;    
        for j in range(0,len(elements)):
            if (elements[j].name == array[i]):
                # print("if")
                elements[j].occurance = elements[j].occurance + 1
                # print("added to" + elements[j].name)
                skipFlag = True;
            
        if skipFlag == False:
            # print("else")
            newNum = arrayElement(array[i])
            # print("adding " + array[i])
            elements.append(newNum)

    for i in range(0,len(elements)):
        if (elements[i].occurance == 1):
            print(str(elements[i].name))


# thing = "6 2 5 2 2 6 6"
# array = thing.split()
# findUniqueElement('7','3',array)


testCases = int(input())
while testCases > 0:
    n,k = input().split()
    array = input().split()
    findUniqueElement(n,k,array)
    testCases = testCases - 1