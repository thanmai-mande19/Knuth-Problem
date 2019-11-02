import sys
import math

"""
Name: Venkata Thanmai Mande
FileName: factroot.py
Class: CSCI 331 : Intro to Artificial Intelligence.

"""

def find(number):
    start =4
    numbers_path={}

    log_start = math.log10(start)

    numbers_path[log_start]="4"

    numbers =[]

    numbers.append(log_start)


    while(numbers_path.get(math.log10(number))==None):

        if len(numbers)==0:
            break


        log_current_number = numbers[0]
        numbers.remove(log_current_number)

        suitable_log_number=log_current_number

        if log_current_number>300:
            suitable_log_number = math.floor(log_current_number)

        current_number = round(10**suitable_log_number,2)

        floor_current_number = math.floor(current_number)
        if not numbers_path.get(math.log10(floor_current_number)):
            numbers_path[math.log10(floor_current_number)] = numbers_path.get(log_current_number) + "f"

            numbers.append(math.log10(floor_current_number))

        root_current_number = log_current_number/3
        if not numbers_path.get(root_current_number):
            numbers_path[root_current_number] = numbers_path.get(log_current_number) + "r"
            numbers.append(root_current_number)

        if current_number<2001:
            if math.floor(current_number) - current_number ==0:
                factorial_current_number = math.factorial(current_number)
                if not numbers_path.get(math.log10(factorial_current_number)):
                    numbers_path[math.log10(factorial_current_number)]=numbers_path.get(log_current_number)+"!"


                    numbers.append(math.log10(factorial_current_number))

    print(numbers_path.get(math.log10(number)))




def main():

     number= int(sys.argv[1])
     find(number)




if __name__ == '__main__':
    main()

