# database.py
import sqlite3

# Connect to the SQLite database (replace 'your_database.db' with the actual database name)
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

def initialize_database():
    # Create Flights table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Flights (
            FlightID INTEGER PRIMARY KEY,
            DepartureCity TEXT,
            ArrivalCity TEXT,
            DepartureTime TEXT,
            ArrivalTime TEXT,
            Airline TEXT
        )
    ''')

    # Create Bookings table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Bookings (
            BookingID INTEGER PRIMARY KEY,
            FlightID INTEGER,
            PassengerName TEXT,
            SeatNumber TEXT,
            FOREIGN KEY (FlightID) REFERENCES Flights(FlightID)
        )
    ''')

    # Commit the changes
    conn.commit()

# CRUD operations for Flights
def get_all_flights():
    cursor.execute('SELECT * FROM Flights')
    return cursor.fetchall()

def get_flight_details(flight_id):
    cursor.execute('SELECT * FROM Flights WHERE FlightID = ?', (flight_id,))
    return cursor.fetchone()

def add_flight(departure_city, arrival_city, departure_time, arrival_time, airline):
    cursor.execute('''
        INSERT INTO Flights (DepartureCity, ArrivalCity, DepartureTime, ArrivalTime, Airline)
        VALUES (?, ?, ?, ?, ?)
    ''', (departure_city, arrival_city, departure_time, arrival_time, airline))
    conn.commit()

def update_flight(flight_id, departure_city, arrival_city, departure_time, arrival_time, airline):
    cursor.execute('''
        UPDATE Flights
        SET DepartureCity=?, ArrivalCity=?, DepartureTime=?, ArrivalTime=?, Airline=?
        WHERE FlightID=?
    ''', (departure_city, arrival_city, departure_time, arrival_time, airline, flight_id))
    conn.commit()

def cancel_flight(flight_id):
    cursor.execute('DELETE FROM Flights WHERE FlightID = ?', (flight_id,))
    conn.commit()

# CRUD operations for Bookings
def get_bookings_for_flight(flight_id):
    cursor.execute('SELECT * FROM Bookings WHERE FlightID = ?', (flight_id,))
    return cursor.fetchall()

def book_flight(flight_id, passenger_name, seat_number):
    cursor.execute('''
        INSERT INTO Bookings (FlightID, PassengerName, SeatNumber)
        VALUES (?, ?, ?)
    ''', (flight_id, passenger_name, seat_number))
    conn.commit()

def update_booking(booking_id, passenger_name, seat_number):
    cursor.execute('''
        UPDATE Bookings
        SET PassengerName=?, SeatNumber=?
        WHERE BookingID=?
    ''', (passenger_name, seat_number, booking_id))
    conn.commit()

def cancel_booking(booking_id):
    cursor.execute('DELETE FROM Bookings WHERE BookingID = ?', (booking_id,))
    conn.commit()

# Close the connection when the program terminates
def close_database():
    conn.close()
