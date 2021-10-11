import random

number = random.randint(1,1000)
round = []
score = 0
for x in range(1,21):
 round = ('this is round: {}'.format(x))
 print('your score is ', score)
 print (round)
 for i in range(0,10):
    user = int(input('guess the number: '))
    if abs(user - number) <= 50 and abs(user - number) > 20 :
        print('hot')
    if abs(user - number) <= 20 and abs(user - number) > 10:
        print('very hot')
    if abs(user - number) <= 10 :
        print('Very very hot')
    if user == number:
        print('Hurray')
        print(f"you guessed the right numbber, its {number}")
        print(round)
        score = score +1
        break

 if user != number:
    print(f'your guessed the incorrect number, the correct number is: {number} ')
 again = input('do u want to play again: ')
 if again == 'N' or again=='n' or again=='no' or again=='No':
    break
 number = random.randint(1,1000)
print('Your total score is: ',score)
