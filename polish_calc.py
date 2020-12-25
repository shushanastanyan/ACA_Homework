# this is the polish calculator function
import os
from datetime import datetime

def polish_calc():


    save_result = []
    expression = reversed([inp for inp in input("Please enter the expression you want to calculate: ").split()])
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

#print(polish_calc())


# new_dir = os.path.join(path, "logging directory")
# if not os.path.exists(new_dir):
#     os.mkdir(new_dir)

path = os.getcwd()
with open(os.path.join(path, "logging directory", "report_file.txt"), "w") as report:
    report.write()
