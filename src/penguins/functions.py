# converting p-value to works
def p_value_to_words(p_value):

    p_value_rounded = str(round(p_value,3))

    if p_value >= 0.05:
        print("we cannot reject the null hypothesis. The p-values is too large: " + p_value_rounded)
    elif p_value < 0.001:
        print("*** The p-value is smaller than the criticial threshold, p-value is: " + p_value_rounded)
    elif p_value < 0.05:
        print("* The p-value is smaller than the critical threshold, p-value is: " + p_value_rounded)
    else:
        print("Your p-value defies maths. I don't know what to do with it.")
    
