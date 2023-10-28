#for stopping program execution for some time
import time


print("Please insert Your CARD")

#for card processing
time.sleep(1)

password = 1234

#taking atm pin from user
pin = int(input("Enter your atm PIN: "))

#user account balance
balance = 5000

#checking pin is valid or not
for i in range(2, 0, -1):
 if pin == password:

    #loop will run user get free
    while True:

        #Showing  info to user

        print("""
                    1 ==> Check Balance
                    2 ==> Withdraw Cash 
                    3 ==> Deposit Cash
                    4 ==> Reset PIN
                    5 ==> View changed PIN
                    6 ==> Mobile Recharge
                    7 ==> Exit
                    """
              )
 
        try:    
             #taking an option from user
            option = int(input("Please enter your choice: "))
        except:
            print("Please enter valid option: ")
       
        #for option 1        
        if option == 1:
            print(f"Your current balance is {balance}")
       
                                     
        if option == 2:
            withdraw_amount = int(input("Please enter withdraw amount(It should be less than Rs 2000): "))

            for i in range(20, 0, -1):

             if withdraw_amount> 2000:
                print("You cannot withdraw more than Rs 2000 at a time")
                withdraw_amount = int(input("Please enter withdraw amount(It should be less than Rs 2000): "))
               
               
             else: break
            if withdraw_amount > balance:
                print("Sorry there are insufficient funds in your account")

            else:
                balance = balance-withdraw_amount
                print(f"{withdraw_amount} was debited from your account")
                print(f"Your current balance is {balance}")



           

        if option == 3:

            deposit_amount = int(input("Please enter your Deposit Amount: "))

            balance = balance + deposit_amount

           

            print(f"{deposit_amount} is credited to your account")



            print(f"Your updated balance is: {balance}")

        if option == 4:
            password = int(input("Enter your new PIN: "))
            print("Your PIN was reset successfully!")
        if option == 5:
            print(f"Your updated PIN is {password}")

        if option == 6:
            print("Reacharge your mobile number.")
            mobile_recharge = int(input("Please enter your mobile number:"))
            print('''Please choose your service provider.
                    1. Jio
                    2. Airtel
                    3. Vodafone
                    4. Idea
                    5. BSNL
                    ''')
              
             #taking an option from user
            option = int(input("Please enter your choice :"))
            
            if option == 1:
                print('''PLans
                        1.150  (unlimited 1.5GB/day)
                        2.200  (unlimited 2GB/day)
                        3.99   (2 GB,60 days)''')
                option =int(input("Choose your plan:"))  
                print("Your plan is succesfully activited") 
            if option == 2:
                print('''Plans
                        1.150  (unlimited 1.5GB/day)
                        2.200  (unlimited 2GB/day)
                        3.99   (2 GB,60 days)''')
                option =int(input("Choose your plan:"))  
                print("Your plan is succesfully activited")

            if option == 3:
                print('''Plans
                        1.199  (unlimited 1.5GB/day)
                        2.299  (unlimited 2GB/day)
                        3.100  (2 GB,60 days)''')
                option =int(input("Choose your plan:"))  
                print("Your plan is succesfully activited") 

            if option == 4:
                print('''Plans
                        1.249  (unlimited 1.5GB/day)
                        2.349  (unlimited 2GB/day)
                        3.95  (2 GB,60 days)''')
                option =int(input("Choose your plan:"))  
                print("Your plan is succesfully activited")

            if option == 5:
                print('''Plans
                        1.249  (unlimited 1.5GB/day)
                        2.349  (unlimited 2GB/day)
                        3.100  (2 GB,60 days)''')
                option =int(input("Choose your plan:"))  
                print("Your plan is succesfully activited") 

            if option == 6:
                print('''Plans
                        1.150  (unlimited 1.5GB/day)
                        2.200  (unlimited 2GB/day)
                        3.99   (2 GB,60 days)''')
                option =int(input("Choose your plan:"))  
                print("Your plan was succesfully activited")              

            

        if option == 7:
       
            print("Thank you for banking with us!")

            
            break
    break
           
   
 else:
     pin = int(input("WRONG PIN. Please try again: "))
if i == 1:
    print("Due to incorrect PIN 3 times, your card has been blocked!")
    print("Kindly contact us for PIN recall")
