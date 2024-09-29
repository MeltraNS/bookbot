#Create a function that takes a single digit integer i 
#1-9 and transforms it in the following pattern:
#1 = 9
#2 = 8
#3 = 7
#4 = 6
#6 = 4
#7 = 3
#8 = 2
#9 = 1
#if i = 5, return 5
#if i != 1-9, is a float, string, or boolean, raise an
#exception to notify the user to enter a single digit
#integer 1-9

def main():
    try:
        print(remap(10))
    except Exception as e:
        print(e)



def remap(num):
    reverse_chronological = [9,8,7,6,5,4,3,2,1]
    if num == 5:
        return 5
    elif (num >= 1 and num < 5) or (num >=6 and num < 10):
        return reverse_chronological[num - 1]
    raise Exception("Please enter an integer from 1 to 9 inclusive.")

main()
