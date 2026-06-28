try: 
    #1. Main logic
    file = open("data.txt","r")
    value = int(file.readline())
    result = 100/value
except FileNotFoundError:
    #2. Runs only if data.txt doesnot exist
    print("Error:The target file was not found.")
except ZeroDivisionError:
    #3. Runs only if value 0
    print("Error:division by zero.")
except ValueError as error:
    #4. Runs if the line isn't a valid number
    print(f"Data type_issue:{error}")
else:
    #5. Runs only if try block executes with zero errors 
    print(f"Sucess! The result is {result}")
finally:
    #6. Always runs, regardless of errors, to clean up states
    if 'file' in locals() and not file.closed:
        file.close()
    print("Cleanup:File resource verified.")