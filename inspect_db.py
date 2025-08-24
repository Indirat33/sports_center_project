import sqlite3
import os

def inspect_database():
    db_path = 'db.sqlite3'
    if not os.path.exists(db_path):
        print(f"Error: Database file not found at {os.path.abspath(db_path)}")
        return

    print(f"Database file: {os.path.abspath(db_path)}")
    print(f"File size: {os.path.getsize(db_path) / 1024:.2f} KB")
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # List all tables
        print("\n=== Tables in database ===")
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        for table in tables:
            table_name = table[0]
            print(f"\nTable: {table_name}")
            print("-" * (len(table_name) + 8))
            
            # Get column info
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()
            print("Columns:")
            for col in columns:
                print(f"  - {col[1]} ({col[2]})")
            
            # Get row count
            cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
            count = cursor.fetchone()[0]
            print(f"Rows: {count}")
            
            # Show sample data for small tables
            if count > 0 and count <= 5:
                cursor.execute(f"SELECT * FROM {table_name};")
                rows = cursor.fetchall()
                print("Sample data:")
                for row in rows:
                    print(f"  {row}")
            elif count > 5:
                cursor.execute(f"SELECT * FROM {table_name} LIMIT 3;")
                rows = cursor.fetchall()
                print("Sample data (first 3 rows):")
                for row in rows:
                    print(f"  {row}")
                print(f"  ... and {count - 3} more rows")
        
        conn.close()
        
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    inspect_database()
