import csv
from collections import Counter

with open('SOCR-HeightWeight.csv' , newline = '') as f : 
    reader  = csv.reader(f)
    lists =  list(reader)

lists.pop(0)
data_weight = []
data_height = []
length = len(lists)

for i in range(len(lists)) : 
    height = lists[i][1]
    data_height.append(float(height))

    weight = lists[i][2]
    data_weight.append(float(weight))

def mean() : 
    total_height = 0
    total_weight = 0

    for i in data_height : 
        total_height = total_height + i

    for i in data_weight : 
        total_weight  = total_weight + i

    mean_height = total_height/length
    mean_weight = total_weight/length
    print('')
    print(f'mean-height : {mean_height}')
    print(f'mean-weight : {mean_weight}')
    print('')

def median() : 
    data_height.sort()
    if(length % 2 == 0) : 
        m1 = float(data_height[length//2])
        m2 = float(data_height[length//2 - 1])
        median_height = (m1 + m2)/2
    else : 
        median_height = float(data_height[length//2])

    data_weight.sort()
    if(length % 2 == 0) : 
        m3 = float(data_weight[length//2])
        m4 = float(data_weight[length//2 - 1])
        median_weight = (m3 + m4)/2
    else : 
        median_weight = float(data_weight[length//2])

    print(f'median-height : {median_height}')
    print(f'median-weight : {median_weight}')
    print('')

def mode() :
    data_1 = Counter(data_height)

    mode_range_height = {'60-65' : 0 , '65-70' : 0}

    for height,occurence in data_1.items() :
        if (60 < height < 65) : 
            mode_range_height['60-65'] = mode_range_height['60-65'] + occurence

        elif (65 < height < 70) : 
            mode_range_height['65-70'] = mode_range_height['65-70'] + occurence

        mode_occurence = 0
        mode_range2 = 0
        for range,occurence in mode_range_height.items() : 
            if(occurence > mode_occurence) : 
                mode_range2,mode_occurence = [int(range.split('-')[0]) , int(range.split('-')[1])],occurence

    mode_height = (mode_range2[0] + mode_range2[1])/2
    print(f'mode_height : {mode_height}')

    data_2 = Counter(data_weight)

    mode_range_weigth = {'90-110' : 0 , '110-130' : 0 , '130-150' : 0}

    for weigth,occurence2 in data_2.items() :
        if (90 < weigth < 110) : 
            mode_range_weigth['90-110'] = mode_range_weigth['90-110'] + occurence2

        elif (110 < weigth < 130) : 
            mode_range_weigth['110-130'] = mode_range_weigth['110-130'] + occurence2

        elif (130 < weigth < 150) : 
            mode_range_weigth['130-150'] = mode_range_weigth['130-150'] + occurence2

        mode_occurence2 = 0
        mode_range3 = 0
        for range2,occurence2 in mode_range_weigth.items() : 
            if(occurence2 > mode_occurence2) : 
                mode_range3,mode_occurence2 = [int(range2.split('-')[0]) , int(range2.split('-')[1])],occurence2

    mode_weigth = (mode_range3[0] + mode_range3[1])/2
    print(f'mode_weigth : {mode_weigth}')
    print('')

mean()
median()
mode()
