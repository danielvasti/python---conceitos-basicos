true_number = 22
tries = 3
discover = False

while tries > 0 and not discover:
    chosen_number = int(input("Digite um número: "))
    if chosen_number < true_number:
        print('Chute muito baixo')
        tries -= 1
    elif chosen_number > true_number:
        print('Chute muito alto')
        tries -= 1
    else: 
        print('Você acertou o número')
        discover = True
            
if not discover:
    print("Out of tries")