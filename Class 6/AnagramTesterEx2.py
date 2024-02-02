"""
Program that takes user input and checks if it's an anagram or not
"""


#user input, no need to check if user gives good data types as input() function is always type str
print("wprowadz slowo")
slowo = input()
print("wprowadz anagram slowa")
anagram = input()


def sprawdz(slowo, anagram):
    #check if the lenght of the word is the same as the lenght of the anagram, if not return False
    if len(slowo) != len(anagram):
        return False
    
    #var that has the amount of letters that the function found to be the same 
    liczba_prawd = 0
    #iterate through the slowo str, for every letter in the word iterate again, this time through anagram, to check if any letter matches
    #if a letter matches add the count of matching letters. replace the anagram with a word without one of the letters,
    #so that there are no errors when counting unusual words that could have over 3 same letters.
    for x in slowo:
        for h in anagram:
            if x == h:
                liczba_prawd += 1
                temp = anagram.replace(x, "", 1)
                anagram = temp
                break

    if liczba_prawd == len(slowo):
        return True
    else:
        return False
    
print(sprawdz(slowo, anagram))