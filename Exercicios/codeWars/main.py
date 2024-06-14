def open_or_senior(data):
    return ['Senior' if person[0] >= 55 and person[1] > 7 else 'Open' for person in data]
            

print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))

# members = []

# for person in data:
#     if person[0] >= 55 and person [1] > 7:
#         members.append('Senior')
#     else:
#         members.append('Open')
        
# return members