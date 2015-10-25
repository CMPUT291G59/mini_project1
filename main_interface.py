import main

def main():
    print("Welcome to W&M flight booking system!")
    print("Do you have acount with us? (Y/N)")
    a=input().upper()
    if a=="Y":
        input("")
    if a=="N":
        
    while True:
        print("1.Search Flight?")
        print("2.List exiting bookings?")
        print("3.Rcord flight depure?")
        print("4.Rcord flight arrival?")
        print("5.Log out?")
        user_input = input ("Please enter the opertion number to continue, or 5 to log_out: ")
        if user_input.lower() == '5':print("Welcome to W&M flight booking system!")
    print("Do you have acount with us? (Y/N)")
            break
        elif user_input == "1":
            prescription()
        elif user_input == "2":
            medical_test()
        elif user_input == "3":
            patient_information_update()
        elif user_input == "4":
            search_engine()
        else:
            print("Invalid opertion number.")
            print()
        print()
    print()
    print("Thanks for using W&M flight booking System.")
    print("Your conveniency has always been our first priority.")
    print("We hope you have a nice day.")        
main()