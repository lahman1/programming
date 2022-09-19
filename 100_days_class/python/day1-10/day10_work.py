def my_function():
    result = 3 * 2
    return result


output = my_function()
# print(output)

# Functions with output


#def format_name(f_name, l_name):
#    full_name = (f_name + ' ' + l_name).title()
#    return full_name


#first_name = input('First Name?\n# ')
#last_name = input('Last Name\n# ')
#nice_name = format_name(first_name, last_name)
#print(nice_name)

# Functions with more than one output


def format_name2(f_name, l_name):
    if f_name == '' or l_name == '':
        return "One of the inputs is blank"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return (f"Formatted Name is: {formated_f_name} {formated_l_name}")


print(format_name2(input("What is your first name?\n# "),
                   input("What is your last name?\n# ")))
