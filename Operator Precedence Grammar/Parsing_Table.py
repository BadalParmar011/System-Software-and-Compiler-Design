# -*- coding: utf-8 -*-
"""
18BCP011
Badal Parmar
SSCD

Experiment 8:
    Write a program to construct operator precedence parsing table for the 
    given givengrammar and check the validity of the string (id+id*id).
"""


givengrammar = open(r'grammar2.txt', 
               'r',
               encoding='utf-8')
N_T_R = givengrammar.readlines()

for i in range(len(N_T_R)):
    N_T_R[i] = N_T_R[i][:-1]
    

#Printing the givengrammar
print('\ngivengrammar')
for each in N_T_R:
    print(each)
    
r_o_g = {}

for each in N_T_R:
    raw_production = each
    temp_production = ''
    for i in range(len(raw_production)):
        if(raw_production[i]!=' '):
            temp_production+=raw_production[i]
            
    lhs, rhs = temp_production.split('->')[0], temp_production.split('->')[1] 
    if '|' in rhs:
        r_o_g[lhs] = rhs.split('|')
    else:
        r_o_g[lhs] = [rhs]


#Checking whether the givengrammar is operator precedence or not
operator_precedence = True

for non_terminal in r_o_g:
    for production in r_o_g[non_terminal]:
        
        if '\u03B5' in production:
            operator_precedence = False
            break
        
        variable = None
        if production[0].isalpha() and production[0].isupper():
            varaible = True 
        else:
            variable = False
            
    
        for i in range(1, len(production)):
            if production[i].isalpha() and variable==True:
                operator_precedence = False
                break
            elif production[i].isalpha() and variable==False:
                variable = True
            elif (not production[i].isalpha()) and variable==False:
                operator_precedence = False
                break
            else:
                variable = False
        
        if not operator_precedence:
            break
        
    if not operator_precedence:
        break


# Extracting all the terminal symbols
terminal_symbols = {}
index = 0
starting_symbol = None

for non_terminal in r_o_g:
    if index==0:
        starting_symbol = non_terminal
        
    for production in r_o_g[non_terminal]:
        
        for i in range(len(production)):
            if not (production[i].isalpha() and production[i].isupper()):
                if production[i] not in terminal_symbols:
                    terminal_symbols[production[i]] = index
                    index+=1
                    
terminal_symbols['$'] = index
index+=1

print(terminal_symbols)


# Function to find the leading of a non-terminal symbol
def get_leading(symbol, r_o_g):
    if(symbol in leadings):
        return
    else:
        leadings[symbol] = []
    nodes = r_o_g[symbol]
    
    for each in nodes:
        i=0
        if each[i].isalpha() and each[i].isupper():
            if i!=len(each)-1:
                if each[i+1] not in leadings[symbol]:
                    leadings[symbol].append(each[i+1])
            
            if each[i] in leadings:
                for leading in leadings[each[i]]:
                    if leading not in leadings[symbol]:
                        leadings[symbol].append(leading)
            else:
                get_leading(each[i], r_o_g)
                
                for leading in leadings[each[i]]:
                    if leading not in leadings[symbol]:
                        leadings[symbol].append(leading)
        
        else:
            if each[i] not in leadings[symbol]:
                leadings[symbol].append(each[i])
        
                
                
# Function to find the leading of a non-terminal symbol
def get_trailing(symbol, r_o_g):
    if(symbol in trailings):
        return
    else:
        trailings[symbol] = []
    nodes = r_o_g[symbol]
    
    for each in nodes:
        i=len(each)-1
        if each[i].isalpha() and each[i].isupper():
            if i!=0:
                if each[i-1] not in trailings[symbol]:
                    trailings[symbol].append(each[i-1])
            
            if each[i] in trailings:
                for trailing in trailings[each[i]]:
                    if trailing not in trailings[symbol]:
                        trailings[symbol].append(trailing)
            else:
                get_trailing(each[i], r_o_g)
                
                for trailing in trailings[each[i]]:
                    if trailing not in trailings[symbol]:
                        trailings[symbol].append(trailing)
        
        else:
            if each[i] not in trailings[symbol]:
                trailings[symbol].append(each[i])            

                
