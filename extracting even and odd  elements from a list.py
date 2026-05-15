print("extracting even and odd indices elements from a list\n")
list=[]
even_list=[]
odd_list=[]
n=int(input("enter no. of terms:"))
for i in range(0,n):
    elements=int(input(f"enter the element {i+1}:"))
    list.append(elements)
    if (list[i]%2==0):
        even_list.append(list[i])
    else:
        odd_list.append(list[i])    
print("your list is",list)
print("even elements",even_list)
print("odd elements",odd_list)