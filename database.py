import json

DATABASE_FILE = 'database.json'

def load_data():
    try:
        with open(DATABASE_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"students": []}

def save_all(collection, data):
    try:
        current_data = load_data()
        current_data[collection] = data
        with open(DATABASE_FILE, 'w') as file:
            json.dump(current_data, file, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

def fetch_all(collection):
    data = load_data()
    return data.get(collection, [])
