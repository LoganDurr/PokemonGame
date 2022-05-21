from dis import dis
from operator import not_
import csv
from re import M

def effectivenessCalculator(attack_type, defender_type):
    #2d array to determine the effectiveness of the move
    f = open('effectivenessMatrix.csv')
    matrix = []
    for line in f:
        data_line = line.rstrip().split('\t')
        data_line = line.split(',')
        matrix.append(data_line)
    temp_string = matrix[0][-1]
    temp_string = temp_string[:-1]
    matrix[0][-1] = temp_string
    #converts all necesarry values to floats for calculator
    for i in range(len(matrix)):
        if i >= 1:
            for j in range(len(matrix[i])):
                if j >= 1:
                    matrix[i][j] = float(matrix[i][j])

    for i in range(len(matrix)):
        if matrix[i][0] == attack_type:
            p1 = i
            break
        
    for j in range(len(matrix[0])):
        if matrix[0][j] == defender_type:
            p2 = j
            break
    return matrix[p1][p2]

'''displayer'''
def effectivenessDisplayer(attacker_type, defender_type):
    #creates the message the user sees after the attack to tell if it was effective or not
    displayer = effectivenessCalculator(attacker_type, defender_type)
    if displayer == .5:
        print('The move is not very effective')
    elif displayer == 1:
        print('The move is effective')
    elif displayer == 1.5:
        print('The move is super effective!')

    



