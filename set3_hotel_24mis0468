print("Hotel System")
def manage_hotel_bookings():
    bookings = [
        {"guest_name": "sriram", "room_type": "Deluxe", "nights": 3, "cost_per_night": 150},
        {"guest_name": "Vidhanshu", "room_type": "Standard", "nights": 5, "cost_per_night": 80},
        {"guest_name": "Agile", "room_type": "Suite", "nights": 2, "cost_per_night": 300},
        {"guest_name": "ayush", "room_type": "Standard", "nights": 1, "cost_per_night": 80},
        {"guest_name": "pallab", "room_type": "Deluxe", "nights": 4, "cost_per_night": 150}
    ]

    for booking in bookings:
        booking["total_bill"] = booking["nights"] * booking["cost_per_night"]

    print("--- Guest Total Bills ---")
    for b in bookings:
        print(f"Guest: {b['guest_name']}, Total Bill: ${b['total_bill']}")

    highest_billed_guest = max(bookings, key=lambda x: x["total_bill"])
    print(f"\nHighest Bill: {highest_billed_guest['guest_name']} (${highest_billed_guest['total_bill']})")

    room_counts = {}
    for b in bookings:
        room_counts[b["room_type"]] = room_counts.get(b["room_type"], 0) + 1
    
    print("\n--- Bookings by Room Type ---")
    for room, count in room_counts.items():
        print(f"{room}: {count}")

    total_revenue = sum(b["total_bill"] for b in bookings)
    print(f"\nTotal Revenue: ${total_revenue}")

    sorted_bookings = sorted(bookings, key=lambda x: x["total_bill"], reverse=True)
    print("\n--- Bookings Sorted by Total Bill (Highest First) ---")
    for b in sorted_bookings:
        print(f"Name: {b['guest_name']}, Room: {b['room_type']}, Bill: ${b['total_bill']}")

manage_hotel_bookings()
