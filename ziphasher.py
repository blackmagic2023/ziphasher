import subprocess
import sys
import os

def generate_zip_hash(zip_file_path, hash_file_path):
    try:
        # Run zip2john to generate the hash and redirect the output to the hash file
        with open(hash_file_path, 'w') as hash_file:
            subprocess.run(['zip2john', zip_file_path], stdout=hash_file, check=True)
        print(f"Hash has been generated and saved to {hash_file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error running zip2john: {e}")
        sys.exit(1)

def run_john(hash_file_path, password_list_path):
    try:
        # Run John the Ripper on the hash file with the provided password list
        result = subprocess.run(['john', '--wordlist=' + password_list_path, hash_file_path], capture_output=True, text=True, check=True)
        print(f"John the Ripper results:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error running John the Ripper: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 ziphasher.py <zip_file_path> <hash_file_path> <password_list_path>")
        sys.exit(1)

    zip_file_path = sys.argv[1]
    hash_file_path = sys.argv[2]
    password_list_path = sys.argv[3]

    if not os.path.isfile(zip_file_path):
        print(f"Error: ZIP file '{zip_file_path}' not found.")
        sys.exit(1)

    if not os.path.isfile(password_list_path):
        print(f"Error: Password list file '{password_list_path}' not found.")
        sys.exit(1)

    generate_zip_hash(zip_file_path, hash_file_path)
    run_john(hash_file_path, password_list_path)
