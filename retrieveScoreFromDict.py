"""Save and retrieve average score  from dictionary within a time range"""
def saveScore(name, score, time):
    """Save score to dictionary"""
    # Write your code here
    time = convertToMinutes(time)
    if name in scoreDict:
        scoreDict[name].append((time, score))
    else:
        scoreDict[name] = [(time, score)]
    return scoreDict

def retrieveScore(name, startTime, endTime):
    """Retrieve average score from dictionary within a time range"""
    # Write your code here
    startTime = convertToMinutes(startTime)
    endTime = convertToMinutes(endTime)
    if name in scoreDict:
        scores = [score for time, score in scoreDict[name] if startTime <= time <= endTime]
        if scores:
            return sum(scores) / len(scores)
    return 0

