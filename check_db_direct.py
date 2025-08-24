import sqlite3

def check_database():
    print("Checking database contents...")
    try:
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        
        # List all tables
        print("\n=== Tables in database ===")
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        for table in tables:
            table_name = table[0]
            print(f"\nTable: {table_name}")
            
            # Get row count
            cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
            count = cursor.fetchone()[0]
            print(f"  Rows: {count}")
            
            # Show column names
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()
            print("  Columns:", ", ".join([col[1] for col in columns]))
            
            # Show sample data for booking tables
            if 'booking_' in table_name and count > 0:
                print("  Sample data:")
                cursor.execute(f"SELECT * FROM {table_name} LIMIT 1;")
                row = cursor.fetchone()
                if row:
                    print("   ", row)
        
        conn.close()
        
    except sqlite3.Error as e:
        print(f"Error checking database: {e}")

if __name__ == "__main__":
    check_database()
