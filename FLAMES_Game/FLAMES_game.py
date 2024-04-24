def name_count():
    n1 = input("Enter your name :")
    n2 = input("Enter your Lover name :")
    res = []
    Y_name = list(n1)
    L_name = list(n2)
    for y in range(0,len(Y_name)):
        if Y_name[y] not in L_name:
            res += [Y_name[y]]
    
    for L in range(0,len(L_name)):
        if L_name[L] not in res and L_name[L] not in Y_name:
            res += [L_name[L]]
    realtionship_finder(res,n1,n2)

def realtionship_finder(c,y,l):
    flames = ['Friends','Lover','Affection','Marriage','Enemy','Sister/brother']
    while len(flames) > 1:
        t = len(c) %  len(flames)
        flames.pop(t - 1)
    
    result = flames[0]
    print(f"Relationship between {y} and {l} is :{result} ")
    co()
def co():
    restart = input("1)You want to continue press 1 \n 2)For Quit press 0 ")
    if restart == '1':
        name_count()
    elif restart == '0':
        print("Thanks for playing ...")
    else:
        print("Invaild choice")
        co()

name_count()
    
            
        
        
    