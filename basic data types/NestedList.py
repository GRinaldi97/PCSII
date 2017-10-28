L=[]
SecondMinimum= int()
AllMarks= set()
Names=[]
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    L.append([name , score])
for Student in L:
    AllMarks.add(Student[1])
SecondMinimum= sorted((list(set(AllMarks))))[1] 
for y in L :
    if y[1]==SecondMinimum:
         Names.append(y[0])
for FName in sorted(Names):
    print FName