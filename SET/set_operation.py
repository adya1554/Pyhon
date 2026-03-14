stud1 = {'English','Maths','comp-sci','chem','bio'}
stud2 = {'English','bio','physics','chem','hindi'}
stud3 = {'kannada','marathi','English'}

# intersection
common_subject = stud1.intersection(stud2)
print(common_subject)

print(stud1 & stud2)

# union 
print('all subject both stud learning -',stud1.union(stud2,stud3))
print('common subject from three students -',stud1.intersection(stud2,stud3))