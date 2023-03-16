def vending_machine():
    print("Make your choice:")
    print(f"1.{first_product}\t{cost1}")
    print(f"2.{second_product}\t{cost2}")
    print(f"3.{third_product}\t{cost3}")
    print("4.exit")

    is_on = True
    Amount_machine = 0
    while is_on:
        choice = int(input("Make your choice: "))
        count = 0
        if choice == 1:
            print(f"Thank you! Here is your {first_product}")
            count += cost1
            Amount_machine += cost1
            # print(f"You have amount {Amount_machine}$ in the machine")
        elif choice == 2:
            print(f"Thank you! Here is your {second_product}")
            count += cost2
            Amount_machine += cost2
            # print(f"You have amount {Amount_machine}$ in the machine")
        elif choice == 3:
            print(f"Thank you! Here is your {third_product}")
            count += cost3
            Amount_machine += cost3
            # print(f"You have amount {Amount_machine}$ in the machine")
        elif choice == 4:
            print(f"You have amount {Amount_machine}$ in the machine")
            is_on = False


import time

print("Let's load the vending machine first!!")
first_product = input("What is the first product? ")
cost1 = float(input("How much it costs? "))
second_product = input("What is the second product? ")
cost2 = float(input("How much it costs? "))
third_product = input("What is the third product? ")
cost3 = float(input("How much it costs? "))

print("Starting machine.....")
time.sleep(1)
print("25%...")
time.sleep(1)
print("50%....")
time.sleep(1)
print("75%...")
time.sleep(1)
print("100%....")
vending_machine()
