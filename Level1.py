#Level 1
#1
l1=[]
print("1. This is the empty list: ",l1)

#2
a1= [1,2,3.2,4,'s',6]
print("2. A list with more than 5 items: ",a1)

#3
l=len(a1)
print("3. Length of the list a1: ",l)

#4
print("4. First item: ",a1[0])
print("Last item: ",a1[len(a1)-1])
d=l//2
print("Middle item: ",(a1[d]))

#5
mixed_data_types=["Sandhya",21,164,"Umarried","BLR"]
print("5. Mixed data types: ",mixed_data_types)

#6
print("6. Creating the variable it_companies: ")
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)

#7
print("7. Printing the list using print() :",it_companies)

#8
print("8.Length of it_companies: ",len(it_companies))

#9
sl=len(it_companies)
print("9. First Company: ",it_companies[0])
print("Last Company: ",it_companies[sl-1])
print("Middle Company: ",it_companies[sl//2])

#10
it_companies[0]="Cisco"
print("10. List after modifying one of the companies :",it_companies)

#11
it_companies.append("Facebook")
print("11. Adding an it company: ",it_companies)

#12
v=len(it_companies)//2
it_companies.insert(v,"Yahoo")
print("12. Inserting in the middle :",it_companies)

#13
it_companies[0]=it_companies[0].upper()
print("13. Upper case: ",it_companies)

#14
print("14. Printing names with is: ");
for i in it_companies:
    print(i+"#")

#15
c=input("15. Enter the companies name you want to check: ")
print("The companies existed in the list are:")
for i in it_companies:
    if c==i:
        print(i)
    else:
        continue


#16
it_companies.sort()
print("16. The sorted list is: ",it_companies)

#17
it_companies.sort(reverse=True)
print("17. Reversing the list: ",it_companies)

#18
first_three=it_companies[0:3]
print("18. First three companies: ",first_three)

#19
last_three=it_companies[-1:-4:-1]
print("19. Last three companies: ",last_three)

#20
print("20. Middle items :")
l_company=len(it_companies)
cut=l_company % 2
if cut==0:
    middle_company=[it_companies[l_company/2],it_companies[(l_company/2)+1]]
elif cut!=0:
    middle_company=[it_companies[l_company//2]]

print(middle_company)

#21
print("21. Removing the first :")
it_companies.pop(0)
print(it_companies)

#22
print("22. Removing the last :")
it_companies.pop(l-1)
print(it_companies)

#23
print("23. Removing the middle :")
it_companies.pop(len(it_companies)//2)
print(it_companies)

#24
print("24. Removing all the items: ")
it_companies.clear()

#25
print("25. Destroy the list: ")
# del it_companies
# print(it_companies=None)

#26
print("26. Joining the following lists: ")
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux'] 
back_end = ['Node','Express', 'MongoDB'] 
print(front_end+back_end)

#27
print("Full_stack variable: ")
full_stack=front_end+back_end
index=full_stack.index('Redux')
full_stack.insert(index+1,"Python")
full_stack.insert(index+2,"SQL")
print(full_stack)