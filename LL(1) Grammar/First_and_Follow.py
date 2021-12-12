# -*- coding: utf-8 -*-
"""
Created on Mon Oct 04 19:29:15 2021

@author: Badal Parmar
    Write a program to calculate first and follow of a given LL (1) grammar.
"""

grammar = open(r'C:/Users/Badal Parmar/Downloads/input.txt', 
               'r',
               encoding='utf-8')
non_terminal_rules = grammar.readlines()

for i in range(len(non_terminal_rules)):
    non_terminal_rules[i] = non_terminal_rules[i][:-1]
    
rules_of_grammar = {}

for each in non_terminal_rules:
    raw_production = each
    temp_production = ''
    for i in range(len(raw_production)):
        if(raw_production[i]!=' '):
            temp_production+=raw_production[i]
            
    lhs, rhs = temp_production.split('->')[0], temp_production.split('->')[1] 
    if '|' in rhs:
        rules_of_grammar[lhs] = rhs.split('|')
    else:
        rules_of_grammar[lhs] = [rhs]
    
print(rules_of_grammar)   
    
# Function to find the first of a non-terminal symbol
def get_first(symbol, rules_of_grammar):
    if(symbol in firsts):
        return
    else:
        firsts[symbol] = []
    nodes = rules_of_grammar[symbol]
    
    for each in nodes:
        for i in range(len(each)):
            stop = False
            
            if ord(each[i])>=65 and ord(each[i])<=90:
                temp =[]
                if(each[i] in firsts):
                    temp = firsts[each[i]]
                    for first in temp:
                        if(first not  in firsts[symbol]):
                            firsts[symbol].append(first)
                else:
                    get_first(each[i], rules_of_grammar)
                    temp = firsts[each[i]]
                    for first in temp:
                        if(first not in firsts[symbol]):
                            firsts[symbol].append(first)
                
                if('\u03B5' not in temp):
                    stop = True
            else:
                if(each[i] not in firsts[symbol]):
                    firsts[symbol].append(each[i])
                stop = True

            if(stop):
                break
            


#Function to find the follow of a non-terminal symbol                
def get_follow(symbol, rules_of_grammar):
    if(symbol in follows):
        return 
    
    follows[symbol] = []
    for nt in rules_of_grammar:
        for node in rules_of_grammar[nt]:
            if(symbol in node):
                index = node.index(symbol)+1
                
                while(index<len(node)):
                    stop = False
                    
                    if ord(node[index])>=65 and ord(node[index])<=90:
                         temp = firsts[node[index]]
                         for e in temp:
                            if(e!='\u03B5'):
                                if(e not in follows[symbol]):
                                    follows[symbol].append(e)
                         if('\u03B5' not in temp):
                            stop = True
                    else:
                        if(node[index] not in follows[symbol]):
                            follows[symbol].append(node[index])
                        stop = True   
            
                    if(stop): 
                        break
                    
                    index = index+1
                
                if(index==len(node)):
                    temp = []
                    if(nt in follows):
                        temp = follows[nt]
                        for e in temp:
                            if(e not in follows[symbol]):
                                follows[symbol].append(e)
                    else:
                        get_follow(nt, rules_of_grammar)
                        temp = follows[nt]
                        for e in temp:
                            if(e not in follows[symbol]):
                                follows[symbol].append(e)
                        

non_terminal_symbols = list(rules_of_grammar.keys())

# Finding the first of each symbol
firsts ={}    
for each in rules_of_grammar:
    get_first(each, rules_of_grammar)

#Finding the follow of wach symbol
follows = {}
for i in range(len(non_terminal_symbols)):
    get_follow(non_terminal_symbols[i], rules_of_grammar)
    if(i==0):
        follows[non_terminal_symbols[i]].append('$')
           
print('\nFirst of each non-terminal symbol')
for each in firsts:
    print(each+':', firsts[each])
    
print('\nFollow of each non-terminal symbol')
for each in follows:
    print(each+':', follows[each])
    
