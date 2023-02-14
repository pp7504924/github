#check for github 
A_lst=[]
C_lst=[]
P_lst=[]
while True:
    print("WELCOME TO FLIPKART")
    print("PRESS 1 FOR ADMIN")
    print("PRESS 2 FOR CUSTOMER")
    print("PRESS 0 FOR EXIT")
    print()
    x=int(input("\t ENTER YOUR CHOICE : "))
    print()
    
    if x==1:
        while True:
            print("\t\t PRESS 1 FOR ADMIN REGISTRATION")
            print("\t\t PRESS 2 FOR ADMIN LOGIN")
            print("\t\t PRESS 0 FOR ADMIN EXIT")
            print()
            x=int(input("\t\t\t ENTER YOUR CHOICE : "))
            print()
            
            if x==1:
                A_details={}
                A_username=input("\t\t\t ENTER YOUR NEW USERNAME : ")
                A_password=input("\t\t\t ENTER YOUR PASSWORD : ")
                A_details['username']=A_username
                A_details['password']=A_password
                A_lst.append(A_details)
                print("\t\t\t SUCSSEFULLY REGISTERD.....!")
                print("\t\t\t ___________________________")
                print()
                
            if x==2:
                f=0
                while True:
                    A_name=input("\t\t\t ENTER USERNAME : ")
                    A_pass=input("\t\t\t ENTER PASSWORD : ")
                    print()
                    
                    for i in A_lst:
                        T_name=i.get('username')
                        T_pass=i.get('password')
                        
                        if T_name==A_name and T_pass==A_pass:
                            f=1
                    if f==1:
                        print("\t\t\t LOGIN SUCSSESFULL.....!")
                        print("\t\t\t _______________________")
                        print()
                        #P_details={}
                        while True:
                            print("\t\t\t\t 1. add product")
                            print("\t\t\t\t 2. remove product")
                            print("\t\t\t\t 3. update product")
                            print("\t\t\t\t 4. display product")
                            print("\t\t\t\t 0. exit")
                            print()
                            P=int(input("\t\t\t\t\t enter your choice : "))
                            print()
                            if P==1:
                                P_details={}
                                P_category=input("\t\t\t\t ENTER PRODUCT CATEGORY : ")
                                P_id=input("\t\t\t\t ENTER PRODUCT ID : ")
                                P_name=input("\t\t\t\t ENTER PRODUCT NAME : ")
                                P_price=input("\t\t\t\t ENTER PRODUCT PRICE : ")
                                P_details[P_id]=[P_category,P_name,P_price]
                                P_lst.append(P_details)
                                print(P_lst)
                                print()
                                
                            if P==2:
                                P_remove=input("\t\t\t\t ENTER PRODUCT ID WANT TO REMOVE : ")
                                print()
                                for i in P_lst:
                                    if P_remove in i:
                                        P_lst.remove(i)
                                        print(P_lst)
                                        print()
                                    else:
                                        print("\t\t\t\t WRONG PRODUCT ID.....!")
                                        print("\t\t\t\t ______________________")
                                        print()
                            
                            if P==3:
                                P_update=input("\t\t\t\t ENTER PRODUCT ID FOR UPDATE : ")
                                print()
                                for i in P_lst:
                                    if P_update in i:
                                        P_category=input("\t\t\t\t ENTER PRODUCT CATEGORY : ")
                                        P_name=input("\t\t\t\t ENTER PRODUCT NAME : ")
                                        P_price=input("\t\t\t\t ENTER PRODUCT PRICE : ")
                                        print()
                                        i[P_update]=[P_category,P_name,P_price]
                                        print(P_lst)
                                        print()
                                    else:
                                        print("\t\t\t\t WRONG PRODUCT ID.....!")
                                        print("\t\t\t\t ______________________")
                                        print()       
                                    
                            if P==4:
                                print(P_lst)
                                print()
                                
                            if P==0:
                                break
                        break       
                            
                    else:
                        print("\t\t\t INVALID.....!")
                        print("\t\t\t _____________")
                        print()
                        break
                
            if x==0:
                break
            
    elif(x==2):
        while True:
            print("\t\t PRESS 1 FOR CUSTOMER REGISTRATION")
            print("\t\t PRESS 2 FOR CUSTOMER LOGIN")
            print("\t\t PRESS 0 FOR CUSTOMER EXIT")
            print()
            x=int(input("\t\t\t ENTER YOUR CHOICE : "))
            print()
            if(x==1):
                C_details={}
                C_username=input("\t\t\t ENTER YOUR NEW USERNAME : ")
                C_password=input("\t\t\t ENTER YOUR PASSWORD : ")
                print()
                C_details["username"]=C_username
                C_details["password"]=C_password
                C_lst.append(C_details)
                print("\t\t\t YOU ARE SUCSSESFULLY REGISTERD......!")
                print("\t\t\t ________________________________________")
                print()
            if(x==2):  
                f=0
                while True:
                    C_name=input("\t\t\t ENTER YOUR USERNAME : ")
                    C_pass=input("\t\t\t ENTER YOUR PASSWORD : ")
                    print()
                    for i in C_lst:
                        T_name=i.get("username")
                        T_password=i.get("password")
                        if C_name==T_name and C_pass==T_password:
                            f=1
                    if f==1:
                        print("\t\t\t\t SUCCESSFULLY LOGGIN...!")
                        print("\t\t\t\t ___________________________")
                        print()
                        while True:
                            print("\t\t\t\t\t1. search product by id")
                            print("\t\t\t\t\t2. search product by name")
                            print("\t\t\t\t\t3. search product by category")
                            print("\t\t\t\t\t4. search product by higher price")
                            print("\t\t\t\t\t5. search product by lower price")
                            print("\t\t\t\t\t6. search product by between higher and lower price")
                            print("\t\t\t\t\t7. display all products")
                            print("\t\t\t\t\t8. add to cart")
                            print("\t\t\t\t\t9. check out")
                            print("\t\t\t\t\t10. display offer")
                            print("\t\t\t\t\t11. help & support")
                            print("\t\t\t\t\t0. exit")
                            break
                    
                    
                    else:
                        print("\t\t\t\t INVALID...!")
                        print("\t\t\t\t _____________")
                        print()
                
                     
              
            if(x==0):
                break
    elif(x==0):
        print("\t\t BYE BYE")
        print("\t\t __________")
        break
           
            
            