#fibbonaci
def fibo(urut) :
    listData = [1,1]
    for i in range(2,urut):
        listData.append(listData[i-2] + listData[i-1])
    return listData[urut-1]
print(fibo(8))

#reverse list
import math
def reverseList(theList) :
    for i in range(0, math.floor(len(theList)/2)) :
        tempList = theList[i]
        theList[i] = theList[len(theList) - 1 - i]
        theList[len(theList) - 1 - i] = tempList
    return theList
print(reverseList([1,2,3,4,5,6,7,8]))

#bubble sort
x = [6000, 34, 203, 3, 746, 200, 984, 198, 764, 9, 1]
def bubbleSort(list) :
    for i in range(len(list), 0, -1) :
        for j in range(0,i-1) :
            if (list[j] > list[j + 1]) :
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
    return list
print(bubbleSort(x))

#mean
x = [ 1,2,3,2,5,2,7,2 ]
def getMean(list) :
    sum = 0
    for item in list :
        sum += item

    mean = sum / len(list)
    return mean
print(getMean(x))

# #median
# x = [ 1,2,3,2,5,2,7,2 ]
# def getMedian(list) :
#     list.sort() 
#     median = 0 
#     if (len(list) % 2 != 0) :
#         median = list[floor(len(list) / 2)]
#     else :
#         mid1 = list[(int(len(list) / 2)) - 1]
#         mid2 = list[int(len(list) / 2)]
#         median = (mid1 + mid2) / 2
#     return median
# print(getMedian(x))

#mode
x = [ 1,2,3,2,5,2,7,2 ]
def getMode(list) :
    countList = []
    # create countList
    for num in list :
        check = False
        for list1 in countList :
            if(list1[0] == num) :
                list1[1] += 1
                check = True
        if(check == False) :
            countList.append([num, 0])
    # create list of mode/s
    maxFrequency = 0
    modes = []
    for list1 in countList :
        if (list1[1] > maxFrequency) :
            modes = [list1[0]]
            maxFrequency = list1[1]
        elif (list1[1] == maxFrequency) :
            modes.append(list1[0])
    # if every value appears same amount of times
    if (len(modes) == len(countList)) :
        modes = []
    return modes
print(getMode(x))