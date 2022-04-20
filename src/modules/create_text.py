"""
1 | .
2 | ,
3 | ~
4 | *
5 | #
6 | o
7 | O
8 | 0
9 | @  
a | !
b | -
c | =
d | E
e | B
f | S
"""


def convert(text):
    if text == "0":
        return " "
    elif text == "1":
        return "."
    elif text == "2":
        return ","
    elif text == "3":
        return "~"
    elif text == "4":
        return "*"
    elif text == "5":
        return "#"
    elif text == "6":
        return "o"
    elif text == "7":
        return "O"
    elif text == "8":
        return "0"
    elif text == "9":
        return "@"
    elif text == "a":
        return "!"
    elif text == "b":
        return "-"
    elif text == "c":
        return "="
    elif text == "d":
        return "E"
    elif text == "e":
        return "B"
    elif text == "f":
        return "S"
    else:
        return " "
def generate(text):
    c = 0
    output = "|"
    for i in text:
        
        output += convert(i)
        c += 1
        if c == 20:
            if i == text[-1]:
                output += "|"
            else:
                output += "|\n|"
                c = 0
    return output
