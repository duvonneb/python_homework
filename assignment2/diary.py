import traceback
i = 0
user_input = ""

# Prompt until user enters "done for now"
while user_input != "done for now":
    try:
        with open('diary.txt', 'a') as file:
            # First prompt for user
            if i == 0:
                user_input = input("What happened today? ")
                i+=1
            # Prompts for additional input
            else:
                user_input = input("What else? ")
            file.write(user_input + "\n")

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

# Close file once user is done
if user_input == "done for now":
    file.close()