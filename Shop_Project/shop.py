from collections import defaultdict
from pandas import DataFrame

class shop:
    iteams = {"Iteam_Name" : ["Fruits","apple","orange","pinapple","Vegitable",'Tomato', 'Potato', 'Carrot',"ELECTRONICS","LED blub","Charger","Headphone"], 
              "QTY/KG":['-',100,200,150,'-',200,300,100,'-',1000,500,3000], 
              "Price":['-',119,50,40,'-',30,20,40,'-',200,350,1500]}
    s_name = "AKC Store"
    Owner = "MUTHU KUMAR"
    s_Address = "Srivilliputtur"
    
    def __init__(self,name,mob):
        self.name = name
        self.mob = mob
        self.price = 0
        self.cart = defaultdict(list)
    
    def show_iteams(self):
        iteam = DataFrame(self.iteams)
        print(iteam)
    
    def Fruits(self):
        print(f"{'-'*8}Avalable Fruits{'-'*8}\n"
              "1.Apple\n"
              "2.Orange\n"
              "3.Pinapple\n"
              "4.Return to cart]\n"
              "5.Exit")
        fn = int(input("Choose the number:"))
        if fn == 1:
            f = {"Iteam_Name" : ["Fruits","apple"], 
                "QTY/KG":['-',100], 
                "Price":['-',119]}
            print(DataFrame(f))
            c = int(input("Enter 1 for Qty choose (or) 0 for exit"))
            if c ==1:
                qty = eval(input("Enter the Qty :"))
                if qty in range(1,101):
                    self.price += 119*qty
                    self.cart['Iteam_Name'] += ['Apple']
                    self.cart['Qty/KG'] += [qty]
                    self.cart['Total Price'] += [self.price]
                    print("Added Successfully!")
                    self.Add_to_cart()
                       
            else:
                self.Fruits()
            
        elif fn == 2:
            f = {"Iteam_Name" : ["Fruits","Orange"], 
                "QTY/KG":['-',200], 
                "Price":['-',50]}
            print(DataFrame(f))
            c = int(input("Enter 1 for Qty choose (or) 0 for exit"))
            if c ==1:
                qty = eval(input("Enter the Qty :"))
                if qty in range(1,201):
                    self.price += 50*qty
                    self.cart['Iteam_Name'] += ['Orange']
                    self.cart['Qty/KG'] += [qty]
                    self.cart['Total Price'] += [self.price]
                    print("Added Successfully!")
                    self.Add_to_cart()
                    
                    
            else:
                self.Fruits()
                
        elif fn == 3:
            f = {"Iteam_Name" : ["Fruits","Pinapple"], 
                "QTY/KG":['-',150], 
                "Price":['-',40]}
            print(DataFrame(f))
            c = int(input("Enter 1 for Qty choose (or) 0 for exit"))
            if c ==1:
                qty = eval(input("Enter the Qty :"))
                if qty in range(1,151):
                    self.price += 40*qty
                    self.cart['Iteam_Name'] += ['Pinapple']
                    self.cart['Qty/KG'] += [qty]
                    self.cart['Total Price'] += [self.price]
                    print("Added Successfully!")
                    self.Add_to_cart()
                    
                    
            else:
                self.Fruits()
            
        elif fn == 4:
            self.Add_to_cart()
            
        elif fn == 5:
            self.Exit()
                
        else:
            print("Invalid Choice")
            self.Fruits()
            
    def Vegitables(self):
        print(f"{'-'*8}Avalable Vegitables{'-'*8}\n"
              "1.Tomato\n"
              "2.Potato\n"
              "3.Carrot\n"
              "4.Return to cart\n"
              "5.Exit")
        fn = int(input("Choose the number:"))
        if fn == 1:
            f = {"Iteam_Name" : ["Vegitables","Tomato"], 
                "QTY/KG":['-',200], 
                "Price":['-',30]}
            print(DataFrame(f))
            c = int(input("Enter 1 for Qty choose (or) 0 for exit"))
            if c ==1:
                qty = eval(input("Enter the Qty :"))
                if qty in range(1,201):
                    self.price += 30*qty
                    self.cart['Iteam_Name'] += ['Tomato']
                    self.cart['Qty/KG'] += [qty]
                    self.cart['Total Price'] += [self.price]
                    print("Added Successfully!")
                    self.Add_to_cart()
                    
                    
            else:
                self.Vegitables()
            
        elif fn == 2:
            f = {"Iteam_Name" : ["Vegitables","Potato"], 
                "QTY/KG":['-',300], 
                "Price":['-',20]}
            print(DataFrame(f))
            c = int(input("Enter 1 for Qty choose (or) 0 for exit"))
            if c ==1:
                qty = eval(input("Enter the Qty :"))
                if qty in range(1,301):
                    self.price += 20*qty
                    self.cart['Iteam_Name'] += ['Potato']
                    self.cart['Qty/KG'] += [qty]
                    self.cart['Total Price'] += [self.price]
                    print("Added Successfully!")
                    self.Add_to_cart()
                    
                    
            else:
                self.Vegitables()
                
        elif fn == 3:
            f = {"Iteam_Name" : ["Vegitables","Carrot"], 
                "QTY/KG":['-',100], 
                "Price":['-',40]}
            print(DataFrame(f))
            c = int(input("Enter 1 for Qty choose (or) 0 for exit"))
            if c ==1:
                qty = eval(input("Enter the Qty :"))
                if qty in range(1,101):
                    self.price += 40*qty
                    self.cart['Iteam_Name'] += ['Carrot']
                    self.cart['Qty/KG'] += [qty]
                    self.cart['Total Price'] += [self.price]
                    print("Added Successfully!")
                    self.Add_to_cart()
                    
                    
            else:
                self.Vegitables()
        
        elif fn == 4:
            self.Add_to_cart()
            
        elif fn == 5:
            self.Exit()
                
        else:
            print("Invalid Choice")
            self.Vegitables()
    
    def Electronics(self):
        print(f"{'-'*8}Avalable Electronics{'-'*8}\n"
              "1.LED blub\n"
              "2.Charger\n"
              "3.Headphone\n"
              "4.Return to cart\n"
              "5.Exit")
        fn = int(input("Choose the number:")) 
        if fn == 1:
            f = {"Iteam_Name" : ["Electronics","LED blub"], 
                "QTY/KG":['-',1000], 
                "Price":['-',200]}
            print(DataFrame(f))
            c = int(input("Enter 1 for Qty choose (or) 0 for exit"))
            if c ==1:
                qty = eval(input("Enter the Qty :"))
                if qty in range(1,1001):
                    self.price += 200*qty
                    self.cart['Iteam_Name'] += ['LED blub']
                    self.cart['Qty/KG'] += [qty]
                    self.cart['Total Price'] += [self.price]
                    print("Added Successfully!")
                    self.Add_to_cart()
                    
                    
            else:
                self.Electronics()
            
        elif fn == 2:
            f = {"Iteam_Name" : ["Electronics","Charger"], 
                "QTY/KG":['-',500], 
                "Price":['-',350]}
            print(DataFrame(f))
            c = int(input("Enter 1 for Qty choose (or) 0 for exit"))
            if c ==1:
                qty = eval(input("Enter the Qty :"))
                if qty in range(1,501):
                    self.price += 350*qty
                    self.cart['Iteam_Name'] += ['Charger']
                    self.cart['Qty/KG'] += [qty]
                    self.cart['Total Price'] += [self.price]
                    print("Added Successfully!")
                    self.Add_to_cart()
                    
                    
            else:
                self.Electronics()
                
        elif fn == 3:
            f = {"Iteam_Name" : ["Electronics","Headphone"], 
                "QTY/KG":['-',3000], 
                "Price":['-',1500]}
            print(DataFrame(f))
            c = int(input("Enter 1 for Qty choose (or) 0 for exit"))
            if c ==1:
                qty = eval(input("Enter the Qty :"))
                if qty in range(1,3001):
                    self.price += 1500*qty
                    self.cart['Iteam_Name'] += ['Headphone']
                    self.cart['Qty/KG'] += [qty]
                    self.cart['Total Price'] += [self.price]
                    print("Added Successfully!")
                    self.Add_to_cart()
                    
                    
            else:
                self.Electronics()
        elif fn == 4:
            self.Add_to_cart()
            
        elif fn == 5:
            self.Exit()
                
        else:
            print("Invalid Choice")
            self.Electronics()
    
    def Add_to_cart(self):
        print(f"{'-'*8}Choose the Number{'-'*8}\n"
              "1.Fruits\n"
              "2.Vegitables\n"
              "3.Electronics\n"
              "4.Bill Cunter\n"
              f"{'-'*30}")
        ch = int(input("Enter a option: "))
        
        if ch == 1:
            self.Fruits()
        
        elif ch == 2:
            self.Vegitables()
        
        elif ch == 3:
            self.Electronics()
            
        elif ch == 4:
            self.show_cart()
        
        else:
            print(f"\n\t{ch} is not valid choice.")
            
    def show_cart(self):
        print(DataFrame(self.cart))
        
    def Exit(self):
        print("\nThank you for shopping with us!")
    
demo = shop("demo",2040982109)
demo.show_iteams()
demo.Add_to_cart()
demo.show_cart()
