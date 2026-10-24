"""
Task 04: Flight Booking Console Application — OOP
Kiran Academy Assignment: Kiran Air Booking
Author: Gayatri Bole  : Date: 24/10/2026
Demonstrates 5 Core OOP Concepts in Python:
1. Class and Object: Modeled through Flight, Passenger, Booking, and FlightBookingSystem.
2. Encapsulation: Attributes are protected and seats are safely modified via methods.
3. Inheritance: RegularPassenger and StudentPassenger inherit from abstract base class Passenger.
4. Polymorphism: get_discount_percentage() behaves differently based on passenger type.
5. Abstraction: Abstract base class Passenger defines an abstract discount method.
"""

from abc import ABC, abstractmethod
import sys

# Ensure UTF-8 output encoding for rupee symbol (₹) across all terminals
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# 1. Class and Encapsulation: Flight

class Flight:
    """Represents a flight with encapsulated seat management."""

    def __init__(self, flight_code: str, airline: str, source: str, destination: str, available_seats: int, base_fare: float):
        self._flight_code = flight_code
        self._airline = airline
        self._source = source
        self._destination = destination
        self._available_seats = available_seats  # Encapsulated attribute
        self._base_fare = base_fare

    # Getters (Encapsulation)
    @property
    def flight_code(self) -> str:
        return self._flight_code

    @property
    def airline(self) -> str:
        return self._airline

    @property
    def source(self) -> str:
        return self._source

    @property
    def destination(self) -> str:
        return self._destination

    @property
    def available_seats(self) -> int:
        return self._available_seats

    @property
    def base_fare(self) -> float:
        return self._base_fare

    def has_available_seats(self, tickets: int) -> bool:
        """Checks if enough seats are available without modifying state."""
        return self._available_seats >= tickets

    def book_seats(self, tickets: int) -> bool:
        """
        Encapsulation in action:
        Updates seat count only if sufficient seats are available.
        """
        if self.has_available_seats(tickets):
            self._available_seats -= tickets
            return True
        return False

    def display_details(self):
        """Displays flight information."""
        fare_display = int(self._base_fare) if self._base_fare.is_integer() else f"{self._base_fare:.2f}"
        print(f"Flight Code: {self._flight_code}")
        print(f"Airline: {self._airline}")
        print(f"Route: {self._source} to {self._destination}")
        print(f"Available Seats: {self._available_seats}")
        print(f"Base Fare: ₹{fare_display}\n")

# 2. Abstraction & Inheritance: Passenger (Abstract Base Class)

class Passenger(ABC):
    """
    Abstract base class representing a generic passenger.
    Defines the contract for discount calculation.
    """

    def __init__(self, name: str, age: int, passenger_type: str):
        self._name = name
        self._age = age
        self._passenger_type = passenger_type

    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age

    @property
    def passenger_type(self) -> str:
        return self._passenger_type

    # Abstraction: Abstract method to be overridden by subclasses
    @abstractmethod
    def get_discount_percentage(self) -> float:
        """Returns discount percentage applicable to the passenger."""
        pass

# 3. Inheritance & Polymorphism: Subclasses

class RegularPassenger(Passenger):
    """Represents a regular passenger entitled to 0% discount."""

    def __init__(self, name: str, age: int):
        super().__init__(name, age, "Regular")

    # Polymorphism: Returns 0% discount
    def get_discount_percentage(self) -> float:
        return 0.0


class StudentPassenger(Passenger):
    """Represents a student passenger entitled to 10% discount."""

    def __init__(self, name: str, age: int):
        super().__init__(name, age, "Student")

    # Polymorphism: Returns 10% discount
    def get_discount_percentage(self) -> float:
        return 10.0

# 4. Class and Object: Booking

class Booking:
    """Stores the details of a confirmed flight booking."""

    def __init__(self, booking_id: str, passenger: Passenger, flight: Flight, num_tickets: int, subtotal: float, discount: float, final_amount: float):
        self.booking_id = booking_id
        self.passenger = passenger
        self.flight = flight
        self.num_tickets = num_tickets
        self.subtotal = subtotal
        self.discount = discount
        self.final_amount = final_amount

    def display_summary(self):
        """Displays formatted booking summary."""
        base_fare_disp = int(self.flight.base_fare) if self.flight.base_fare.is_integer() else f"{self.flight.base_fare:.2f}"
        subtotal_disp = int(self.subtotal) if self.subtotal.is_integer() else f"{self.subtotal:.2f}"
        discount_disp = int(self.discount) if self.discount.is_integer() else f"{self.discount:.2f}"
        final_disp = int(self.final_amount) if self.final_amount.is_integer() else f"{self.final_amount:.2f}"
        disc_pct = int(self.passenger.get_discount_percentage())

        print(f"Booking ID: {self.booking_id}")
        print(f"Flight: {self.flight.flight_code}")
        print(f"Route: {self.flight.source} to {self.flight.destination}\n")
        print(f"Passenger Name: {self.passenger.name}")
        print(f"Passenger Age: {self.passenger.age}")
        print(f"Passenger Type: {self.passenger.passenger_type}\n")
        print(f"Number of Tickets: {self.num_tickets}")
        print(f"Base Fare per Ticket: ₹{base_fare_disp}")
        print(f"Subtotal: ₹{subtotal_disp}")
        print(f"{self.passenger.passenger_type} Discount ({disc_pct}%): ₹{discount_disp}\n")
        print(f"Final Amount: ₹{final_disp}\n")

