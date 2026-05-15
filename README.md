# extracting-even-and-odd-elements-from-a-list
Extracting Even and Odd Elements from a List
📌 Aim

To read elements into a list and separate them into even and odd numbers.

💻 Python Program
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
▶️ Sample Output
extracting even and odd indices elements from a list

enter no. of terms:5
enter the element 1:10
enter the element 2:7
enter the element 3:22
enter the element 4:9
enter the element 5:14

your list is [10, 7, 22, 9, 14]
even elements [10, 22, 14]
odd elements [7, 9]
🧠 Explanation
The user enters the number of elements.
Elements are stored in a list using append().
Using the modulus operator %:
If a number is divisible by 2, it is added to even_list.
Otherwise, it is added to odd_list.
Finally, the original list, even elements, and odd elements are displayed.
📚 Concepts Used
Lists
for loop
if-else condition
Modulus operator %
User input
append() method
