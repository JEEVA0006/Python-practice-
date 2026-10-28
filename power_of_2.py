n=int(input("Enter number to be checked:")) 
verify=False
for i in range(n//2):
    if 2**i==n or n==2:
        verify=True
print(verify)
