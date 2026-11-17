print("====================================")
print("      Welcome to Ride Builder!      ")
print("====================================")

print(" Step 1: Choose your vehicle")
print("  1 - Bike")
print("  2 - Car")
print()

choice = int(input("Enter  1 or 2: "))
print()

if choice == 1:
    print("You have chosen Bike")
    print("Step 2: Choose your bike type")
    print("  1 - Mountain Bike")
    print("  2 - Scooty ")
    print()
    bike_choice = int(input("Enter 1 or 2: "))
    print()

    if  bike_choice == 2:
        print("You have chosen Scooty")
        print("Top speed:  80 km/h")
        print(" Best for :  City Roads")
    else:
        print(" You have chosen Mountain Bike")
        print("Top speed:  40 km/h" )
        print(" Best for :  Off-Roads")
elif choice == 2:
    print(" Step 2: Pick your car type")
    print(" 1 - Sedan")
    print(" 2 - SUV ")
    print()
    car_choice = int(input("Pick 1 or 2."))
    if car_choice == 2:
        print("You Have choosen the SUV.")
        print("Top Speed : 150 Km/h ")
        print("Best for : Big car")
    else:
        print("You have choosen the Sedan")
        print("Top speed : 150 Km/h ")
        print("Best for : City roads")




else:
      print("    Invaild Response   ")



    