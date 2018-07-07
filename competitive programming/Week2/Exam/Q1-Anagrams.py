def anagrams(s,t):
    dict_s = {}
    dict_t = {}
    for i in s:
        i = i.lower()
        if i!=" ":
            if i not in dict_s:
                dict_s[i] = 1
            else:
                dict_s[i] += 1
    for i in t:
        i = i.lower()
        if i!=" ":
            if i not in dict_t:
                dict_t[i] = 1
            else:
                dict_t[i] += 1
    for i in dict_s.keys():
        if dict_s[i]!=dict_t.get(i,0):
            return False
    return True

if __name__ == '__main__':
    print(anagrams("anagram","nagaram"))
    print(anagrams("peek", "Keep"))
    print(anagrams("Mother in Law", "Hitler Woman"))
    print(anagrams("TooS", "Shot"))