import json
from pathlib import Path

DB_FILE = Path("database.json")

def load_records():
    if DB_FILE.exists():
        try:
            return json.loads(DB_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print("Warning: database file is invalid. Starting with an empty database.")
    return []

def save_records(records):
    DB_FILE.write_text(json.dumps(records, indent=4), encoding="utf-8")

def normalize(value):
    return " ".join(value.strip().lower().split())

def add_record(records, name, email):
    name, email = name.strip(), email.strip()
    if not name or not email or "@" not in email:
        print("Invalid data. Enter a name and a valid email address.")
        return records

    email_key = normalize(email)
    if any(normalize(item["email"]) == email_key for item in records):
        print("Duplicate detected! Record was not added.")
        return records

    records.append({"name": name, "email": email})
    save_records(records)
    print("Record added successfully.")
    return records

def main():
    records = load_records()
    print("=== Data Redundancy Removal System ===")
    print(f"Existing records: {len(records)}")
    while True:
        print("\n1. Add record\n2. View records\n3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            records = add_record(records, name, email)
        elif choice == "2":
            if not records:
                print("No records found.")
            else:
                print("\\nSaved records:")
                for number, record in enumerate(records, 1):
                    print(f"{number}. {record['name']} - {record['email']}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
