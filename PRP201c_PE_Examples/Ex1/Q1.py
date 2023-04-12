#Q1 - Type until get 'done', count the number,sum,average of all even numbers.Through Exception if wrong format.

evenCount = 0
evenSum = 0
while True:
    try:
        inp = input("Input a number: ")
        if (inp=='done'):
            print("Even count: ", evenCount)
            print("Even sum: ", evenSum)
            try:
                print("Even average: ", evenSum/evenCount)
            except:
                print("Cannot divide 0!")
            break
        x = int(inp)
        if (x%2==0):
            evenSum += x
            evenCount +=1
    except:
        print("Wrong format!")
        continue