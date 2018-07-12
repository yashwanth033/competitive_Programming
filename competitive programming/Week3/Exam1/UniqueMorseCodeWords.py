codes = {'A': ".-", 'B': "-...", 'C': "-.-.", 'D': "-..", 'E': ".", 'F': "..-.", 'G': "--.", 'H': "....", 'I': "..", 'J': ".---", 'K': "-.-", 'L': ".-..", 'M': "--", 'N': "-.", 'O': "---", 'P': ".--.", 'Q': "--.-", 'R': ".-.", 'S': "...", 'T': "-", 'U': "..-", 'V': "...-", 'W': ".--", 'X': "-..-", 'Y': "-.--", 'Z': "--.."	}


def unique_codes(words):
    un_codes = []
    string = ""
    for word in words:
        for c in word:
            string += codes.get(c.upper())
        if string not in un_codes:
            un_codes.append(string)
        string = ""
    return len(un_codes)

if __name__ == '__main__':
    print(unique_codes(["gin", "zen", "gig", "msg"]))
    print(unique_codes(["a", "z", "g", "m"]))
    print(unique_codes(["hig", "sip", "pot"] ))
    print(unique_codes(["a", "b", "c", "d"] ))
    print(unique_codes(["bhi", "vsv", "sgh", "vbi"]  ))