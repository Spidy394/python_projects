import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('mess_expense.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS expense (
               id INTEGER PRIMARY KEY,
               month TEXT NOT NULL,
               room_rent INTEGER,
               electric_bill INTEGER,
               food INTEGER,
               total INTEGER
    )
''')

def update_ids():
    cursor.execute("SELECT id FROM expense ORDER BY id")
    rows = cursor.fetchall()
    for index, row in enumerate(rows, start=1):
        cursor.execute("UPDATE expense SET id = ? WHERE id = ?", (index, row[0]))
    conn.commit()

def is_table_empty():
    cursor.execute("SELECT COUNT(*) FROM expense")
    count = cursor.fetchone()[0]
    return count == 0

def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer")

def get_value_from_table(column, data_id):
    cursor.execute(f"SELECT {column} FROM expense WHERE id = ?", (data_id,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        print(f"No data found for id {data_id}")
        return None

def list_data():
    cursor.execute("SELECT * FROM expense")
    rows = cursor.fetchall()
    headers = ["ID", "Month", "Room Rent", "Electric Bill", "Food", "Total"]
    table = tabulate(rows, headers, tablefmt="pretty", colalign=("=", "=", "=", "=", "=", "="))
    print("\n" + table + "\n")

def add_data():
    while True:
        month = input("Enter month: ")
        room_rent = get_integer_input("Enter room rent: ")
        electric_units = get_integer_input("Enter electric units used: ")
        food = get_integer_input("Enter food cost: ")
        if (electric_units == 0): electric_bill = 0
        else: electric_bill = electric_units * 8.5 + 25
        total = room_rent + electric_bill + food
        cursor.execute("INSERT INTO expense (month, room_rent, electric_bill, food, total) VALUES (?, ?, ?, ?, ?)", (month, room_rent, electric_bill, food, total))
        conn.commit()
        print("Entry added!")
        list_data()
        repeat = input("Do you want to add another entry (y/n): ")
        if repeat.lower() != 'y':
            break

def update_data():
    while True:
        list_data()
        data_id = input("Enter data id to be updated: ")
        print("1. Month")
        print("2. Room Rent")
        print("3. Electric Bill")
        print("4. Food")
        update_choice = input("Select update field: ")
        old_room_rent = get_value_from_table("room_rent", data_id)
        old_electric_bill = get_value_from_table("electric_bill", data_id)
        old_food = get_value_from_table("food", data_id)
        match update_choice:
            case '1':
                new_month = input("Enter month: ")
                cursor.execute("UPDATE expense SET month = ? WHERE id = ?", (new_month, data_id))
            case '2':
                new_room_rent = get_integer_input("Enter room rent: ")
                new_total = new_room_rent + old_electric_bill + old_food
                cursor.execute("UPDATE expense SET room_rent = ?, total = ? WHERE id = ?", (new_room_rent, new_total, data_id))
            case '3':
                new_electric_unit = get_integer_input("Enter eletric units: ")
                if (new_electric_unit != 0): new_electric_bill = new_electric_unit * 8.5 + 25
                else: new_electric_bill = 0
                new_total = old_room_rent + new_electric_bill + old_food
                cursor.execute("UPDATE expense SET electric_bill = ?, total = ? WHERE id = ?", (new_electric_bill, new_total, data_id))
            case '4':
                new_food = get_integer_input("Enter food cost: ")
                new_total = old_room_rent + old_electric_bill + new_food
                cursor.execute("UPDATE expense SET food = ?, total = ? WHERE id = ?", (new_food, new_total, data_id))
            case _:
                print("Invalid input!")
        conn.commit()
        print("Entry updated!")
        list_data()
        repeat = input("Do you want to update another entry (y/n): ")
        if repeat.lower() != 'y':
            break

def delete_data():
    while not is_table_empty():
        list_data()
        data_id = input("Enter data id to be deleted: ")
        cursor.execute("DELETE FROM expense WHERE id = ?", (data_id,))
        conn.commit()
        print("Data deleted!")
        update_ids()
        if is_table_empty():
            print("\n" + "*" * 70 + "\nNo more data remaining!\n" + "*" * 70)
        else:
            repeat = input("Do you want to delete another entry (y/n): ")
            if repeat.lower() != 'y':
                break

def main():
    while True:
        a = 1
        print("\n|| Mess Expense Tracker ||\n")
        print(f"{a}. Add Entry")
        if not is_table_empty():
            print(f"{a+1}. View Data")   
            print(f"{a+1}. Update Entry")
            print(f"{a+1}. Delete Entry")
        print(f"{a+1}. Exit app")
        choice = input("Enter your choice: ")

        match choice: 
            case '1':
                add_data()
            case '2':
                list_data()
            case '3':
                update_data()
            case '4':
                delete_data()   
            case '5':
                print("Thank you! Have a great day!")
                break
            case _:
                print("Invalid choice!!")

    conn.close()
                      
if __name__ == "__main__":
    main()
