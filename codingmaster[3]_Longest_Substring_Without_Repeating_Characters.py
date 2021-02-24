def lengthOfLongestSubstring(s):
    if len(s) == 0:
        return 0

    maxlens = []
    sublen = 0
    temp = {}
    for i in s:
        if i not in temp.keys():
            temp[i] = 1
            sublen += 1
        else:
            maxlens.append(sublen)
            del temp
            temp = {}
            temp[i] = 1
            sublen = 1
    return max(maxlens)

lengthOfLongestSubstring("abcabcbb")
