#// Importing libraries //
  import hashlib 
  import os
  import configparser 

#// load the bad hashes from certification files //
def load_certification_files(cert_files):
    bad_hashes = set()
    for cert_file in cert_files:
      with open(cert_file, 'r') as file:
          bad_hashes.update(line.strip() for line in file)
    return bad_hashes

#// Calculate Sha-256 hash of given file //
def get_file_hash(file_path):
    hash_algo = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hash_algo.update(chunk)
    return hash_algo.hexdigest()

#// Scan files in the specified directory for known bad hashes //
def scan_directory(directory_path, cert_files):
    bad_hashes = load_certification_files(cert_files)
    for root, _, files in os.walk(directory_path):
      for file_name in files:
          file_path = os.path.join(root, file_name)
          try:
              file_hash = get_file_hash(file_path)
              if file_hash in bad_hashes:
               print(f"Warning: {file_path} contains a known bad signature!")
          except Exception as e:
              print(f"Eroor scanning {file_path}: {e}")
            

#// Usage Example //
if __name__ == "__main__":
  config = configparser.ConfigParser()
  config.read('config.ini') #// Reads config file

  
  directory_to_scan = config.get('Settings', 'directory_to_scan')
  certification_file = [file.strip() for file in config.get('Settings', 'certification_files').split(',')] #Replace with your certification file path 

  scan_directory(directory_to_scan, certification_files)


## To run the script use a terminal 
## python simple_antivirus.py
##
