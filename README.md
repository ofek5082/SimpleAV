# SimpleAV

**SimpleAV** is a straightforward antivirus tool that scans files for viruses and malware efficiently. It supports configuration management and is compatible with both Linux and Windows.

## Features

- **Advanced Virus Scanning**: 🦠 Detects known viruses and malware using top repositories.
- **Configuration Management**: 🛠️ Manage settings with the `config.ini` file.
- **Cross-Platform Compatibility**: 🌐 Bash script for automated file downloads on both Linux and Windows.
- **Automated Process**: 🔄 Automatically downloads certification files using a Bash script.

## Installation

1. **Clone the Repository**: 🧑‍💻 <br>
 Open your terminal or command prompt and run:
   ```bash
   git clone https://github.com/ofek5082/SimpleAV.git
 <br>
   
 2. **Download Certification Files**: 🚀 <br>
    Navigate to the project directory and run:
    ```bash
    cd SimpleAV
    bash AutoCertDownload.sh  
  <br>
  
 - **Windows Alternative**: <br> You can run the bat file to automatically get the cert files. <br>
     [SimpleAV/AutoCertDownload.bat](AutoCertDownload.bat)
    <br>
 <br>

3. **Update Configuration**: 📝 <br>
     Edit the config.ini file to set your scan preferences and paths.

    ```bash
    [Settings]
    scan_path = C:\  # By default, can be changed
    cert_files = cert1-5.txt  # No need to change . 
 <br>
 
 4. **Run the Scanner**: ⚙️ <br>
     Execute the scan with:
     ```bash
     python simpleav.py
 <br>
 
 ## **🖼️ Screenshots**
(In progress)

## **🤝 Contributing**
Feel free to fork the repository and submit pull requests. For major changes or feature requests, please open an issue first to discuss your ideas.

## **📜 License**
This project is licensed under the MIT License. See the LICENSE file for details.

## **📫 Contact**
For questions or suggestions, reach out to me at ofekbendavid5082@gmail.com .
