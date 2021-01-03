import os
from datetime import datetime

# the list of operators
operators = ["+", "-", "*", "/", "add", "sub", "mul", "div"]


def is_valid_expression(expression):
    """ Takes an expression and checks whether it is valid or not"""
    return all(element in operators or element.replace(".", "").isdigit() for element in expression.split())


def polish_calc(expression):
    """ Takes an expression and calculates it's value, expression is in polish notation"""
    save_result = []
    for elem in expression:
        if elem == "+" or elem == "add":
            save_result[-2:] = [save_result[-1] + save_result[-2]]
        elif elem == "-" or elem == "sub":
            save_result[-2:] = [save_result[-1] - save_result[-2]]
        elif elem == "*" or elem == "mul":
            save_result[-2:] = [save_result[-1] * save_result[-2]]
        elif elem == "/" or elem == "div":
            save_result[-2:] = [save_result[-1] / save_result[-2]]
        else:
            if "." in elem:
                save_result.append(float(elem))
            else:
                save_result.append(int(elem))

    return save_result[0]


def report(expression):
    """ Takes an expression and prints report about is,
        if it is valid prints the result, else prints error message"""
    rev_expression = list(reversed([inp for inp in expression.split()]))
    if is_valid_expression(expression):
        info = f"Expression: {expression}\nResult: {polish_calc(rev_expression)}\nReport: INFO-1, ERROR-0"
    else:
        info = f"Expression: {expression}\nERROR: Invalid expression\nReport: INFO-1, ERROR-1"
    return info


def logging_file(expression):
    """ Writes the report in the file"""
    path = os.getcwd()
    new_dir = os.path.join(path, "logging directory")
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
    with open(os.path.join(new_dir, "report_file.txt"), "a") as rep_file:
        rep_file.write(f"\n{datetime.now()}\n")
        rep_file.write(report(expression) + "\n")


def final_calculator():
    expression = input("Please enter the expression you want to calculate: ")
    return logging_file(expression)

final_calculator()