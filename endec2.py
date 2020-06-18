print("\t\t\t\t***ENDEC***\n")
print("here you can encrypt or decrypt sentences/words")
print("type 0 to close this, type 1 to go back")
print("give a level of encryption, more level denotes more security")
choice=input("to encrypt data type \"encrypt\" to decrypt data type \"decrypt\" :")
if choice=="encrypt":
  while True:
    a=input("data:\n")
    level=int(input("level: "))
    if a=="0":
        print("\nthanks for using me")
        break
    elif (len(a)%2)==1:
        while level>0:
            ar=a[::-1]
            a1=ar[::2]
            a2=a[1::2]
            level=level-1
            a=a2+a1
        print("encrypted:\n"+a2+a1)
    else:
        while level>0:
            ar=a[::-1]
            a1=ar[::2]
            a2=a[::2]
            level=level-1
            a=a1+a2
        print("encrypted:\n"+a1+a2)
elif choice=="decrypt":
  while True:
    a=input("encrypted data:\n")
    level=int(input("level: "))
    if a=="0":
        print("\nthanks for using me")
        break
    elif (len(a)%2)==1:
        while level>0:
            c=len(a)-1
            b=(len(a)-1)/2
            list1=list(a)
            i=0
            a=list(a)
            j=1
            while i<b:
                a[j]=list1[i]
                i=i+1
                j=j+2
            i=0
            while c>(b-1):
                a[i]=list1[c]
                i=i+2
                c=c-1
            b=""
            for i in a:
                b=b+i
            a=b
            level=level-1
        print("decrypted form:\n"+b)
    else:
        while level>0:
            c=len(a)-1
            b=int(len(a)/2)
            list1=list(a)
            i=0
            a=list(a)
            j=c
            while i<b:
                a[j]=list1[i]
                i=i+1
                j=j-2
            i=0
            while c>=b:
                a[i]=list1[b]
                i=i+2
                b=b+1
            d=""
            for i in a:
                d=d+i
            a=d
            level=level-1
        print("decrypted form:\n"+d)
elif choice=="0":
    print("\nthanks for using me")
else:
    print("wrong input")