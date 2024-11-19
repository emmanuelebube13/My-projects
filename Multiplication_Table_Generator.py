try:
    a = int(input("\nEnter the number you want the multiplication table for and press Enter: "))
    maxnumer = int(input("\nEnter how long you want your Table: "))
    b = 1

    while  True:
        c = a * b
        print(f"{a} * {b} = {c}")
        b += 1
        if b > maxnumer:
            break
    print("\nThank you!")
except ValueError:
    print("\nInvalid input! Please entere a valid number.")