def extention():
    r = 0
    tue_morse_new = tue_morse.copy()
    while r < len(tue_morse_new):
        if tue_morse_new[r] == 0:
            del tue_morse_new[r]
            tue_morse_new.insert(r, 1)
        elif tue_morse_new[r] == 1:
            del tue_morse_new[r]
            tue_morse_new.insert(r, 0)
        r += 1
    return tue_morse_new

tue_morse = [0]
while len(tue_morse) <= 2055:
    tue_morse_new = extention()
    tue_morse.extend(tue_morse_new)
print(tue_morse[16:22])
print(tue_morse[59:65])
print(tue_morse[99:105])
print(tue_morse[199:205])
print(tue_morse[2049:2055])


    
    
    

