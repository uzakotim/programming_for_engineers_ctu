#!/usr/bin/python3
# Programming for Engineers - KYR 2021
# Optimal Expedition
# CVUT
# Timur Uzakov
from itertools import combinations

def toNumber(global_day,global_month):
        sum = 0
        for i in range(global_month):
            if i==0:
                sum+= 0
            if i==1:
                sum+= 31
            if i==2:
                sum+= 28
            if i==3:
                sum+= 31
            if i==4:
                sum+= 30
            if i==5:
                sum+= 31
            if i==6:
                sum+= 30
            if i==7:
                sum+= 31
            if i==8:
                sum+= 31
            if i==9:
                sum+= 30
            if i==10:
                sum+= 31
            if i==11:
                sum+= 30
        sum+=global_day
        return sum

def main():
    n = input()
    sentences = []
    global_day   = ''
    global_month = ''
    for i in range(int(n)):
        sentence = input()
        sentence = sentence.replace(","," ")
        sentence = sentence.replace("\""," ")
        sentence = sentence.replace("?"," ")
        sentence = sentence.replace("!"," ")
        if sentence[-1] == '.':
            sentence = sentence[:-1]
        sentence = list(sentence.split())
        
        sentences.append(sentence)
    expeditions = []
    dates = []
    
    for i in range(int(n)):
        expedition = []
        date = []
        for j,word in enumerate(sentences[i]):
            if '.' in word:
                if  word[-1]=='.':
                    word = word[:-1]
                tmp_list = word.split('.')
                day   = int(tmp_list[0])
                month = int(tmp_list[1])
            
                if month <13 and month>0:
                    global_month = str(month)
                else:
                    continue
                if day < 32 and day > 0:
                    if month == 2 and day <29:
                        global_day = str(day)
                    if month != 2:
                        global_day = str(day)
                else:
                    continue                
            if (global_day!='') and (global_month!=''):

                expedition.append(toNumber(int(global_day),int(global_month)))
                date.append(global_day+"."+global_month+".")
        
            global_month = ''
            global_day = ''

        dates.append(date)
        expeditions.append(expedition)

    durations = []
    trips = [0]*int(n)
    trip_elements = []
    considerations = []
    index = 0
    indexes = []
    
    expeditions_sorted = sorted(expeditions)
    expeditions_sorted = [x for x in expeditions_sorted if x!=[]]
    expeditions_indexes = []   

    look_up = [0]*len(expeditions)

    for sorted_expedition in expeditions_sorted:
        for i,unsorted_expedition in enumerate(expeditions):
            if unsorted_expedition == sorted_expedition:                
                if look_up[i] == 0:
                    expeditions_indexes.append(i)
                    look_up[i] = 1
                else: 
                    continue
        
    

    for line in expeditions:
        max_day = []
        min_day = []

        if line != []:
            max_day = max(line)
            min_day = min(line)
            trip_elements.append(max_day)
            trip_elements.append(min_day)
            duration = max_day-min_day+1
            trips[index] = [min_day,max_day,duration]
            indexes.append(index)
        else: 
            trips[index] = []
        index+=1


    considerations = [comb for comb in combinations(expeditions_indexes,2)]

    #Checks
    for j,comb in enumerate(considerations):

        for i in trip_elements:
            if trips[comb[0]][1] < i and i < trips[comb[1]][0]:
                considerations[j] = []
                break
            # if second expedition starts at duration of the first:
            if trips[comb[0]][0] < trips[comb[1]][0] < trips[comb[0]][1]:
                considerations[j] = []
                break
            # if first expedition start at duration of the second:
            if trips[comb[1]][0] < trips[comb[0]][0] < trips[comb[1]][1]:
                considerations[j] = []
                break
            # if second expedition ends at duration of the first:
            if trips[comb[0]][0] < trips[comb[1]][1] < trips[comb[0]][1]:
                considerations[j] = []
                break
            # if first expedition ends at duration of the second:
            if trips[comb[1]][0] < trips[comb[0]][1] < trips[comb[1]][1]:
                considerations[j] = []
                break
        # 7 Days Check
        if abs(trips[comb[1]][0] - trips[comb[0]][1]) <=7:
            # print("Less then seven days break")
            considerations[j] = []
        # 7 Days Check
        if abs(trips[comb[0]][0] - trips[comb[1]][1]) <=7:
            # print("Less then seven days break")
            considerations[j] = []

    considerations = [x for x in considerations if x!=[]]
    durations = [(trips[comb[0]][2]+trips[comb[1]][2]) for comb in considerations]
    
    expedition_array = [] # consist of line number  and two dates
    max_duration = max(durations)
    
    output = ''
    output += str(max_duration)
    output += '\n'

    for comb in considerations:
        if trips[comb[0]][2] + trips[comb[1]][2] == max_duration:
            # comb[0] - expedition 1
            # comb[1] - expedition 2      
            for i in range(2):
                expedition_array = ''
                expedition_array+= str(comb[i]+1)
                expedition_array+=' '
                expedition_array+= dates[comb[i]][expeditions[comb[i]].index(trips[comb[i]][0])]
                expedition_array+=' '
                try:
                    expedition_array+= dates[comb[i]][expeditions[comb[i]].index(trips[comb[i]][1])]
                except:
                    expedition_array+= dates[comb[i]][expeditions[comb[i]].index(trips[comb[i]][0])]
                if i == 0:
                    expedition_array+=' '
                output+=expedition_array
            output+='\n'
    output = output[:-1]
    print(output)
    
if __name__ == "__main__":
	main()    
	    
