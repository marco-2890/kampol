# Key Handling (เก็บ key เป็น JSON)

def save_key(key, filename="key_store.json"):
    print(f"Saving key to {filename}")

if __name__ == "__main__":
    save_key("dummy_key")