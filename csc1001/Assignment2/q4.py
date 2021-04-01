# Check whether the string pair is an anagram
def is_anagram(s1, s2):
    s1.sort()
    s2.sort()
    if s1 == s2:
        print('Is an anagram.')
    else:
        print('Is not an anagram.')

string1 = list(input('Please enter the first word: '))
string2 = list(input('Please enter the second word: '))
is_anagram(string1, string2)