# 5. System Controller: FlightBookingSystem

class FlightBookingSystem:
    """Manages available flights, user bookings, and menu interaction."""

    def __init__(self):
        # Predefined flights
        self.flights = {
            "PN101": Flight("PN101", "Kiran Air", "Pune", "Delhi", 20, 4000.0),
            "MB202": Flight("MB202", "Kiran Air", "Mumbai", "Bengaluru", 30, 3500.0),
            "PH303": Flight("PH303", "Kiran Air", "Pune", "Hyderabad", 25, 3000.0),
        }
        self.latest_booking = None
        self.booking_counter = 1001

    def view_flights(self):
        """Option 1: Display all available flights."""
        print("\n===== AVAILABLE FLIGHTS =====\n")
        for flight in self.flights.values():
            flight.display_details()

    def book_flight(self):
        """Option 2: Validate inputs, calculate fare using polymorphism, and confirm booking."""
        print()
        # 1. Flight Code Validation
        flight_code_input = input("Enter flight code: ").strip().upper()
        if flight_code_input not in self.flights:
            print("\nBooking failed: Invalid flight code. Flight does not exist.\n")
            return

        flight = self.flights[flight_code_input]

        # 2. Passenger Name Validation
        passenger_name = input("Enter passenger name: ").strip()
        if not passenger_name:
            print("\nBooking failed: Passenger name cannot be blank.\n")
            return

        # 3. Passenger Age Validation
        age_input = input("Enter age: ").strip()
        try:
            age = int(age_input)
            if age <= 0:
                print("\nBooking failed: Age must be greater than zero.\n")
                return
        except ValueError:
            print("\nBooking failed: Age must be a valid positive integer.\n")
            return

        # 4. Passenger Type Validation & Object Creation (Polymorphism)
        pass_type_input = input("Passenger type (Regular/Student): ").strip().capitalize()
        if pass_type_input == "Regular":
            passenger = RegularPassenger(passenger_name, age)
        elif pass_type_input == "Student":
            passenger = StudentPassenger(passenger_name, age)
        else:
            print("\nBooking failed: Passenger type must be Regular or Student.\n")
            return

        # 5. Number of Tickets Validation
        tickets_input = input("Enter number of tickets: ").strip()
        try:
            num_tickets = int(tickets_input)
            if num_tickets <= 0:
                print("\nBooking failed: Number of tickets must be greater than zero.\n")
                return
        except ValueError:
            print("\nBooking failed: Number of tickets must be a valid positive integer.\n")
            return

        # 6. Seat Availability Validation
        if not flight.has_available_seats(num_tickets):
            print("\nBooking failed: Not enough seats available.\n")
            return

        # 7. Fare Calculation (Polymorphic call)
        subtotal = num_tickets * flight.base_fare
        discount_percentage = passenger.get_discount_percentage()
        discount_amount = subtotal * (discount_percentage / 100.0)
        final_amount = subtotal - discount_amount

        # 8. Update Seats (Encapsulation) & Create Booking
        flight.book_seats(num_tickets)
        booking_id = f"BK{self.booking_counter}"
        self.booking_counter += 1

        booking = Booking(
            booking_id=booking_id,
            passenger=passenger,
            flight=flight,
            num_tickets=num_tickets,
            subtotal=subtotal,
            discount=discount_amount,
            final_amount=final_amount,
        )
        self.latest_booking = booking

        # 9. Confirmation Display
        print("\n===== BOOKING CONFIRMED =====\n")
        booking.display_summary()

    def view_booking(self):
        """Option 3: View the latest confirmed booking."""
        if self.latest_booking is None:
            print("\nNo confirmed booking found. Please book a flight first.\n")
        else:
            print("\n===== LATEST BOOKING =====\n")
            self.latest_booking.display_summary()

    def run(self):
        """Main loop displaying the menu."""
        while True:
            print("===== KIRAN AIR BOOKING =====\n")
            print("1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit\n")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.view_flights()
            elif choice == "2":
                self.book_flight()
            elif choice == "3":
                self.view_booking()
            elif choice == "4":
                print("\nThank you for using Kiran Air Booking. Goodbye!")
                break
            else:
                print("\nInvalid choice! Please select a valid option (1-4).\n")
                
# Main Entry Point
def main():
    app = FlightBookingSystem()
    app.run()


if __name__ == "__main__":
    main()

