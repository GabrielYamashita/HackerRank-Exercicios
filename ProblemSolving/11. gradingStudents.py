# -*- coding: utf-8 -*-

#print(35%5)

grades=[73,67,38,33]

def gradingStudents(grades):
    i=0
    while i < len(grades):
        if grades[i] >= 38:
            if (grades[i]+1)%5 == 0:
                grades[i] = grades[i]+1
            
            if (grades[i]+2)%5 == 0:
                grades[i] = grades[i]+2
        i+=1 
    return grades
        
print(gradingStudents(grades))