# itere sobre um string com while

fullname = 'Eduardo Marques Negalho'

count = 0
new_string = ''

while count < len(fullname):
    new_string += fullname[count] + '*'

    count += 1

print(new_string)