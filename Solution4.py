sen = input()
clauses = sen.split()
for i in range(len(clauses)):
    clauses[i] = clauses[i].replace('_', ' ').title().replace(' ', '')
    clauses[i]= clauses[i][0].lower() + clauses[i][1:]
sen = " ".join(clauses)
print(sen)
