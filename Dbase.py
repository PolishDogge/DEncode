from random import randint
import ast

skip = False

def rng():
    x = randint(0, 1000)
    return x
    
def convert(mes):
    if type(mes) == list:
        return mes
    elif type(mes) == str:
        x = ast.literal_eval(mes)
    return x    

def DEncode(message, move):
    global skip
    loop = []
    output = []
    for character in message:
        loop = []
        if character.isupper():
            loop.append(int(2))
            character = character.lower()
        elif character.islower():
            loop.append(int(1))
            character = character.lower()
        elif character.isspace():
            loop.append(int(0))
            loop.append(randint(-255, 255))
            output.append(loop)
            continue
        elif character.isnumeric():
            loop.append(int(5))
            loop.append(int(character))
            output.append(loop)
            continue
        elif character in ['{', '}', '[', ']', '(', ')', '<', '>', '/', '\\', '|', '?', '!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '+', '=', '~', '`', "'", '"', ':', ';', '.', ',']:
            loop.append(int(10))
            loop.append(ord(character))
            output.append(loop)
            continue

        #convert character to number
        number = ord(character) - move

        #messwith
        if rng() >= 350:
            k = randint(0, 1000)
            number = number + k
            loop.append(k)
            loop.append(number)
            skip = True

        #add number to loop
        if skip == False:
            loop.append(number)


        #add to output
        output.append(loop)
        skip = False
    output.append(move)
    return output


def DDecode(msg):
    final = []
    msg = convert(msg)
    skip = False
    fulllen = len(msg)
    move = msg[fulllen-1]
    msg.pop(fulllen-1)



    for x in msg:
        for y in x:
            
            try:
                if y == x[2]:
                    continue
            except IndexError:
                pass
            
            if y == x[0]:
                if y == 0:
                    final.append(' ')
                    skip = True
                    continue
                

                if y == 1:
                    out = False
                if y == 2:
                    out = True
                if y == 5:
                    final.append(str(x[1]))
                    skip = True
                    continue
                
                if y == 10:
                    final.append(chr(x[1]))
                    skip = True
                    continue
            else:

                try:
                    if x[2]:
                        y = x[2] - y
                except IndexError:
                    pass

                if skip:
                    skip = False
                    continue
                
                if out:
                    final.append(chr(y + move).upper())
                else:
                    final.append(chr(y + move))
        final1 = ''.join(final)
    return final1   