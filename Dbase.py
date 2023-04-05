from random import randint
def DEncode(message, move=randint(-5,255)) -> list:
    output = []
    if message != str:
        message = str(message)
    for character in message:
        if character.isupper(): 
            output.append([2, ord(character.lower()) - move])
        elif character.islower():
            output.append([1, ord(character) - move])
        elif character.isspace():
            output.append([0, randint(-255, 255)])
        elif character.isnumeric():
            output.append([5, int(character)])
        elif character in [ 
            "{",
            "}",
            "[",
            "]",
            "(",
            ")",
            "<",
            ">",
            "/",
            "\\",
            "|",
            "?",
            "!",
            "@",
            "#",
            "$",
            "%",
            "^",
            "&",
            "*",
            "-",
            "_",
            "+",
            "=",
            "~",
            "`",
            "'",
            '"',
            ":",
            ";",
            ".",
            ",",
        ]:
            output.append([10, ord(character)])
        else:
            number = ord(character) - move
            if randint(0, 1000) >= 350:
                k = randint(0, 1000)
                number += k
                output.append([k, number])
            else:
                output.append([number])
    output.append(move)
    return output


def DDecode(msg) -> str:
    final = []
    if msg != list:
        msg = list(msg)
    move = msg.pop()
    for x in msg:
        if x[0] == 0:
            final.append(" ")
        elif x[0] == 1:
            final.append(chr(x[1] + move))
        elif x[0] == 2:
            final.append(chr(x[1] + move).upper())
        elif x[0] == 5:
            final.append(str(x[1]))
        elif x[0] == 10:
            final.append(chr(x[1]))
        elif len(x) == 3:
            final.append(chr(x[2] - x[1]))
    return "".join(final)
