# Enter your code here. Read input from STDIN. Print output to STDOUT
n=  raw_input().split()
List1=[]
List2=[]
for x in range(1,int(n[0])+1): #for the first set of elements I append the list1
    cm=raw_input()
    List1.append(cm)
for _ in range(int(n[1])): # and then to the list2
    Cm=raw_input()
    List2.append(Cm)
for x in List2:
            print (' '.join([str(i+1) for i, y in enumerate(List1) if y == x]) or -1)
#this last line joins every index if the list1 if  y(element of list1)   is equal to the  of the list2(x). in contrary case prints -1