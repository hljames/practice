def urlify(s,truelength):
    new_index = len(s)
    for i in reversed(range(truelength)):
        if s[i] == ' ':
            s[new_index - 3:new_index] = '%20'
        else:
            s[new_index - 1] = s[i]
