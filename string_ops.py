def solve (a,b):
    a_len = len (a) -1
    b_len = len (b)
    ast_position = a.find("*")
    ast_len = b_len - a_len
    substring = ""
    if ast_position == -1:
        if a == b :
            return True
        else:
            return False
    for x in range (b_len):
        if b[x] == a[x]:
            continue
        elif b[x] != a[x] and a[x] != "*":
            return False
        else: 
            substring = b[x:x+ast_len]
            break
    a= a.replace("*", substring)
    if a == b:
        return True
    else:
        return False


def find_nth_occurrence (substring, string, occurrence):
    start = 0
    count = 0 
    for i in range(len(string)):
        word = string.find(substring,start)
        start = word +1
        count+=1
        if count == occurrence:
            return word
        elif word == -1 :
            return -1




def is_palindrome(s):
    s=s.lower()
    reverse = s[::-1]
    if s == reverse:
        return True
    else:
        return False
