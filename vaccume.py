def vacuum(a, b, pos):
    while a == 1 or b == 1:
        if pos == 'A':
            if a == 1:
                print("Clean Room A")
                a = 0
            else:
                print("Move Right")
                pos = 'B'
        else:
            if b == 1:
                print("Clean Room B")
                b = 0
            else:
                print("Move Left")
                pos = 'A'

    print("Both rooms are clean")


a = int(input("Room A (1/0): "))
b = int(input("Room B (1/0): "))
pos = input("Position (A/B): ")

vacuum(a, b, pos)