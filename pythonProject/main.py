# Press the green button in the gutter to run the script.
def toMin(hhmm):
    [hours,minutes] = hhmm.split(':')
    return int(hours)*60+int(minutes)
def toHHMM(minutes):
    hours = str(minutes//60)
    if len(hours)==1:
        hours = '0'+hours
    minstr = str(minutes%60)
    if len(minstr) == 1:
        minstr = '0'+minstr
    return hours+':'+minstr


if __name__ == '__main__':
    hhmm = "12:15"
    startMin = toMin("8:00")
    endMin = toMin("17:59")

    array1 = [-1 for i in range(endMin)]
    for i in range(len(array1)):
        if i>startMin:
            array1[i] = 0

    propositions = []

    [G,P] =[int(x) for x in input().split(", ")]
    names = sorted([x for x in input().split(", ")])
    rooms = [x for x in input().split(", ")]

    for i in range(P):
        propositions.append(list(input().split(", ")))
    conflict_times = []
    timeline = []
    for name in names:
        timeline = array1.copy()
        for pr in propositions:
            if (pr[0] == name):
                start_time = toMin(pr[1])
                end_time   = toMin(pr[2])
                for k in range(len(timeline)):
                    if (k >= start_time) and (k <= end_time):
                        timeline[k] += 1
        conflict_times.append(toHHMM(len([i for i in timeline if i > 1])))
    # conflict times have the same indexecs as names
    # sorting conflict times
    indexes = sorted(range(len(conflict_times)),key=conflict_times.__getitem__)
    free_times= []
    for room in rooms:
        timeline = array1.copy()
        for pr in propositions:
            if pr[-1] == room:
                start_time = toMin(pr[1])
                end_time = toMin(pr[2])
                for k in range(len(timeline)):
                    if (k >= start_time) and (k <= end_time):
                        timeline[k] += 1
        free_times.append(toHHMM(timeline.count(0)+2))

    output =''
    output += free_times[0]+' '
    output += free_times[1]+'\n'
    for i in range(len(conflict_times)):
        output+= sorted(conflict_times)[i]+' '+ names[indexes[i]]
        output+='\n'
    print(output[:-1])


    """A, 12:15, 13:00, X"""

    # counter = 0
    # for i in array1:
        # if i>=0:
        #     counter+=1
    # print(counter)
    # print(endMin-startMin)
    # print(startMin)
    # print(endMin)
"""
2, 8
A, B
X, Y
A, 12:15, 13:00, X
A, 13:15, 14:00, X
A, 12:45, 13:30, Y
A, 13:45, 14:30, Y
B, 14:15, 15:00, X
B, 15:15, 16:00, X
B, 14:45, 15:30, Y
B, 15:45, 16:30, Y
"""