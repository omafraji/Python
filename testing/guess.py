from random import randint
import sys
# generate a number 1~10
#answer = randint(1, 10)

# input from user?
# check that input is a number 1~10
def inserted_num (guess, answer):
    if  0 < guess < 11:
        if guess == answer:
            return True
    else:
        return False
    
if __name__ == '__main__':
    answer = randint(1, 10)
    print(answer)
    while True:
        try:
            guess = int(input('guess a number 1~10:  '))
            if (inserted_num(guess, answer)):
                break
        except ValueError:
            continue



#while True:
    #try:
        #guess = int(input('guess a number 1~10:  '))
        #if  0 < guess < 11:
            #if guess == answer:
                #print('you are a genius!')
                #break
        #else:
            #print('hey bozo, I said 1~10')
    #except ValueError:
        #print('please enter a number')
        #continue