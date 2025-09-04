import os

base_dir = "Ransomware_Lab"
folders = [
    "dummy_files",
    "dummy_logs",
    "scripts"
]
files = [
    "README.md",
    "key_store.json"
]
script_files = [
    "loader.py",
    "encryptor.py",
    "key_handler.py",
    "persistence.ps1",
    "ransom_note.py",
    "cleanup.py"
]

dummy_txt_files = ["test1.txt", "test2.txt"]
dummy_docx_files = ["doc1.docx", "doc2.docx"]
dummy_log_files = ["log1.log", "log2.log"]

# Create base directory
os.makedirs(base_dir, exist_ok=True)

# Create folders
for folder in folders:
    os.makedirs(os.path.join(base_dir, folder), exist_ok=True)

# Create files in base directory
for file in files:
    open(os.path.join(base_dir, file), "w").close()

# Create script files
for script in script_files:
    open(os.path.join(base_dir, "scripts", script), "w").close()

# Create dummy .txt and .docx files
for txt in dummy_txt_files:
    open(os.path.join(base_dir, "dummy_files", txt), "w").close()
for docx in dummy_docx_files:
    open(os.path.join(base_dir, "dummy_files", docx), "w").close()

# Create dummy log files
for log in dummy_log_files:
    open(os.path.join(base_dir, "dummy_logs", log), "w").close()

print("Lab structure created successfully.")