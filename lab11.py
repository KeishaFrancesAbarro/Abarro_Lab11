passing = 75
minimum_grade = 40
maximum_grade = 100
counter = 0
passed = 0 
numlist = []

for grade in range(5):
    x = int(input("Enter grade: "))
    if x >= minimum_grade and x <= maximum_grade:
        numlist.append(x)
        counter += 1
        if x >= passing:
            passed += 1
        
    else:
        print("Your grade should be between 40 and 100 only..")
        break
    
if counter == 5:
    Average_Grade = sum(numlist) / counter
    passing_grade = (passed / counter) * 100
    rounded = round(passing_grade, 2)
    
    print (f"Total number of grades input: {counter}")
    print (f"Total number of people who have passed: {passed}")
    print (f"Total percentage of students who passed: {rounded}")
    print (f"Grades of students include: {numlist}")
    
else:
    print("Invalid input")