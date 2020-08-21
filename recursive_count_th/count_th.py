'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    i = 0
    if len(word) <= 0:
        return 0
    elif(word[0:2] == "th"):
        i += 1
        return i
    else: 
        return count_th(word[0:])