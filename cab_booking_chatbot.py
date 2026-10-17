"""
Task 02: Cab Booking Chatbot
Kiran Academy Assignment

A beginner-friendly console-based cab booking chatbot in Python.
"""

import random
import sys

# Ensure UTF-8 output encoding for rupee symbol (₹) across all terminals
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def generate_otp():
    #Generates a random 4-digit OTP.
    return random.randint(1000, 9999)


def book_ride():
    # Step 1: Select Cab Type
   
    print("\n===== SELECT CAB TYPE =====")
    print("1. Auto")
    print("2. Sedan")
    print("3. SUV")
    cab_choice = input("\nEnter your choice: ").strip()

    if cab_choice == "1":
        cab_type = "Auto"
        rate = 12
    elif cab_choice == "2":
        cab_type = "Sedan"
        rate = 18
    elif cab_choice == "3":
        cab_type = "SUV"
        rate = 25
    else:
        print("\nInvalid cab choice! Returning to main menu...\n")
        return

    # Step 2: Select Predefined Route
    
    print("\n===== SELECT ROUTE =====")
    print("1. Pune Station to Shivajinagar - 5 km")
    print("2. Swargate to Kothrud - 8 km")
    print("3. Hinjawadi to Wakad - 10 km")
    route_choice = input("\nEnter route choice: ").strip()

    if route_choice == "1":
        source = "Pune Station"
        destination = "Shivajinagar"
        distance = 5
    elif route_choice == "2":
        source = "Swargate"
        destination = "Kothrud"
        distance = 8
    elif route_choice == "3":
        source = "Hinjawadi"
        destination = "Wakad"
        distance = 10
    else:
        print("\nInvalid route choice! Returning to main menu...\n")
        return

    # Step 3: Calculate Fare
    
    total_fare = distance * rate
    
    # Step 4: Display Ride Details
    
    print("\n===== RIDE DETAILS =====")
    print(f"Cab Type: {cab_type}")
    print(f"Source: {source}")
    print(f"Destination: {destination}")
    print(f"Distance: {distance} km")
    print(f"Rate: ₹{rate}/km")
    print(f"Total Fare: ₹{total_fare}")

    # Step 5: Booking Confirmation & OTP Rule
  
    print("\n===== BOOKING CONFIRMATION =====")
    print("1. Confirm & Share OTP")
    print("2. Cancel Ride")
    confirm_choice = input("\nEnter your choice: ").strip()

    if confirm_choice == "1":
        otp = generate_otp()
        print("\nBooking confirmed successfully!")
        print(f"Your OTP is: {otp}\n")
        print("Once the OTP has been shared,")
        print("the ride cannot be cancelled.\n")
        print("Returning to the main menu...\n")
    elif confirm_choice == "2":
        print("\nRide cancelled successfully.")
        print("Returning to the main menu...\n")
    else:
        print("\nInvalid choice! Returning to the main menu...\n")


def main():
    """Main program loop showing the main menu."""
    while True:
        print("===== CAB BOOKING CHATBOT =====")
        print("1. Book Ride")
        print("2. Exit")
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            book_ride()
        elif choice == "2":
            print("\nThank you for using Cab Booking Chatbot!")
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice! Please select 1 or 2.\n")


if __name__ == "__main__":
    main()

