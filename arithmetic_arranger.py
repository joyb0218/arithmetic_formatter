import sys
def arithmetic_arranger(problems):
    long = (' '.join(problems))
    problems2 = problems[0:-1]
    problems3 = problems[-1]        # LAST PROBLEM

    if len(problems) > 5:
        print("Error: Too many problems.")
        sys.exit(0)

    if '*' in long:
        print("Error: Operator must be '+' or '-'.")
        sys.exit(0)
    if '/' in long:
        print("Error: Operator must be '+' or '-'.")
        sys.exit(0)

    #/// TOP ROW
    for x, y in enumerate(problems2):
        y = y.split(' ')
        res = max(y, key=len)

        if y[0].isdigit() is False or y[2].isdigit() is False:
            print("Error: Numbers must only contain digits.")
            sys.exit(0)

        if len(res) > 4:
            print("Error: Numbers cannot be more than four digits.")
            sys.exit(0)

        if len(y[0]) < len(y[2]):
            total_spaces = len(str(y[2])) + 2  
            rw1_space = total_spaces - len(str(y[0])) 
            w = " " * rw1_space  
            top = w + str(y[0]) + "    " 
            print(top, end="")

        if len(y[0]) >= len(y[2]):
            w = " " * 2  
            top = w + str(y[0]) + "    " 
            print(top, end="")

    # /// TOP ROW - LAST PROBLEM
    y = problems3.split()
    res = max(y, key=len)

    if y[0].isdigit() is False or y[2].isdigit() is False:
        print("Error: Numbers must only contain digits.")
        sys.exit(0)
    if len(res) > 4:
        print("Error: Numbers cannot be more than four digits.")
        sys.exit(0)

    if len(y[0]) <= len(y[2]):
        total_spaces = len(str(y[2])) + 2  
        rw1_space = total_spaces - len(str(y[0]))
        w = " " * rw1_space  
        last_prob_top = w + str(y[0])  
        print(last_prob_top)
    if len(y[0]) >= len(y[2]):
        w = " " * 2  # "..."
        last_prob_top = w + str(y[0])  
        print(last_prob_top)    # /// TOP ROW IS GOOD

    # /// BOTTOM ROW
    for x, y in enumerate(problems2):
        y = y.split(' ')
        if len(y) > 4:
            print("Error: Numbers cannot be more than four digits.")
            sys.exit(0)
        join = (' '.join(y))
        if "+" in join:
            if len(y[0]) <= len(y[2]):
                bottom = "+" + " " + y[2] + "    "
                print(bottom, end="")
            if len(y[0]) > len(y[2]):
                w2 = " " * ((len(y[0]) + 2) - (len(y[2]) + 1))
                bottom = "+" + w2 + y[2] + "    "
                print(bottom, end="")

        if "-" in join:
            if len(y[0]) <= len(y[2]):
                bottom = "-" + " " + y[2] + "    "
                print(bottom, end="")
            if len(y[0]) > len(y[2]):
                w2 = " " * ((len(y[0]) + 2) - (len(y[2]) + 1))
                bottom = "-" + w2 + y[2] + "    "
                print(bottom, end="")

    # /// BOTTOM ROW - LAST PROBLEM
    y = problems3.split()
    if y[1] == "+":                    
        if len(y[0]) <= len(y[2]):
            last_prob_bottom = "+" + " " + y[2]
            print(last_prob_bottom)
        if len(y[0]) > len(y[2]):
            w2 = " " * ((len(y[0]) + 2) - (len(y[2]) + 1))
            last_prob_bottom = "+" + w2 + y[2]
            print(last_prob_bottom)

    if y[1] == "-":                   
        if len(y[0]) <= len(y[2]):
            last_prob_bottom = "-" + " " + y[2]
            print(last_prob_bottom)
        if len(y[0]) > len(y[2]):
            w2 = " " * ((len(y[0]) + 2) - (len(y[2]) + 1))
            last_prob_bottom = "-" + w2 + y[2]
            print(last_prob_bottom)         # /// BOTTOM ROW IS GOOD

    ##  /// DASHES
    for x, y in enumerate(problems2):
        y = y.split(' ')
        dashes1 = max(y, key=len)
        dashes2 = (len(dashes1) + 2) * "-"
        print(dashes2, end="    ")
        sp5 = len(dashes1) + 2

    # /// DASHES - FOR LAST PROBLEM
    y = problems3.split()
    dashes1 = max(y, key=len)
    dashes2 = len(dashes1) + 2  # 6
    dashes3 = "-" * dashes2
    print(dashes3)                      # /// DASHES IS GOOD

    ##  /// RESULTS LINE
    for i in problems2:
        y = i.split(' ')      
        m = max(y, key=len)
        m2 = (len(m)) + 2      
        results = eval(i)     
        spaces_results = len(str(results))   
        if len(str(results)) == 1:
            spaces_results = spaces_results + 1    
        spacing1 = m2 - spaces_results          
        if spacing1 == 1:
            spacing1 = spacing1 + 1

        spacing = spacing1 * " "
        new_results = str(spacing) + str(results) + "    "
        print(new_results, end="")

    ##  /// RESULTS LINE - FOR LAST PROBLEM
    last_prob_result = eval(problems3)
    if last_prob_result < 1:
        spaces = " " + str(last_prob_result)
        print(spaces)
    if last_prob_result > 1:
        y = problems3.split()
        spacing3 = max(y, key=len)
        spacing4 = (len(str(spacing3))) + 2
        spacing5 = spacing4 - len(str(spacing3))
        spaces = " " * spacing5 + str(last_prob_result) # /// DASHES IS GOOD
        print(spaces)

    sys.exit(0)
    return arithmetic_arranger