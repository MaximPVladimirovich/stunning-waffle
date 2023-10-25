import random


num_digits = 3
max_guesses = 10


def main():
    print('''Bagels, a deductive logic game. 
        
        I am thinking of a {}-digit number with no repeated digits. 
        Try to guess what it is. 
        Here are some clues:
          
        When I say:  That means:
        Pico         One digit is correct but in the wrong position.
        Fermi        One digit is correct and in the right position. 
        Bagels       No digit is correct. 
          
        For example, if the secret number was 248 and your guess was 843, the
        clues would be Fermi Pico.'''.format(num_digits))
    
    while True:
        secretNumber = getSecretNumber();
        print("I have thought of a number.");
        print('You have {} guesses to get the correct answer'.format(max_guesses))

        num_guesses = 1;
        while num_guesses <= max_guesses:
            guess='';
            while len(guess) != num_digits or not guess.isdecimal():
                print('Guess #{}:'.format(num_guesses));
                guess=input('> ')
            
            clues=getClues(guess, secretNumber);
            print(clues);
            num_guesses+=1;

            
            if guess == secretNumber:
                break;
            if num_guesses > max_guesses:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNumber))


def getSecretNumber():
    numbers = list('123456789');
    random.shuffle(numbers);

    secret_number = '';
    for i in range(num_digits):
        secret_number += str(numbers[i]);
    return secret_number;



def getClues(guess, secret_number):
    if guess == secret_number:
        return "You got it!"
    

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            clues.append("Fermi")
        elif guess[i] in secret_number:
            clues.append("Pico");
    if len(clues) == 0:
        return "Bagels";
    else:
        clues.sort();
    return ' '.join(clues);


if __name__=='__main__':
    main();