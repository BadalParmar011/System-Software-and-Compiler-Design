Given_Grammar = open(r'grammar2.txt',
                     'r',
                     encoding='utf-8')
N_Rules = Given_Grammar.readlines()

for x in range(len(N_Rules)):
    N_Rules[x] = N_Rules[x][:-1]

# Printing the grammar
print('\nGiven Grammar')
for item in N_Rules:
    print(item)

R_Grammar = {}

for item in N_Rules:
    initial_production = item
    intermediate_production = ''
    for x in range(len(initial_production)):
        if initial_production[x] != ' ':
            intermediate_production += initial_production[x]

    lhs, rhs = intermediate_production.split('->')[0], intermediate_production.split('->')[1]
    if '|' in rhs:
        R_Grammar[lhs] = rhs.split('|')
    else:
        R_Grammar[lhs] = [rhs]

# Checking whether the grammar is operator precedence or not

P_Operator = True

for non_terminal in R_Grammar:
    for given_production in R_Grammar[non_terminal]:

        if '\u03B5' in given_production:
            P_Operator = False
            break

        var = None
        if given_production[0].isalpha():
            var = True
        else:
            variable = False

        for x in range(1, len(given_production)):
            if given_production[x].isalpha() and var == True:
                P_Operator = False
                break
            elif given_production[x].isalpha() and var == False:
                variable = True
            elif (not given_production[x].isalpha()) and var == False:
                P_Operator = False
                break
            else:
                var = False

        if not P_Operator:
            break

    if not P_Operator:
        break


# Function to find the leading of a non-terminal symbol
def get_leading(symbol, rules_of_grammar):
    if symbol in leads:
        return
    else:
        leads[symbol] = []
    nodes = rules_of_grammar[symbol]

    for item in nodes:
        x = 0
        if item[x].isalpha() and item[x].isupper():
            if x != len(item) - 1:
                if item[x + 1] not in leads[symbol]:
                    leads[symbol].append(item[x + 1])

            if item[x] in leads:
                for leading in leads[item[x]]:
                    if leading not in leads[symbol]:
                        leads[symbol].append(leading)
            else:
                get_leading(item[x], rules_of_grammar)

                for leading in leads[item[x]]:
                    if leading not in leads[symbol]:
                        leads[symbol].append(leading)

        else:
            if item[x] not in leads[symbol]:
                leads[symbol].append(item[x])


# Function to find the leading of a non-terminal symbol
def get_trailing(symbol, rules_of_grammar):
    if symbol in trails:
        return
    else:
        trails[symbol] = []
    nodes = rules_of_grammar[symbol]

    for item in nodes:
        x = len(item) - 1
        if item[x].isalpha() and item[x].isupper():
            if x != 0:
                if item[x - 1] not in trails[symbol]:
                    trails[symbol].append(item[x - 1])

            if item[x] in trails:
                for trailing in trails[item[x]]:
                    if trailing not in trails[symbol]:
                        trails[symbol].append(trailing)
            else:
                get_trailing(item[x], rules_of_grammar)

                for trailing in trails[item[x]]:
                    if trailing not in trails[symbol]:
                        trails[symbol].append(trailing)

        else:
            if item[x] not in trails[symbol]:
                trails[symbol].append(item[x])


if P_Operator:
    print("\nThe grammar is an operator precedence grammar")

    non_terminal_symbols = list(R_Grammar.keys())

    # Finding the leading of item symbol
    leads = {}
    for item in R_Grammar:
        get_leading(item, R_Grammar)

    # Finding the trailing of item symbol
    trails = {}
    for item in R_Grammar:
        get_trailing(item, R_Grammar)

    print('\nLeading of item non-terminal symbol')
    for item in leads:
        print(item + ':', leads[item])

    print('\nTrailing of item non-terminal symbol')
    for item in trails:
        print(item + ':', trails[item])

else:
    print("\nGrammar is not an Operator Precedence grammar, no further leading and trailing")
