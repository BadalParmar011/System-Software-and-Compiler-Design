# -*- coding: utf-8 -*-
"""
Created on Wed Sept 1 10:15:40 2021

@author: Badal Parmar
@rollno: 18BCP011
@branch: Computer Engineering
@division: 1

Experiment 3:
    Write a program to convert the non-deterministic grammar into deterministic
    grammar.
"""
final_productions = {}

def find_common_start(lst):
    smallest = len(lst[0])
    temp = {}
    
    if smallest == 1:
        temp[lst[0]] = ['\u03B5']
        for i in range(1,len(lst)):
            temp[lst[0]].append(lst[i][1:])
        
    else:
        key = lst[0][0]
        index = 1
        for i in range(1,smallest):
            to_compare = lst[0][i]
            satisfies = True
            for j in range(1, len(lst)):
                if(lst[j][i]!=to_compare):
                    satisfies = False
                    break
            
            if(satisfies):
                key = key + to_compare
                index = i
            else:
                break
        
        if(key==lst[0]):
            temp[lst[0]] = ['\u03B5']
            for i in range(1,len(lst)):
                temp[lst[0]].append(lst[i][index+1:])
        else:
            temp[key] = lst[0][index+1:]
            for i in range(1,len(lst)):
                temp[lst[0]].append(lst[i][index+1:])
        
        
    return temp
    

def refine_grammar(nt, p):
    temp = p.copy()
    groups = {}
    
    for i in range(len(temp)):
        if not (temp[i][0] in groups):
            groups[temp[i][0]] = [temp[i]]
            
            for j in range(i+1, len(temp)):
                if(temp[j][0]==temp[i][0]):
                    groups[temp[i][0]].append(temp[j])
                    
            groups[temp[i][0]].sort(key=len)
    
    final = []
    new_productions = {}
    dashes = 1
    
    for each in groups:
        if(len(groups[each])==1):
            final.append(groups[each][0])
        else:
            temp = find_common_start(groups[each])
            final.append(list(temp.keys())[0]+nt+("'")*dashes)
            new_productions[nt+("'")*dashes] = temp[list(temp.keys())[0]]         
            dashes+=1
            
    
    final_productions[nt] = final
    
    if(len(new_productions)!=0):
        for each in new_productions:
            refine_grammar(each, new_productions[each])
    
    
non_terminals = int(input("Enter the number of non-terminal symbols in your grammar: "))

productions = {}

for i in range(non_terminals):
    raw_production = input("Enter production number {}: ".format((i+1)))
    temp_production = ''
    for i in range(len(raw_production)):
        if(raw_production[i]!=' '):
            temp_production+=raw_production[i]
            
    lhs, rhs = temp_production.split('->')[0], temp_production.split('->')[1] 
    productions[lhs] = rhs.split('|')


print('\nDeterministic grammar:\n')

for each in productions:
    refine_grammar(each, productions[each])
    
for each in final_productions:
    production = each+'->'
    for i in range(len(final_productions[each])):
        if(i==len(final_productions[each])-1):
            production = production+final_productions[each][i]
        else:
            production = production+final_productions[each][i]+'|'
    
    print(production+'\n')