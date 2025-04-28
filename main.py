
def show_Balance():
    pass

def depost():
    pass

def withdraw():
    pass

running = True

while running:
    print('-----Welcome to Banking system-----')
    print()
    opetions = {'1': 'Check Blance', '2': 'Depost money', '3': 'Withdraw money' }
    for key in opetions:
        print(key, opetions[key])
    result = input('enter your option')

    if result=='1':
        show_Balance()

    elif result == '2':
        depost()

    elif result == '3':
        withdraw()

    elif result =='4':
        running =False
    else:
        print('error 505: Unknown input ')
