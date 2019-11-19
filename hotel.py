import pickle

def printMenu():
    print("Welcome to the South Moreland Motor Hotel")
    print("1. Check in!")
    print("2. Check out")
    print("3. Check the guest lists (HOTEL MANAGEMENT ONLY PLZ)")
    print("4. exit hotel management software")

def printGuests(hotel):
    for floor, place in hotel.items():
        print(f"floor {floor}")
        for room, guests in place.items():
            print(f"room {room} has these guests :")
            for name in guests:
                print(name)

def checkIn(hotel):
    floor = input("what floor is the room you would like to check into? ")
    if floor not in hotel:
        print("We don't have that floor!")
        return hotel
    room = input("what room?" )
    if room in hotel[floor]:
        print("somebody is already in that room!")
        return hotel
    guests = int(input("How many people are checking in? "))
    guest_list = []
    for x in range(guests):
        guest_list.append(input(f"who is person number {x+1}? "))
    hotel[floor][room] = guest_list
    return hotel
    
def checkOut(hotel):
    floor = input("what floor is the room you would like to check out of? ")
    if floor not in hotel:
        print("We don't have that floor!")
        return hotel
    room = input("what room?" )
    if room not in hotel[floor]:
        print("Theres nobody staying in that room!")
        return hotel
    guests = hotel[floor].pop(room, False)
    print(f"thanks for staying with us {guests}")

    return hotel

def main():
    hotel = {'1': {}, "2" : {}, '3' : {}, '4': {}}
    file_name = "hotel.pickle"
    try:
        with open (file_name, 'rb') as file_handle:
            hotel = pickle.load(file_handle)
    except:
        pass

    choice = None
    while choice != '4':
        printMenu()
        choice = input("what would you like to do? ")
        if choice == '1':
            hotel = checkIn(hotel)
        if choice == '2':
            hotel = checkOut(hotel)
        if choice =='3':
            printGuests(hotel)
    print("Thanks for visiting the front desk. bye.")
    with open(file_name, "wb") as file_handle:
        pickle.dump(hotel, file_handle)

main()
