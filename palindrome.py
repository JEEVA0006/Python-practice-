integer=int(input("Enter the integer:"))
if str(integer)==str(integer)[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")