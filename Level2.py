ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort() 
print(ages)
min_age=ages[0]
print("Minimum age: ",min_age)

l=len(ages)
max_age=ages[l-1]
print("Maximum age: ",max_age)

ages.append(min_age)
ages.append(max_age)
print(ages)


if l%2==0:
    median=((ages[l//2])+(ages[(l//2)-1]))//2
else:
    median=ages[l//2]
print("Median: ",median)

print(ages) 
print("Average Age: ")
total=0
for i in ages:
    total+=i
average=total/len(ages)
print(average)

print("Range of the ages: ")
print(max_age-min_age)

print("Comparing using abs()")
diff1=abs(min_age-average)
diff2=abs(max_age-average)
print("Minimum - Average: ",diff1)
print("Maximum -Average: ",diff2)

if diff1>diff2:
    print("Minimum - Average age is greater in value")
elif diff1<diff2:
    print("Maximum - Average age is greater in value")


countries=['China', 'Russia', 'USA', 'India', 'Sweden', 'Norway', 'Denmark']
print(countries)

l1=len(countries)
if l1%2==0:
    med=((countries[l1//2])+(countries[(l1//2)-1]))//2
else:
    med=countries[l1//2]
print("Median: ",med)



