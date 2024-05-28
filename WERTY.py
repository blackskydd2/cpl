inpt=input("Enter a Message:")

alpha=["\\",']','P','O','I','U','Y','T','R','E','W','Q','None',"'",';','L','K','J','H','G','F','D','S','A','None','/','.',',','M','N','B','V','C','X','Z','None',' ',' ']
alpha1=[]
for k in range(len(inpt)):
    for i in range(len(alpha)-1):
        if inpt=='Q' or inpt=='A' or inpt=='Z':
            continue
        elif inpt[k]==alpha[i]:
            print(alpha[i+1],end="")
        else:
            pass
            
            


    