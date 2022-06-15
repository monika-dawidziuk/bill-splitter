import random

guests = int(input('Enter the number of friends joining (including you): \n'))

if guests <= 0:
    print('No one is joining for the party')
else:
    print('Enter the name of every friend (including you), each on a new line:')
    friends = {}

    for i in range(guests):
        name = input()
        friends[name] = 0

    print('Enter the total bill value:')
    bill = int(input())

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky = input()

    if lucky == 'Yes':
        list_to_choose = []
        for name in friends:
            list_to_choose.append(name)
        chosen = random.choice(list_to_choose)
        print(chosen + ' is the lucky one!')

        guests = guests - 1

        for name in friends:
            friends[name] = round(bill / guests, 2)
        friends[chosen] = 0
        print(friends)

    else:
        print('No one is going to be lucky')
        for name in friends:
            friends[name] = round(bill / guests, 2)
        print(friends)