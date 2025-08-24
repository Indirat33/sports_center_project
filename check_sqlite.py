import sqlite3

def check_database():
    print("Checking database contents...")
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        
        # List all tables
        print("\n=== Tables in database ===")
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        for table in tables:
            print(f"- {table[0]}")
        
        # Check booking_venue table
        print("\n=== Venues ===")
        try:
            cursor.execute("SELECT id, name, venue_type, is_active FROM booking_venue")
            venues = cursor.fetchall()
            if not venues:
                print("No venues found in the database!")
            else:
                for venue in venues:
                    print(f"ID: {venue[0]}, Name: {venue[1]}, Type: {venue[2]}, Active: {bool(venue[3])}")
        except sqlite3.OperationalError as e:
            print(f"Error accessing venues table: {e}")
        
        # Check booking_timeslot table
        print("\n=== Time Slots ===")
        try:
            cursor.execute("SELECT id, venue_id, start_time, end_time, is_active FROM booking_timeslot")
            slots = cursor.fetchall()
            if not slots:
                print("No time slots found in the database!")
            else:
                for slot in slots[:5]:  # Show first 5 slots
                    print(f"ID: {slot[0]}, Venue ID: {slot[1]}, Time: {slot[2]} to {slot[3]}, Active: {bool(slot[4])}")
                if len(slots) > 5:
                    print(f"... and {len(slots) - 5} more slots")
        except sqlite3.OperationalError as e:
            print(f"Error accessing timeslots table: {e}")
        
        conn.close()
        
    except Exception as e:
        print(f"Error accessing database: {e}")

if __name__ == "__main__":
    check_database()
