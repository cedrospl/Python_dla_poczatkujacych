import sys

tasksPerPerson = 0

try:
    tasks = 32
    personsStr = input('How many perople are there in the team?')
    persons = int(personsStr)

    tasksPerPerson = tasks / persons

except ValueError as e:
    print('Sorry - you need to enter an integer number:', e)

except ZeroDivisionError as e:
    print('Sorry - you need to enter value > 0:', e)

except:
   print("Something went wrong...", sys.exc_info()[0])
else:
    print("Every person should have around", tasksPerPerson, "tasks")

finally:
    print("Script finished with/without errors")
