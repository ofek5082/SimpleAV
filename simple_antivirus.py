// Importing libraries //
  import hashlib 
  import os

// load the bad hashes from certification file //
def load_certification_file(cert_file_path):
    with open(cert_file_path, 'r') as file:
      bad_hashes = set(line.strip() for line in file)
    return bad_hashes

// Calculate Sha-256 hash of given file //
def get_file_hash(file_path)
    hash_algo = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hash_algo.update(chunk)
    return hash_algo.hexdigest()

// Scan files in the specified directory for known bad hashes //
def scan_directory(directory_path, cert_file_path):
    bad_hashes = load_certification_file(cert_file_path)
    for root, _, files in os.walk(directory_path):
      for file_name in files:
    file_path = os.path.join(root, file_name)
    try:
      file_hash = get_file_hash(file_path)
      if file_hash in bad_hashes:
        print(f"Warning: {file_path} contains a known bad signature!")
    except Exception as e:
        print(f"Eroor scanning {file_path}: {e}")

// Usage Example //
if __name__ == "__main__":
  directory_to_scan = 'path/to/scan' #Replace with the directory you want to scan
  certification_file = 'certification.txt ' #Replace with your certification file path 

scan_directory(direction_to_scan, certification_file)


## To run the script use a terminal 
## python simple_antivirus.py
##
