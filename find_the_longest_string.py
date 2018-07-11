def find_the_longest_string(x):
    string = []
    for i in range(len(x) - 1):
        longest = x[i:len(x)]
        for i in range(len(x) - i):
            if len(longest) != len(set(longest)):
                longest = longest[0:len(longest) - 1]
        string = np.append(string,longest)
    string = np.append(string,x[-1])
    count = []
    for i in range(len(x)):
        count = np.append(count,len(string[i]))
    number = max(count)
    result = []
    for i in range(len(x)):
        if count[i] == number:
            result = np.append(result,string[i])
    return result