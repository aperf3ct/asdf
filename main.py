import random
student_list = ['Katherine', 'Nicole', 'Shreya', 'April',
                'Anya', 'Abby', 'Melissa', 'Kaitlyn', 'Michelle', 'Olivia', 'Mr Harrison']
valid = False
choice_1 = 0
choice_2 = 0

while valid == False:
    choice_1 = random.choice(student_list)
    choice_2 = random.choice(student_list)
    if choice_1 == choice_2:
        choice_2 = random.choice(student_list)
    else:
        valid = True

print("{} vs {}".format(choice_1, choice_2))
