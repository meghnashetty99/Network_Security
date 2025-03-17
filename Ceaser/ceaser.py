letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(text,key):
    cip=[]
    for ch in text:
        if ch.upper() in letters:
            ind=(letters.index(ch.upper())+key)%26
            cip.append(letters[ind])
        else:
            cip.append(ch)
    return "".join(cip)

def decrypt(text,key):
    cip=[]
    for ch in text:
        if ch.upper() in letters:
            ind=(letters.index(ch.upper())-key)%26
            cip.append(letters[ind])
        else:
            cip.append(ch)
    return "".join(cip)

print("For Encryption\n")
text=str(input("Enter the text :"))
key=int(input("Enter the key : "))
et=encrypt(text,key)
print("Encrypted Text :\n",et)

print("\nFor Decryption\n")
text=str(input("Enter the text :"))
key=int(input("Enter the key : "))
dt=decrypt(text,key)
print("Encrypted Text :\n",dt)