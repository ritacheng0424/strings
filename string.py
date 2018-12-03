def cs110_upper(upperstring):
    String = ""
    for s in upperstring:
        if s == " ":
            String += s
        upperCase = ord(s) - 32
        String += chr(upperCase)
    return String


def cs110_lower(lowerstring):
    String = ""
    for s in lowerstring:
        if s == " ":
            String += s
        lowerCase = ord(s) + 32
        String += chr(lowerCase)
    return String


def cs110_rfind(findstring):
    findChar = input("Which character do you want to find: ")
    for s in range(len(findstring)-1, -1, -1):
        if findChar == findstring[s]:
            return("It is at index:",s)
            break
        else:
            continue


def cs110_compare(str1, str2):
    if str1 < str2:
        print("-1")
    elif str1 == str2:
        print("0")
    elif str1 > str2:
        print("+1")


def cs110_strip(stripstring):
    nospace = ""
    for s in stripstring:
        if s != " ":
            nospace = nospace + s
        elif s == " ":
            space = ""
            nospace = nospace + space
    return nospace


def cs110_lstrip(x):
    noleadspace = ""
    stringCount = 0
    for i in x:
        if i != " ":
            noleadspace = x[stringCount:]
            break
        else:
            stringCount = stringCount + 1
    return noleadspace
    
def cs110_replace(userString, char1, char2):
    replace = ""
    for s in userString:
        if s == char1:
            s = char2
        replace = replace + s
    return replace


def cs110_in(userString, search):
    count = 0
    for i in userString:
        if search == i:
            count += 1
    if count > 0:
            return True
    else:
            return  False


def cs110_notin(userString, search):
    count = 0
    for i in userString:
        if search == i:
            count += 1
    if count > 0:
        return False
    else:
        return True


def cs110_title(x):
    titileString = ""
    position = 0
    for s in range(len(x)):
        if position == 0:
            letter = x[position]
            cap = ord(letter) - 32
            titileString += chr(cap)
            position += 1
        elif s != " " and x[s - 1] == " ":
            letter = x[s]
            cap = ord(letter) - 32
            titileString += chr(cap)
        else:
            titileString += x[s]
    return titileString




def cs110_remove_repeats(removestring):
    String = ""
    position = 0
    for s in removestring:
        position += 1
        if position > len(removestring) - 1:
            String += s
            continue
        elif s == removestring[position]:
            if position == len(removestring) - 1:
                String += s
                continue
            s = ""
            String += s
        else:
            String += s
    return String




def main():
    lowerString = input("Please enter any string with lower case: ")
    print (cs110_upper(lowerString))
    upperString = input("Please enter any string with upper case: ")
    print (cs110_lower(upperString))
    findInput = input("Enter a string, this is a test for finding a character: ")
    print (cs110_rfind(findInput))
    print("Enter two strings to compare.")
    compare1 = input("First string: ")
    compare2 = input("Second string: ")
    print (cs110_compare(compare1,compare2))
    stripInput = input("Please enter a string with white space on either sides: ")
    print (cs110_strip(stripInput))
    replaceString = input("Enter any string, this is a test for replacing a character: ")
    replace1 = input("What character do you want to replace: ")
    replace2 = input("What do you want it to be replaced as: ")
    print (cs110_replace(replaceString,replace1,replace2))
    lstripInput = input("Please enter a string with leading white space: ")
    print (cs110_lstrip(lstripInput))
    inInput = input("Enter a string, this is a test for determining if a string is within the input string: ")
    inSearch = input("What string do you want to find in the above: ")
    print (cs110_in(inInput, inSearch))
    notinInput = input("Enter a string, this is another test for determining if a string is within the input string: ")
    notinSearch = input("Enter a string that will not be found in the above: ")
    print (cs110_notin(notinInput, notinSearch))
    capInput = input("Enter a string with more than one word, each word's first letter will be capitalized: ")
    print (cs110_title(capInput))
    repeatInput = input("Enter a string with duplicating characters, this will remove duplicates: ")
    print (cs110_remove_repeats(repeatInput))


main()