if operator_precedence:
    print("\nThe givengrammar is an operator precedence given grammar")
    
    non_terminal_symbols = list(r_o_g.keys())

    #Finding the leading of each symbol
    leadings = {}    
    for each in r_o_g:
        get_leading(each, r_o_g)
    
    #Finding the trailing of each symbol
    trailings = {}
    for each in r_o_g:
        get_trailing(each, r_o_g)
               
    print('\nLeading of each non-terminal symbol')
    for each in leadings:
        print(each+':', leadings[each])
        
    print('\nTrailing of each non-terminal symbol')
    for each in trailings:
        print(each+':', trailings[each])
        
    
    # Building the parsing table
    
    # Initializing the parsing table
    parsing_table = [[] for _ in range(len(terminal_symbols))]
    for each in parsing_table:
        for _ in range(len(terminal_symbols)):
            each.append(' ')

    
    # Filling the parsing table
    for non_terminal in r_o_g:
        for production in r_o_g[non_terminal]:
            
            if len(production)==1:
                continue
            
            for i in range(1,len(production)):
                
                if production[i].isalpha() and production[i].isupper():
                    
                    for terminal in leadings[production[i]]:
                        parsing_table[terminal_symbols[production[i-1]]][terminal_symbols[terminal]] = '<'
                
                else:
                    
                    for terminal in trailings[production[i-1]]:
                        parsing_table[terminal_symbols[terminal]][terminal_symbols[production[i]]] = '>'
    
    
    for terminal in list(terminal_symbols.keys()):
        # Adding an accept character in the parsing table for validating the string
        if terminal == '$':
            parsing_table[terminal_symbols['$']][terminal_symbols['$']] = 'A'
        else:
            parsing_table[terminal_symbols[terminal]][terminal_symbols['$']] = '>'
            parsing_table[terminal_symbols['$']][terminal_symbols[terminal]] = '<'
        
  
    # Since '(' and ')' have same precedence
    if ('(' in list(terminal_symbols.keys())) and '(' in list(terminal_symbols.keys()):
        parsing_table[terminal_symbols['(']][terminal_symbols[')']] = '='
        parsing_table[terminal_symbols[')']][terminal_symbols['(']] = '='
        
    
    
    # Printing the parsing table
    print('\n\nParsing table\n')
    print('  | ',end='')
    print(' '.join(list(terminal_symbols.keys())), end='\n')
    print('--+-',end='')
    print('-'*((len(terminal_symbols)*2)))
    
    
    for i in range(len(parsing_table)):
        print(list(terminal_symbols.keys())[i]+' | ',end='')
        print(' '.join(parsing_table[i]),end='\n')

    # Validating the input string 
    string = input("\nEnter the string to be validated: ");    
    string+='$'
    
    stack = ['$'] #Initializing stack
    top = 0
    pointer = 0

    operator_precedence_givengrammar = False
    while True:
        
        if pointer < len(string):
            entry = parsing_table[terminal_symbols[stack[top]]][terminal_symbols[string[pointer]]]
            if entry == '<' or entry == '=':
                stack.append(string[pointer])
                top+=1
                pointer+=1
            elif entry == '>':
                stack.pop()
                top-=1
            elif entry == 'A':
                operator_precedence_givengrammar = True
                break
            else:
                break
            
        else:
            break

    if operator_precedence_givengrammar:
        print('\nValid string! It belongs to the givengrammar')
    else:
        print('\nInvalid string! It does not belong to the givengrammar')
            
else:
    print("\nThe givengrammar is not an operator precedence givengrammar, hence leading and trailing cannot be find out")
                    


    