def OddAndEven(listNumber):
    oddNumbers=[];
    evenNumbers=[];

    numberList=listNumber.split();

    for item in numberList:
        try:
              num=int(item);
              if(num%2==0):
                evenNumbers.append(item);
              else:
                oddNumbers.append(item);
        except:
            pass
        '''try:
            num = int(item)
            if num % 2 == 0:
                evenNumbers.append(num)
            else:
                oddNumbers.append(num)
        except ValueError:
            # Ignore non-numeric values
            pass'''
     
    return oddNumbers,evenNumbers;


numbers="1 2 3 4 5 6 7 9 7";
oddList,evenList=OddAndEven(numbers);

print("Even numbers : ",evenList);
print("Odd numbers : ",oddList);




                



    
