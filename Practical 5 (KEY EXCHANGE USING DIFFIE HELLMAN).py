p=23 
g=5 
print("Publicly Shared Values:")
print("Prime (p):", p )
print("Base (g):", g)
a=6
A=(g ** a)% p 
b=15
B=(g ** b)% p
print("\n Alice's Public Key(A):", A)
print("Bob's Public Key(B):", B)
secret_Alice=(B ** a)% p
secret_Bob=(A ** b)% p
print("\n Shared Secret computed by Alice's:", secret_Alice)
print("Shared Secret computed by Bob:", secret_Bob)
if secret_Alice==secret_Bob:
    print("\nKey Exchange Successfull!Shared Secret Key=", secret_Alice)
else:
    print("\nKey Exchange Failed!")
