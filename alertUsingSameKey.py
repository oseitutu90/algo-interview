def alertNames(keyName, keyTime):
    """Alert Using Same Key-Card Three or More Times in a One Hour Period"""
    # Write your code here
    keyTime = [convertToMinutes(time) for time in keyTime]
    # store in a dictionary
    keyDict = {}
    for i in range(len(keyName)):
        if keyName[i] in keyDict: # if keyName is already in the dictionary
            keyDict[keyName[i]].append(keyTime[i])
        else:
            keyDict[keyName[i]] = [keyTime[i]]
    # print(keyDict)
    # check if the time difference is less than 60
    alert = []
    for key in keyDict: # iterate through the dictionary
        for i in range(len(keyDict[key]) - 2): # iterate through the list
            if keyDict[key][i + 2] - keyDict[key][i] <= 60:
                alert.append(key)
                break
    return sorted(alert)
    
def convertToMinutes(time):
    """Convert time to minutes"""
    time = time.split(":")
    return int(time[0]) * 60 + int(time[1])

print(alertNames(["daniel","daniel","daniel","luis","luis","luis","luis"],["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]))
print(alertNames(["daniel","daniel","daniel","luis","luis","luis","luis"], ["10:00","10:00","11:00","09:00","11:00","13:00","15:00"]))
print(alertNames(["alice","alice","alice","bob","bob","bob","bob"], ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]))