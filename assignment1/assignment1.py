# Task 1
def hello():
    return("Hello!")

# Task 2
def greet(name):
    return ("Hello, " + name + "!")

# Task 3
def calc(num1, num2, operation=None):
    # defaults to multiply is no operation is given
    if operation is None:
        return num1 * num2
    # checks to ensure values given are integers or floaters
    elif isinstance (num1, (int, float)) and isinstance(num2, (int, float)):
        match operation:
            case "add":
                return num1 + num2
            case "subtract":
                return num1 - num2
            case "multiply":
                return num1 * num2
            case "divide":
                if num1 == 0 or num2 == 0:
                    return "You can't divide by 0!"
                else:
                    return num1 / num2
            case "modulo":
                return num1 % num2
            case "int_divide":
                return num1 // num2
            case "power":
                return num1 ** num2
    else:
        return "You can't multiply those values!"
    
# Task 4
def data_type_conversion(value, data_type):
    match data_type:
        case "float":
            try:
                if isinstance(float(value), (int, float)):
                    return float(value)
            # if operation errors out, value given is not a number
            except ValueError:
                return ("You can't convert " + {value} + " into a " + {data_type} + ".")
        case "str":
            return str(value)
        case "int":
            try:
                if isinstance(int(value), (int, float)):
                    return int(value)
            # if operation errors out, value given is not a number
            except ValueError:
                return ("You can't convert " + value + " into a " + data_type + ".")
            
# Task 5
def grade(*args):
    # check is valus given are numbers
    for i in args:
        ifnums = isinstance(i, (int, float))
    if ifnums:    
        avg = sum(args) / len(args)
        if avg >= 90:
            return "A"
        elif avg >= 80 and avg <= 89:
            return "B"
        elif avg >= 70 and avg <= 79:
            return "C"
        elif avg >= 60 and avg <= 69:
            return "D"
        elif avg <= 60:
            return "F"
    else:
        return ("Invalid data was provided.")
    
# Task 6
def repeat(string, count):
    # multiply strings by count value given
    for x in range(count):
        newstring = (string * x) + string
    return newstring

# Task 7
def student_scores(position, **kwargs):
    total_value = 0
    match position:
        case "mean":
            for key, value in kwargs.items():
                total_value = total_value + value
            return total_value / len(kwargs)
        case "best":
            x = 0
            # check each value keep the highest one
            for key, value in kwargs.items():
                if value >= x:
                    student = key
                    x = value
            return student

# Task 8
def titleize(string):
    words = string.split()
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    new_string = ""
    for i, word in enumerate(words):
        if word in little_words:
            # If word is first always capitalize
            if i == 0:
                new_string = new_string + word.capitalize()
            # If word is last always capitalize
            elif i == len(words) - 1:
                new_string = new_string + " " + word.capitalize()
            # If little word is not first or last add as is
            else:
                new_string = new_string + " " + word
        else:
            # If word is first always capitalize
            if i == 0:
                new_string = new_string + word.capitalize()
            # If word is last always capitalize
            elif i == len(words) - 1:
                new_string = new_string + " " + word.capitalize()
            # If word is not little capitalize
            else:
                new_string = new_string + " " + word.capitalize()
    return new_string

# Task 9
def hangman(secret, guess):
    # Create list out of secret and guess values
    secret_letters = list(secret)
    guess_letters = list(guess)
    current_guess = ""
    for secret_letter in secret_letters:
        # If secret letter is in guess letter show letter
        if secret_letter in guess_letters:
            current_guess = current_guess + secret_letter
        # If secret letter is not in guess letter show underscore
        else:
            current_guess = current_guess + "_"
    return current_guess

# Task 10
def pig_latin(x):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = x.split()
    pig_latin_words = []
    for word in words:
        x_letters = list(word)
        x_length = len(x_letters)
        i = 0
        
        # Check if word starts with a vowel
        if x_letters[0] in vowels:
            x_letters.append("ay")
        else:
            # Handle 'qu' special case
            while i <= x_length:
                if len(x_letters) > 1 and x_letters[0] == "q" and x_letters[1] == "u":
                    x_letters.append(x_letters.pop(0))
                    x_letters.append(x_letters.pop(0))
                    break
                elif x_letters[0] not in vowels:
                    x_letters.append(x_letters.pop(0))
                else:
                    break
            x_letters.append("ay")
        pig_latin_words.append(''.join(x_letters))
    return ' '.join(pig_latin_words)