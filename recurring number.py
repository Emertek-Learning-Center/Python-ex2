#in this program we have to calculate the recurring number from a big string full with a number#
################################################################################################

string="12225563377887142152" #string of numbers
list=[] #empty list

#return the number of recurring for a given number
def getOcc(nb,ch):
    counter=0
    for c in ch:
        if c == nb:
            counter +=1
    return counter

#verify if a given number is existe in a list
def isExist(nb,list):
    if not list:
        return False
    for l in list:
        if l['number']==nb:
            return True
    return False

#main porocces        
for s in string:
    nb=getOcc(s,string)
    if not isExist(int(s),list):
        dict={
                'number':int(s),
                'recurring number':nb
            }
        list.append(dict)
#display a list
print(list)
