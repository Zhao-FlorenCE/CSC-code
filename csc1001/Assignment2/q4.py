def is_anagram(s1, s2):
    s1.sort()
    s2.sort()
    if s1 == s2:
        print('is an anagram')
    else:
        print('is not an anagram')

string1 = list(input('Please enter the first word: '))
string2 = list(input('Please enter the second word: '))
is_anagram(string1, string2)