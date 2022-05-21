import math
import time

def calculator(USER_INPUT):
    if USER_INPUT == 1:
        while True:
            NUM1 = input('ENTER THE FIRST NUMBER:')
            NUM2 = input('ENTER THE SECOND NUMBER:')
            if NUM1 == 'exit' or 'EXIT' or 'Exit':
                break
            else:
                try:
                    print(f"THE ANSWER IS {NUM1 + NUM2}")
                except Exception as e:
                    e = e
                    print ("INVALID NUMBERS ENTERED.")

    elif USER_INPUT == 2:
        while True:
            NUM1 = input('ENTER THE FIRST NUMBER:')
            NUM2 = input('ENTER THE SECOND NUMBER:')
            if NUM1 == 'exit' or 'EXIT' or 'Exit':
                break
            else:
                try:
                    print(f"THE ANSWER IS {NUM1 - NUM2}")
                except Exception as e:
                    e = e                    
                    print ("INVALID NUMBERS ENTERED.")


    elif USER_INPUT == 2:
        while True:
            NUM1 = input('ENTER THE FIRST NUMBER:')
            NUM2 = input('ENTER THE SECOND NUMBER:')
            if NUM1 == 'exit' or 'EXIT' or 'Exit':
                break
            else:
                try:
                    print(f"THE ANSWER IS {NUM1 * NUM2}")
                except Exception as e:
                    e = e 
                    print ("INVALID NUMBERS ENTERED.")

    elif USER_INPUT == 2:
        while True:
            NUM1 = input('ENTER THE FIRST NUMBER:')
            NUM2 = input('ENTER THE SECOND NUMBER:')
            if NUM1 == 'exit' or 'EXIT' or 'Exit':
                break
            else:
                try:
                    print(f"THE QUOTIENT IS {NUM1 / NUM2} AND THE REMAINDER IS {NUM1 % NUM2}")
                except Exception as e:
                    e = e
                    print ("INVALID NUMBERS ENTERED.")

    elif USER_INPUT == 5:
        print('PRESS')
        print('1 FOR SIN, COS, TAN, LOG')
        print('2 FOR FINDING AVERAGE')
        print('3 FOR FINDING SQUARE ROOT')
        print('4 FOR COVERTION OF RADIAN TO DEGREE')
        print('5 FOR FACTORIAL')
        print('6 FOR π CALCULATIONS')
        print('7 FOR e CALCULATIONS')
        EXTRA_INPUT = int(input())

        if EXTRA_INPUT == 1:
            INPUT = int(input('ENTER THE NUMBER'))
            print(f"THE COS OF {INPUT} IS {math.cos(INPUT)}")
            print(f"THE SIN OF {INPUT} IS {math.sin(INPUT)}")
            print(f"THE TAN OF {INPUT} IS {math.tan(INPUT)}")
            print(f"THE LOG OF {INPUT} IS {math.log(INPUT)}")

        elif EXTRA_INPUT == 2:
            while True:
                NUM_LIST = []

                for i in range(int(input('ENTER THE SIZE OF THE NUMBERS:'))):
                    INPUT = input('ENTER THE NUMBER:')
                    if INPUT == 'exit' or 'EXIT' or 'Exit':
                        break
                    else:
                        try:
                            NUM_LIST.append(INPUT)
                            AVERAGE = (sum(NUM_LIST)) / len(NUM_LIST)
                            print (f'THE AVERAGE IS {AVERAGE}')
                        except Exception as e:
                            print ("INVALID INPUT!")

        elif EXTRA_INPUT == 3:
            while True:
                INPUT = input ('ENTER THE NUMBER')
                if INPUT == 'exit' or 'EXIT' or 'Exit': 
                    break
                else: 
                    try:
                        SQRT = math.sqrt(INPUT)
                        print (f'THE SQUARE ROOT OF {INPUT} IS {SQRT}')
                    except Exception as e:
                        print ('INVALID INPUT!')

        elif EXTRA_INPUT == 4:
            while True:
                INPUT = input ('ENTER THE NUMBER:')
                if INPUT == 'exit' or 'EXIT' or 'Exit':
                    break
                else:
                    try:
                        RADIAN= math.radians(INPUT)
                        print (f'WHEN CONVERTED {INPUT} TO RADIAN, WE GET {RADIAN}')
                    except Exception as e:
                        print ('INVAILID INPUT!')

        elif EXTRA_INPUT == 5:
            while True:
                INPUT = input ('ENTER THE NUMBER:')
                if INPUT == 'exit' or 'EXIT' or 'Exit':
                    break
                else:
                    try:
                        FACTORIAL = math.factorial(INPUT)
                        print (f'THE FACTORIAL OF {INPUT} is {FACTORIAL}')
                    except Exception as e:
                        e = e
                        print ('INVAILID INPUT!')
        
        elif EXTRA_INPUT == 6:  
            while True:
                INPUT = input('ENTER THE NUMBER:')
                if INPUT == 'exit' or 'EXIT' or 'Exit':
                    break
                else:
                    try:
                        print (f'π + {INPUT} = {math.pi() + INPUT}')
                        print (f'π - {INPUT} = {math.pi() - INPUT}')
                        print (f'π x {INPUT} = {math.pi() * INPUT}')
                        print (f'π / {INPUT} = {math.pi() / INPUT}')
                    except Exception as e:
                        print ('INVALID INPUT!')
        
        elif EXTRA_INPUT == 7:  
            while True:
                INPUT = input('ENTER THE NUMBER:')
                if INPUT == 'exit' or 'EXIT' or 'Exit':
                    break
                else:
                    try:
                        print (f'e + {INPUT} = {math.e() + INPUT}')
                        print (f'e - {INPUT} = {math.e() - INPUT}')
                        print (f'e x {INPUT} = {math.e() * INPUT}')
                        print (f'e / {INPUT} = {math.e() / INPUT}')
                    except Exception as e:
                        print ('INVALID INPUT!')

if __name__ == '__main__':
    INITIAL_TIME = time.time()
    print ('Loading...')
    time.sleep(1.5)
    print('WELCOME TO PYCAL\n')
    print (f"ABOUT 5 RESULTS ({format (time.time() - INITIAL_TIME, '.2f')} seconds)\n")
    print('PRESS:')
    print('1 FOR ADDITION')
    print('2 FOR SUBSTRACTION')
    print('3 FOR MULTIPLICATION')
    print('4 FOR DIVISION')
    print('5 FOR ADVANCE CALCULATIONS')
    USER_INPUT = int(input())
    calculator(USER_INPUT)  