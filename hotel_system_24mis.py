print("Hotel System by Sriram ( 24Mis0468")

# 1. Setup the booking data for all guests -- by default data we are adding
bookings = [
    {"name": "sriram", "type": "Deluxe", "nights": 3, "price": 150},
    {"name": "Vidhanshu", "type": "Standard", "nights": 5, "price": 80},
    {"name": "Agile", "type": "Suite", "nights": 2, "price": 300},
    {"name": "ayush", "type": "Standard", "nights": 1, "price": 80},
    {"name": "pallab", "type": "Deluxe", "nights": 4, "price": 150}
]

# 2.calc and print final output for all guests
print("\n--- Guest Total Bills ---")
for b in bookings:
    b["bill"] = b["nights"] * b["price"]
    print(f"Guest: {b['name']}, Total Bill: ${b['bill']}")

# 3. Highest paid guest
highest_guest = bookings[0] 
for b in bookings:
    if b["bill"] > highest_guest["bill"]:
        highest_guest = b
print(f"\nHighest Bill: {highest_guest['name']} (${highest_guest['bill']})")

# 4. count number of room
room_counts = {}
for b in bookings:
    room = b["type"]
    if room in room_counts:
        room_counts[room] += 1
    else:
        room_counts[room] = 1

print("\n--- Bookings by Room Type ---")
for room, count in room_counts.items():
    print(f"{room}: {count}")

# 5. Calculate total revenue
total_revenue = 0
for b in bookings:
    total_revenue += b["bill"]
print(f"\nTotal Revenue: ${total_revenue}")

# 6. Sort bookings by highest to lowest
def get_bill(booking_item):
    return booking_item["bill"]

bookings.sort(key=get_bill, reverse=True)

print("\n--- Bookings Sorted by Total Bill (Highest First) ---")
for b in bookings:
    print(f"Name: {b['name']}, Room: {b['type']}, Bill: ${b['bill']}")
