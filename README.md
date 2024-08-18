# SimpleAV

**SimpleAV** is a straightforward antivirus tool that scans files for viruses and malware efficiently. It supports configuration management and is compatible with both Linux and Windows.

## Features

- **Advanced Virus Scanning**: 🦠 Detects known viruses and malware using top repositories.
- **Configuration Management**: 🛠️ Manage settings with the `config.ini` file.
- **Cross-Platform Compatibility**: 🌐 Bash script for automated file downloads on both Linux and Windows.
- **Automated Process**: 🔄 Automatically downloads certification files using a Bash script.

## Installation

1. **Clone the Repository**: 🧑‍💻
 Open your terminal or command prompt and run:
   ```bash
   git clone https://github.com/ofek5082/SimpleAV.git

   
 2. **Download Certification Files**: 🚀
    Navigate to the project directory and run:
    ```bash
    cd SimpleAV
    bash download_certs.sh

3. **Update Configuration**: 📝 Edit the config.ini file to set your scan preferences and paths.

 4. **Run the Scanner**: ⚙️ Execute the scan with:
    ```bash
    python simpleav.py

## **🖼️ Screenshots**
(Add screenshots or terminal outputs here if applicable.)

## **📄 Example**
To scan a file using the default settings, run:

`bash
python simpleav.py

## **🤝 Contributing**
Feel free to fork the repository and submit pull requests. For major changes or feature requests, please open an issue first to discuss your ideas.

## **📜 License**
This project is licensed under the MIT License. See the LICENSE file for details.

## **📫 Contact**
For questions or suggestions, reach out to me at your-email@example.com.
