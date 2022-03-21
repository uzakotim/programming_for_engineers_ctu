#!/usr/bin/python3
# Programming for Engineers - KYR 2021
# Optimal Expedition
# CVUT
# Timur Uzakov
from itertools import combinations

def toNumber(global_day,global_month):
        
        calendar = {
            1:{
                1:1,
                2:2,
                3:3,
                4:4,
                5:5,
                6:6,
                7:7,
                8:8,
                9:9,
                10:10,
                11:11,
                12:12,
                13:13,
                14:14,
                15:15,
                16:16,
                17:17,
                18:18,
                19:19,
                20:20,
                21:21,
                22:22,
                23:23,
                24:24,
                25:25,
                26:26,
                27:27,
                28:28,
                29:29,
                30:30,
                31:31
            },
            2:{
                1:32,
                2:33,
                3:34,
                4:35,
                5:36,
                6:37,
                7:38,
                8:39,
                9:40,
                10:41,
                11:42,
                12:43,
                13:44,
                14:45,
                15:46,
                16:47,
                17:48,
                18:49,
                19:50,
                20:51,
                21:52,
                22:53,
                23:54,
                24:55,
                25:56,
                26:57,
                27:58,
                28:59
            },
            3:{
                1:60,
                2:61,
                3:62,
                4:63,
                5:64,
                6:65,
                7:66,
                8:67,
                9:68,
                10:69,
                11:70,
                12:71,
                13:72,
                14:73,
                15:74,
                16:75,
                17:76,
                18:77,
                19:78,
                20:79,
                21:80,
                22:81,
                23:82,
                24:83,
                25:84,
                26:85,
                27:86,
                28:87,
                29:88,
                30:89,
                31:90
            },
            4:{
                1:91,
                2:92,
                3:93,
                4:94,
                5:95,
                6:96,
                7:97,
                8:98,
                9:99,
                10:100,
                11:101,
                12:102,
                13:103,
                14:104,
                15:105,
                16:106,
                17:107,
                18:108,
                19:109,
                20:110,
                21:111,
                22:112,
                23:113,
                24:114,
                25:115,
                26:116,
                27:117,
                28:118,
                29:119,
                30:120
            },
            5:{
                1:121,
                2:122,
                3:123,
                4:124,
                5:125,
                6:126,
                7:127,
                8:128,
                9:129,
                10:130,
                11:131,
                12:132,
                13:133,
                14:134,
                15:135,
                16:136,
                17:137,
                18:138,
                19:139,
                20:140,
                21:141,
                22:142,
                23:143,
                24:144,
                25:145,
                26:146,
                27:147,
                28:148,
                29:149,
                30:150,
                31:151,
            },
            6:
            {
                1:152,
                2:153,
                3:154,
                4:155,
                5:156,
                6:157,
                7:158,
                8:159,
                9:160,
                10:161,
                11:162,
                12:163,
                13:164,
                14:165,
                15:166,
                16:167,
                17:168,
                18:169,
                19:170,
                20:171,
                21:172,
                22:173,
                23:174,
                24:175,
                25:176,
                26:177,
                27:178,
                28:179,
                29:180,
                30:181
            },
            7:
            {
                1:182,
                2:183,
                3:184,
                4:185,
                5:186,
                6:187,
                7:188,
                8:189,
                9:190,
                10:191,
                11:192,
                12:193,
                13:194,
                14:195,
                15:196,
                16:197,
                17:198,
                18:199,
                19:200,
                20:201,
                21:202,
                22:203,
                23:204,
                24:205,
                25:206,
                26:207,
                27:208,
                28:209,
                29:210,
                30:211,
                31:212,
            },
            8:
            {
                1:213,
                2:214,
                3:215,
                4:216,
                5:217,
                6:218,
                7:219,
                8:220,
                9:221,
                10:222,
                11:223,
                12:224,
                13:225,
                14:226,
                15:227,
                16:228,
                17:229,
                18:230,
                19:231,
                20:232,
                21:233,
                22:234,
                23:235,
                24:236,
                25:237,
                26:238,
                27:239,
                28:240,
                29:241,
                30:242,
                31:243
            },
            9:
            {
                1:244,
                2:245,
                3:246,
                4:247,
                5:248,
                6:249,
                7:250,
                8:251,
                9:252,
                10:253,
                11:254,
                12:255,
                13:256,
                14:257,
                15:258,
                16:259,
                17:260,
                18:261,
                19:262,
                20:263,
                21:264,
                22:265,
                23:266,
                24:267,
                25:268,
                26:269,
                27:270,
                28:271,
                29:272,
                30:273   
            },
            10:
            {
                1:274,
                2:275,
                3:276,
                4:277,
                5:278,
                6:279,
                7:280,
                8:281,
                9:282,
                10:283,
                11:284,
                12:285,
                13:286,
                14:287,
                15:288,
                16:289,
                17:290,
                18:291,
                19:292,
                20:293,
                21:294,
                22:295,
                23:296,
                24:297,
                25:298,
                26:299,
                27:300,
                28:301,
                29:302,
                30:303,
                31:304
            },
            11:
            {
                1:305,
                2:306,
                3:307,
                4:308,
                5:309,
                6:310,
                7:311,
                8:312,
                9:313,
                10:314,
                11:315,
                12:316,
                13:317,
                14:318,
                15:319,
                16:320,
                17:321,
                18:322,
                19:323,
                20:324,
                21:325,
                22:326,
                23:327,
                24:328,
                25:329,
                26:330,
                27:331,
                28:332,
                29:333,
                30:334
            },
            12:
            {
                1:335,
                2:336,
                3:337,
                4:338,
                5:339,
                6:340,
                7:341,
                8:342,
                9:343,
                10:344,
                11:345,
                12:346,
                13:347,
                14:348,
                15:349,
                16:350,
                17:351,
                18:352,
                19:353,
                20:354,
                21:355,
                22:356,
                23:357,
                24:358,
                25:359,
                26:360,
                27:361,
                28:362,
                29:363,
                30:364,
                31:365
            }
        }

        return calendar[global_month][global_day]

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

    # Combinatorial part

    considerations = [comb for comb in combinations(expeditions_indexes,2)]

    # Optimization part
    trip_elements = sorted(set(trip_elements))
    #Checks
    for j,comb in enumerate(considerations):

        index_end_first = trip_elements.index(trips[comb[0]][1])
        index_start_second = trip_elements.index(trips[comb[1]][0])

        # if there is a start or end in between
        if index_start_second-index_end_first>1:
            considerations[j] = []
            continue
        
        # if second expedition starts at duration of the first:
        if trips[comb[0]][0] < trips[comb[1]][0] < trips[comb[0]][1]:
            considerations[j] = []
            continue
        # if first expedition start at duration of the second:
        if trips[comb[1]][0] < trips[comb[0]][0] < trips[comb[1]][1]:
            considerations[j] = []
            continue
        # if second expedition ends at duration of the first:
        if trips[comb[0]][0] < trips[comb[1]][1] < trips[comb[0]][1]:
            considerations[j] = []
            continue
        # if first expedition ends at duration of the second:
        if trips[comb[1]][0] < trips[comb[0]][1] < trips[comb[1]][1]:
            considerations[j] = []
            continue


        # 7 Days Check
        if abs(trips[comb[1]][0] - trips[comb[0]][1]) <=7:
            # print("Less then seven days break")
            considerations[j] = []
            continue
        # 7 Days Check
        if abs(trips[comb[0]][0] - trips[comb[1]][1]) <=7:
            # print("Less then seven days break")
            considerations[j] = []
            continue

    considerations = [x for x in considerations if x!=[]]
    durations = sorted([(trips[comb[0]][2]+trips[comb[1]][2]) for comb in considerations])

    expedition_array = '' # consist of line number  and two dates
    
    max_duration = durations[-1]
    

    # Printing

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
	    
