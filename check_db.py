import sqlite3
from pathlib import Path

def check_database():
    db_path = Path('db.sqlite3')
    if not db_path.exists():
        print("Error: Database file not found at", db_path.absolute())
        return
    
    print(f"Database found at: {db_path.absolute()}")
    print(f"Size: {db_path.stat().st_size / (1024 * 1024):.2f} MB\n")
    
    try:
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()
        
        # List all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
        tables = cursor.fetchall()
        
        print(f"Found {len(tables)} tables:")
        for table in tables:
            table_name = table[0]
            print(f"\n=== Table: {table_name} ===")
            
            # Get column info
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns = cursor.fetchall()
            print("Columns:")
            for col in columns:
                print(f"  - {col[1]} ({col[2]})")
            
            # Get row count
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            count = cursor.fetchone()[0]
            print(f"Rows: {count}")
            
            # Show sample data
            if count > 0:
                print("Sample data (first 3 rows):")
                cursor.execute(f"SELECT * FROM {table_name} LIMIT 3")
                rows = cursor.fetchall()
                for row in rows:
                    print(f"  {row}")
        
        conn.close()
        print("\nDatabase check completed successfully!")
        
    except Exception as e:
        print(f"Error accessing database: {e}")

if __name__ == "__main__":
    check_database()
