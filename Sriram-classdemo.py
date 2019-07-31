def grade_converter(grade):
    if (grade >= 90):
        return "A"
    elif grade in range(80,89) :
        return "B"
    elif grade in range(70,79):
        return "C"
    elif grade in range(65,69):
        return "D"
    else:
        return "F"
      
# This should print an "A"      
print grade_converter(92)

# This should print a "C"
print grade_converter(84)

# This should print an "F"
print grade_converter(61
